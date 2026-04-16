#!/usr/bin/env python3
"""Sync edited narration from a _final.md file back into the storyboard YAML.

Usage
-----
    python tools/sync_narration_back.py --deck-id ch01_inverse_functions

Workflow
-------
1. Run ``render_manim_lesson.py`` (or the export step) to produce ``_final.md``.
2. Open ``_final.md`` and edit the narration text under each scene's
   ``Narration:`` heading.  Do **not** change the ``Slide ID`` lines — they are
   used to match edits back to the correct scene.
3. Run this script.  It reads the edited ``_final.md``, compares each scene's
   narration with the storyboard YAML, and writes back any changes.
4. A summary is printed showing which scenes were updated.

The script is intentionally conservative:

- It never touches ``data``, ``timing``, ``template``, or any field other than
  ``voiceover``.
- It refuses to run if a scene ID in the markdown cannot be found in the YAML.
- It creates a ``.bak`` copy of the YAML before writing.
"""
from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

# ---- bootstrap so sibling modules are importable ----
_TOOLS_DIR = Path(__file__).resolve().parent
if str(_TOOLS_DIR) not in sys.path:
    sys.path.insert(0, str(_TOOLS_DIR))

from media_paths import manim_narration_path, manim_storyboard_path
from runtime_bootstrap import REPO_ROOT

# ---------------------------------------------------------------------------
# Markdown parser — extracts (scene_id, narration) pairs from _final.md
# ---------------------------------------------------------------------------

_SLIDE_HEADER_RE = re.compile(r"^## Slide \d+:\s+.+$")
_SLIDE_ID_RE = re.compile(r"^Slide ID:\s*`([^`]+)`")


def parse_narration_md(text: str) -> dict[str, str]:
    """Return ``{scene_id: narration_text}`` from a ``_final.md`` file."""
    lines = text.splitlines()
    scenes: dict[str, str] = {}
    current_id: str | None = None
    collecting = False
    narration_lines: list[str] = []

    for line in lines:
        # Detect a new slide header — flush previous scene if any.
        if _SLIDE_HEADER_RE.match(line):
            if current_id is not None:
                scenes[current_id] = "\n".join(narration_lines).strip()
            current_id = None
            collecting = False
            narration_lines = []
            continue

        # Detect the Slide ID line.
        id_match = _SLIDE_ID_RE.match(line)
        if id_match:
            current_id = id_match.group(1)
            continue

        # Detect the "Narration:" marker — everything after this belongs to
        # the voiceover until the next slide header.
        if line.strip() == "Narration:":
            collecting = True
            continue

        if collecting:
            narration_lines.append(line)

    # Flush the last scene.
    if current_id is not None:
        scenes[current_id] = "\n".join(narration_lines).strip()

    return scenes


# ---------------------------------------------------------------------------
# YAML updater — surgically replaces voiceover values in the raw YAML text
# ---------------------------------------------------------------------------

import json  # noqa: E402 — keep imports grouped logically


def _yaml_escaped(text: str) -> str:
    """Return *text* as a JSON-encoded string (which is valid YAML scalar)."""
    return json.dumps(text, ensure_ascii=False)


