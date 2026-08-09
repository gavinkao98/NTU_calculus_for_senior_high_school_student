#!/usr/bin/env python3
"""Quote linter / fixer for the live HTML handout (CONTENT_SPEC §8).

Enforces: rendered prose uses Unicode curly quotes “…” / ‘…’ and the
curly apostrophe ’ (U+2019); ASCII straight quotes (" and ') are NOT
allowed in prose.

It is deliberately scoped to *rendered prose*. A structural classifier
excludes, and never touches, ASCII quotes that legitimately stay ASCII:

  - math      : the prime in \\(f'\\), \\[f''\\], $f'$ — MathJax notation
  - tag       : HTML attribute values, e.g. class="sec"
  - code/kbd  : literal syntax shown to the reader
  - comment   : <!-- authoring notes --> (not rendered)

Only ASCII ' or " that survive that filter — i.e. sit in running prose —
are reported (or rewritten with --fix). Stdlib-only (matches build.py),
so CI needs no pip install.

2026-08-09 (LaTeX unification): also lints the LaTeX sources. For `.tex` the
excluded spans are `%` line comments (escaped percents stay prose) and math
(`\\(..\\)` / `\\[..\\]`); everything else is prose. Default targets =
latex/src/**/*.tex (the live sources) + html/fragments/**/*.html (frozen).

Usage:
    python handout/html/quote_lint.py         # lint latex/src + frozen fragments
    python handout/html/quote_lint.py --fix   # rewrite prose ASCII quotes -> curly
    python handout/html/quote_lint.py PATH ...  # lint/fix specific files or dirs

Conversion (--fix):
    prose '  ->  ’  (U+2019)        apostrophe / closing single — unambiguous
    prose "  ->  “ / ”             alternating per file in document order
                                    (handout prose uses flat, non-nested pairs;
                                    an odd count per file is refused so a stray
                                    quote is never mis-paired — fix it by hand).
After --fix, review the diff and re-run `python handout/html/build.py`.

Exit code (lint mode) 0 = clean, 1 = violations found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

SPAN_PATTERNS = [
    ("comment", re.compile(r"<!--.*?-->", re.S)),
    ("math", re.compile(r"\\\[.*?\\\]", re.S)),
    ("math", re.compile(r"\\\(.*?\\\)", re.S)),
    ("math", re.compile(r"\$\$.*?\$\$", re.S)),
    ("math", re.compile(r"(?<![\\$])\$(?!\$).+?(?<![\\$])\$(?!\$)", re.S)),
    ("code", re.compile(r"<code[^>]*>.*?</code>", re.S)),
    ("code", re.compile(r"<kbd[^>]*>.*?</kbd>", re.S)),
    ("tag", re.compile(r"<[^>]+>", re.S)),
]
TEX_SPAN_PATTERNS = [
    ("comment", re.compile(r"(?<!\\)%[^\n]*")),
    ("math", re.compile(r"\\\[.*?\\\]", re.S)),
    ("math", re.compile(r"\\\(.*?\\\)", re.S)),
]
_EXCLUDE_KINDS = ("comment", "math", "code", "tag")
RSQUO, LDQUO, RDQUO = "’", "“", "”"


def _patterns_for(suffix: str):
    return TEX_SPAN_PATTERNS if suffix == ".tex" else SPAN_PATTERNS


def _build_spans(text: str, suffix: str = ".html") -> list[tuple[int, int, str]]:
    spans = []
    for kind, pat in _patterns_for(suffix):
        for m in pat.finditer(text):
            spans.append((m.start(), m.end(), kind))
    return spans


def _in_excluded_span(pos: int, spans: list[tuple[int, int, str]]) -> bool:
    for kind in _EXCLUDE_KINDS:
        for s, e, k in spans:
            if k == kind and s <= pos < e:
                return True
    return False


def _prose_positions(text: str, spans):
    """Yield (pos, char) for each ASCII ' or " that sits in rendered prose."""
    for m in re.finditer(r"['\"]", text):
        if not _in_excluded_span(m.start(), spans):
            yield m.start(), m.group()


