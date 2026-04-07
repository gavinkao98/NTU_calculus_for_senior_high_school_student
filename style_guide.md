# Calculus Book Style Guide

## Core Rule
Treat each manuscript as a content source, not a layout source.

Preserve only:
- mathematical meaning
- logical structure
- pedagogical intent

## Approved Structure
Use the hierarchy:
- Chapter
- Section
- Subsection

Avoid deeper levels unless necessary.

## Approved Environments
Use only:
- `definition`
- `theorem`
- `lemma`
- `proposition`
- `corollary`
- `example`
- `remark`
- `exercise`
- `proof` (standard environment)

## Strict Source Rules
- Use explicit standard LaTeX.
- Do not invent macros unless explicitly requested.
- Do not use single-letter macros.
- Do not redefine standard LaTeX commands.
- Do not use shorthand wrappers for theorem environments.

## Numbering Policy
Use chapter-based numbering for:
- theorem-like environments
- equations
- figures
- tables

## Notation Policy
Use consistent notation throughout the book.

Preferred examples:
- `\arcsin x`, `\arccos x`, `\arctan x`
- `e^x`
- `\ln x`
- `\sin`, `\cos`, `\tan`, `\exp`
- `f'(x)` for general discussion
- `\dfrac{d}{dx}` for explicit calculations
- `\lim_{x\to a} f(x)=L`
- `\lim_{x\to a^-}`, `\lim_{x\to a^+}`
- `(a,b)`, `[a,b]`
- `\mathbb{R}`

## Terminology Policy
Choose one standard term for each concept and use it consistently.

Examples:
- use one of: squeeze theorem / sandwich theorem / squeezing lemma
- use one of: inverse sine / arcsine
- use one of: one-to-one / injective
- use one of: increasing / strictly increasing

## Section Writing Order
When possible, organize material in this order:
1. introduction or recall
2. definitions
3. properties and theorems
4. proofs
5. examples
6. exercises

## Figure Policy
For each manuscript figure, classify it as one of the following:
- Redraw
- Simplify
- Replace

Do not preserve handwritten figures by default.

## Exercise Policy
- Keep examples in the exposition.
- Move exercises to the end of the relevant section or chapter.
- Rewrite homework prompts as complete, grammatically clear exercise statements.

## Final Check Before Accepting a Chapter
- only approved environments are used
- notation is consistent
- terminology is consistent
- no custom shortcuts were introduced
- no single-letter macros were introduced
- theorem and proof structure is explicit
- exercises are properly relocated
- figures are classified correctly
- tone matches a formal textbook
- source code is readable by both humans and AI
