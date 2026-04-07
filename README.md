# Calculus Book Project Skeleton

This project skeleton is designed for a multi-author calculus textbook that will be normalized into a single textbook-style LaTeX source.

## Directory Overview
- `main.tex`: global document structure only
- `preamble/`: centralized package, layout, theorem, numbering, and bibliography setup
- `chapters/`: one file per chapter
- `figures/`: figures organized by chapter
- `refs/`: bibliography database
- `style_guide.md`: editorial and AI writing rules

## Workflow
1. Choose a manuscript section.
2. Extract semantic units.
3. Rewrite them into standard textbook prose.
4. Place the output into the appropriate chapter file.
5. Classify each figure as redraw, simplify, or replace.
6. Run a consistency check.