def lint_text(text: str, suffix: str = ".html") -> list[tuple[int, str, str]]:
    """Return [(line_no, char, context), ...] for prose ASCII-quote violations."""
    spans = _build_spans(text, suffix)
    out = []
    for pos, ch in _prose_positions(text, spans):
        line_no = text.count("\n", 0, pos) + 1
        ctx = text[max(0, pos - 30):pos + 30].replace("\n", " ")
        out.append((line_no, ch, ctx))
    return out


def fix_text(text: str, suffix: str = ".html") -> tuple[str, int]:
    """Rewrite prose ASCII quotes to curly. Returns (new_text, n_changed).

    Raises ValueError if a file has an odd number of prose double quotes
    (a stray " that cannot be paired) so the author can resolve it by hand.
    """
    spans = _build_spans(text, suffix)
    prose = list(_prose_positions(text, spans))
    dq = [p for p, ch in prose if ch == '"']
    if len(dq) % 2 != 0:
        raise ValueError(
            f"odd number of prose double quotes ({len(dq)}) — a stray \" cannot "
            f"be paired; fix manually"
        )
    repl = {}
    for p, ch in prose:
        if ch == "'":
            repl[p] = RSQUO
    for i, p in enumerate(dq):
        repl[p] = LDQUO if i % 2 == 0 else RDQUO
    if not repl:
        return text, 0
    buf, last = [], 0
    for p in sorted(repl):
        buf.append(text[last:p])
        buf.append(repl[p])
        last = p + 1
    buf.append(text[last:])
    return "".join(buf), len(repl)


def _iter_sources(paths: list[Path]):
    for p in paths:
        if p.is_dir():
            yield from sorted(p.rglob("*.html"))
            yield from sorted(p.rglob("*.tex"))
        elif p.suffix in (".html", ".tex"):
            yield p


def main(argv: list[str]) -> int:
    do_fix = "--fix" in argv
    args = [a for a in argv if a != "--fix"]
    if args:
        targets = [Path(a) for a in args]
    else:
        here = Path(__file__).resolve().parent
        targets = [here.parent / "latex" / "src", here / "fragments"]

    files = list(_iter_sources(targets))

    if do_fix:
        total = 0
        for fp in files:
            text = fp.read_text(encoding="utf-8")
            try:
                new_text, n = fix_text(text, fp.suffix)
            except ValueError as exc:
                print(f"{fp}: {exc}", file=sys.stderr)
                return 1
            if n:
                fp.write_text(new_text, encoding="utf-8", newline="")
                total += n
                print(f"{fp}: fixed {n} prose ASCII quote(s)")
        if total:
            print(
                f"\nquote_lint --fix: rewrote {total} prose quote(s) across "
                f"{len(files)} file(s). Review the diff and re-run "
                f"`python handout/html/build.py`."
            )
        else:
            print(f"quote_lint --fix: nothing to fix — {len(files)} file(s) already clean.")
        return 0

    total = 0
    for fp in files:
        text = fp.read_text(encoding="utf-8")
        violations = lint_text(text, fp.suffix)
        if violations:
            total += len(violations)
            for line_no, ch, ctx in violations:
                kind = "apostrophe/single" if ch == "'" else "double quote"
                print(f"{fp}:{line_no}: ASCII {kind} in prose — use a curly quote (§8): …{ctx}…")

    if total:
        print(
            f"\nquote_lint: {total} prose ASCII-quote violation(s) in "
            f"{len(files)} file(s). Run `python handout/html/quote_lint.py --fix` "
            f"to auto-convert, then re-run `python handout/html/build.py`.",
            file=sys.stderr,
        )
        return 1
    print(f"quote_lint: clean — {len(files)} file(s), no prose ASCII quotes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
