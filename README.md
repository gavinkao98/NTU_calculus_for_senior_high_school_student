# Calculus Textbook Project

This repository has two separate working tracks:

- textbook content authoring
- slide, audio, and video generation

Use the dedicated guides instead of treating this file as the full rulebook:

- [`CONTENT_README.md`](CONTENT_README.md): authoritative textbook writing and editorial rules
- [`VIDEO_README.md`](VIDEO_README.md): slide, narration, and video pipeline

## Repository Layout

- `main.tex`: main LaTeX entry point for the book
- `chapters/`: chapter source files
- `preamble/`: shared LaTeX setup
- `refs/`: bibliography data
- `tools/`: media-generation scripts
- `schemas/`: JSON schema files for generated deck data
- `inputs/`: reusable raw inputs such as source voice recordings
- `artifacts/`: generated slides, scripts, audio, and video outputs

## Which File To Read

If you are writing or revising textbook content:
- start with [`CONTENT_README.md`](CONTENT_README.md)
- then work in the relevant file under `chapters/`

If you are generating media:
- start with [`VIDEO_README.md`](VIDEO_README.md)
- then use the scripts under `tools/`

## Current Scope

The book source is general, but the media pipeline is currently a Chapter 1 prototype centered on:

- `chapters/ch01_foundations.tex`
- the section `Inverse Functions and One-to-One Functions`
- generated assets under `artifacts/`

## Notes

- `style_guide.md` is only a short redirect note now.
- Local caches, virtual environments, and vendored dependencies live in hidden repo folders such as `.cache/`, `.venv/`, `.deps/`, and `.deps_f5/`.
