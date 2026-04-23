from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
TEX_ROOTS = ("chapters", "frontmatter")
TEX_FILES = ("main.tex",)


@dataclass
class Violation:
    path: Path
    line_number: int
    message: str
    line: str


def strip_comments(line: str) -> str:
    escaped = False
    pieces: list[str] = []
    for char in line:
        if char == "%" and not escaped:
            break
        pieces.append(char)
        escaped = (char == "\\") and not escaped
        if char != "\\":
            escaped = False
    return "".join(pieces)


# Per-line regex checks. Each tuple is (human-readable message, compiled pattern).
# A match on any line of a chapter file (after comment-stripping) is a violation.
LINE_CHECKS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "manual cross-reference prefix; use cleveref instead",
        re.compile(
            r"\\(?:Figure|Theorem|Section|Chapter|Lemma|Proposition|Corollary|Definition|Example|Exercise|Remark)~\\ref\{"
        ),
    ),
    (
        "manual page break command is disallowed here",
        re.compile(r"\\(?:newpage|pagebreak|clearpage)\b"),
    ),
    (
        "bold emphasis in prose is disallowed; use \\emph{} instead (CONTENT_README.md v3.0 \u00a78)",
        re.compile(r"\\textbf\{"),
    ),
    (
        "italic emphasis in prose is disallowed; use \\emph{} instead (CONTENT_README.md v3.0 \u00a78)",
        re.compile(r"\\textit\{"),
    ),
)


# Whole-file structural checks.
# These run on the combined (comment-stripped) text of a chapter file rather
# than line-by-line, because they reason about block structure (definition
# bodies, named-theorem proximity to \index{}, etc.).

_DEFINITION_BLOCK_RE = re.compile(
    r"\\begin\{definition\}(?P<body>.*?)\\end\{definition\}",
    re.DOTALL,
)
_DEFINITION_LABEL_RE = re.compile(r"\\label\{def:([^}]+)\}")
_INDEX_IN_BLOCK_RE = re.compile(r"\\index\{")
_NAMED_THEOREM_RE = re.compile(
    r"\\begin\{theorem\}\[(?P<name>[^\]]+)\]",
)


def _find_line_number(text: str, offset: int) -> int:
    """Return 1-indexed line number for a character offset in ``text``."""
    return text.count("\n", 0, offset) + 1


def check_definitions_have_index(path: Path, text: str) -> list[Violation]:
    """Every \\begin{definition} body MUST contain at least one \\index{...} entry,
    except when the block is a paired *precise* restatement (label ending in
    ``-precise``), since the term was already indexed at its informal first
    occurrence (CONTENT_README.md v3.0 \u00a711 rule: place index at first
    occurrence only).
    """
    violations: list[Violation] = []
    for match in _DEFINITION_BLOCK_RE.finditer(text):
        body = match.group("body")
        if _INDEX_IN_BLOCK_RE.search(body):
            continue
        # Exempt paired precise restatements.
        label_match = _DEFINITION_LABEL_RE.search(body)
        if label_match and label_match.group(1).endswith("-precise"):
            continue
        line_number = _find_line_number(text, match.start())
        snippet_line = text.splitlines()[line_number - 1].strip() if line_number - 1 < len(text.splitlines()) else ""
        violations.append(
            Violation(
                path=path,
                line_number=line_number,
                message=(
                    "definition body lacks \\index{...}; every defined term must be indexed "
                    "at its first occurrence (CONTENT_README.md v3.0 \u00a711)"
                ),
                line=snippet_line,
            )
        )
    return violations


