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


CHECKS: tuple[tuple[str, re.Pattern[str]], ...] = (
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
)


def iter_tex_files() -> list[Path]:
    files: list[Path] = [ROOT / name for name in TEX_FILES if (ROOT / name).exists()]
    for folder in TEX_ROOTS:
        base = ROOT / folder
        if base.exists():
            files.extend(sorted(base.rglob("*.tex")))
    return files


def lint_file(path: Path) -> list[Violation]:
    violations: list[Violation] = []
    for line_number, raw_line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
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
        for message, pattern in CHECKS:
            if pattern.search(line):
                violations.append(
                    Violation(
                        path=path,
                        line_number=line_number,
                        message=message,
                        line=raw_line.strip(),
                    )
                )
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