def update_voiceovers_in_yaml(yaml_text: str, updates: dict[str, str]) -> str:
    """Return *yaml_text* with voiceover values replaced for the given scene IDs.

    The strategy:
    1. Walk through the YAML line by line.
    2. Track the most-recently-seen ``scene_id``.
    3. When a ``voiceover:`` key is encountered and the current scene_id is in
       *updates*, replace the value.

    This keeps all other formatting, comments, and field order intact.
    """
    lines = yaml_text.splitlines(keepends=True)
    result: list[str] = []
    current_scene_id: str | None = None
    remaining = dict(updates)

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip()

        # Detect scene_id
        if stripped.startswith("scene_id:"):
            value = stripped.split(":", 1)[1].strip().strip('"').strip("'")
            current_scene_id = value
            result.append(line)
            i += 1
            continue

        # Detect voiceover line for a scene we want to update.
        if stripped.startswith("voiceover:") and current_scene_id in remaining:
            indent = line[: len(line) - len(stripped)]
            new_vo = remaining.pop(current_scene_id)
            result.append(f"{indent}voiceover: {_yaml_escaped(new_vo)}\n")
            i += 1
            continue

        result.append(line)
        i += 1

    return "".join(result)


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Sync edited narration from _final.md back into the storyboard YAML."
    )
    parser.add_argument(
        "--deck-id",
        required=True,
        help="Deck identifier, e.g. ch01_inverse_functions.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing the YAML.",
    )
    parser.add_argument(
        "--script-file",
        type=Path,
        default=None,
        help="Override the path to the edited _final.md.",
    )
    parser.add_argument(
        "--storyboard-file",
        type=Path,
        default=None,
        help="Override the path to the storyboard YAML.",
    )
    args = parser.parse_args()

    script_path = (args.script_file or manim_narration_path(REPO_ROOT, args.deck_id)).resolve()
    storyboard_path = (args.storyboard_file or manim_storyboard_path(REPO_ROOT, args.deck_id)).resolve()

    if not script_path.exists():
        print(f"ERROR: narration file not found: {script_path}", file=sys.stderr)
        print("Run render_manim_lesson.py first to export the narration file.", file=sys.stderr)
        sys.exit(1)
    if not storyboard_path.exists():
        print(f"ERROR: storyboard not found: {storyboard_path}", file=sys.stderr)
        sys.exit(1)

    # --- Parse the edited markdown ---
    md_text = script_path.read_text(encoding="utf-8")
    md_narrations = parse_narration_md(md_text)

    if not md_narrations:
        print("No narration sections found in the markdown file.")
        sys.exit(0)

    # --- Read the current YAML ---
    yaml_text = storyboard_path.read_text(encoding="utf-8")

    # --- Determine which scenes actually changed ---
    # Quick extraction of current voiceovers from the YAML for comparison.
    from simple_yaml import load_yaml  # noqa: E402

    current_storyboard = load_yaml(yaml_text)
    current_voiceovers: dict[str, str] = {}
    for scene in current_storyboard.get("scenes", []):
        sid = scene.get("scene_id", "")
        vo = scene.get("voiceover", "")
        current_voiceovers[sid] = vo

    # Validate: every scene_id from markdown must exist in the YAML.
    unknown_ids = set(md_narrations) - set(current_voiceovers)
    if unknown_ids:
        print(
            f"ERROR: the following scene IDs in the markdown are not in the storyboard: "
            f"{', '.join(sorted(unknown_ids))}",
            file=sys.stderr,
        )
        sys.exit(1)

    # Find actual changes.
    changes: dict[str, str] = {}
    for scene_id, new_text in md_narrations.items():
        old_text = current_voiceovers.get(scene_id, "")
        if new_text != old_text:
            changes[scene_id] = new_text

    if not changes:
        print("No narration changes detected. Storyboard is already up to date.")
        sys.exit(0)

    # --- Report ---
    print(f"Detected {len(changes)} narration change(s):\n")
    for scene_id in changes:
        old_preview = current_voiceovers[scene_id][:60].replace("\n", " ")
        new_preview = changes[scene_id][:60].replace("\n", " ")
        print(f"  [{scene_id}]")
        print(f"    old: {old_preview}...")
        print(f"    new: {new_preview}...")
        print()

    if args.dry_run:
        print("Dry run — no files modified.")
        sys.exit(0)

    # --- Write back ---
    backup_path = storyboard_path.with_suffix(".yml.bak")
    shutil.copy2(storyboard_path, backup_path)
    print(f"Backup saved: {backup_path.name}")

    updated_yaml = update_voiceovers_in_yaml(yaml_text, changes)
    storyboard_path.write_text(updated_yaml, encoding="utf-8")
    print(f"Storyboard updated: {storyboard_path.name}")
    print(f"\nDone. {len(changes)} scene(s) synced.")


if __name__ == "__main__":
    main()