def check_named_theorems_have_index(path: Path, text: str) -> list[Violation]:
    """Every \\begin{theorem}[Name] MUST have a matching \\index{...} entry nearby.

    ``Nearby`` is operationalised as: within 400 characters after the theorem
    start. The match is case-insensitive and ignores leading/trailing spaces;
    the index key may contain an ``@`` sort-key split.
    """
    violations: list[Violation] = []
    for match in _NAMED_THEOREM_RE.finditer(text):
        name = match.group("name").strip().lower()
        window = text[match.end() : match.end() + 400]
        # Extract all \index{...} entries in the window and pull out the sort key
        # (portion before ``@``, or the whole argument if no ``@``).
        keys = []
        for idx_match in re.finditer(r"\\index\{([^}]*)\}", window):
            arg = idx_match.group(1)
            key = arg.split("@", 1)[0].strip().lower()
            keys.append(key)
        if any(key == name for key in keys):
            continue
        line_number = _find_line_number(text, match.start())
        snippet_line = text.splitlines()[line_number - 1].strip() if line_number - 1 < len(text.splitlines()) else ""
        violations.append(
            Violation(
                path=path,
                line_number=line_number,
                message=(
                    f"named theorem ``{match.group('name')}'' has no matching \\index{{{name}}} "
                    f"within 400 characters (CONTENT_README.md v3.0 \u00a76)"
                ),
                line=snippet_line,
            )
        )
    return violations


# TODO(v3.x content migration): add a fourth block check enforcing the
# chapter-opening structure required by CONTENT_README.md v3.0 \u00a74:
#   every chapter file MUST open with \chapter{...} followed by a 1-2 paragraph
#   overview followed by a "\paragraph{By the end of this chapter, you will
#   be able to:}" learning-outcomes bullet list.
# Deferred until the existing chapters/ch01_foundations.tex has been migrated
# to the new chapter-opening pattern. Turning this check on before that
# migration would intentionally break CI; the rule in CONTENT_README is
# already authoritative, and this lint check is the enforcement layer that
# catches violations after the first migration pass.

BLOCK_CHECKS = (
    check_definitions_have_index,
    check_named_theorems_have_index,
)


def iter_tex_files() -> list[Path]:
    files: list[Path] = [ROOT / name for name in TEX_FILES if (ROOT / name).exists()]
    for folder in TEX_ROOTS:
        base = ROOT / folder
        if base.exists():
            files.extend(sorted(base.rglob("*.tex")))
    return files


def is_chapter_file(path: Path) -> bool:
    """Block-level checks only apply to real chapter sources, not main.tex or
    the scratch/template files.
    """
    if path.name.startswith("_"):
        return False
    return path.parent.name == "chapters"


def _strip_all_comments(text: str) -> str:
    return "\n".join(strip_comments(line) for line in text.splitlines())


def lint_file(path: Path) -> list[Violation]:
    violations: list[Violation] = []
    raw_lines = path.read_text(encoding="utf-8").splitlines()
    for line_number, raw_line in enumerate(raw_lines, start=1):
        line = strip_comments(raw_line)
        if not line:
            continue
        if '"' in line:
            violations.append(
                Violation(
                    path=path,
                    line_number=line_number,
                    message="straight ASCII quotes are disallowed in TeX source",
                    line=raw_line.strip(),
                )
            )
        for message, pattern in LINE_CHECKS:
            if pattern.search(line):
                violations.append(
                    Violation(
                        path=path,
                        line_number=line_number,
                        message=message,
                        line=raw_line.strip(),
                    )
                )

    # Block-level checks run on the comment-stripped text of real chapter files.
    if is_chapter_file(path):
        stripped_text = _strip_all_comments(path.read_text(encoding="utf-8"))
        for check in BLOCK_CHECKS:
            violations.extend(check(path, stripped_text))

    return violations


def main() -> int:
    violations: list[Violation] = []
    for path in iter_tex_files():
        violations.extend(lint_file(path))

    if not violations:
        print("style_lint: ok")
        return 0

    for violation in violations:
        rel_path = violation.path.relative_to(ROOT)
        print(f"{rel_path}:{violation.line_number}: {violation.message}")
        print(f"  {violation.line}")
    print(f"style_lint: {len(violations)} violation(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
