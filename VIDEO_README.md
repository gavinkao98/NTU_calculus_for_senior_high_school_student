# Video Pipeline README

This file documents the slide, audio, and video generation workflow for this repository.

The textbook-writing rules live in [`CONTENT_README.md`](CONTENT_README.md).
The repository overview lives in [`README.md`](README.md).
This file is only about the media pipeline that turns chapter content into narrated slide videos.

## Purpose

The current video workflow is a prototype pipeline for one textbook section:

- source chapter content in LaTeX
- extract a section into a structured slide deck JSON
- render a Beamer slide deck
- synthesize narration per slide
- combine slide images and narration into an MP4

At the moment, the scripts are specialized to:

- source file: `chapters/ch01_foundations.tex`
- source section: `Inverse Functions and One-to-One Functions`
- deck id: `ch01_inverse_functions`

So this is a working pipeline for Chapter 1 media generation, not yet a general-purpose framework for all chapters.

## Directory Map

- `chapters/`: textbook source content
- `tools/`: Python scripts for media generation
- `schemas/`: JSON schema for generated deck data
- `inputs/voice/`: raw voice recordings used as reference input
- `artifacts/slide_spec/`: generated deck JSON
- `artifacts/slides/`: generated Beamer `.tex` and slide PDF
- `artifacts/scripts/`: generated narration script markdown
- `artifacts/voice/`: processed short reference clip for voice cloning
- `artifacts/audio/`: per-slide narration WAV files and synthesis manifests
- `artifacts/video/`: final MP4 files plus intermediate frames and segments
- `.deps/`: local Python dependencies used by most scripts
- `.deps_f5/`: extra local Python dependencies for F5-TTS
- `.cache/`: Hugging Face, torch, and TTS model caches

## Pipeline Overview

The current pipeline is:

1. Prepare a short reference voice clip.
2. Generate the structured deck JSON, Beamer source, and script markdown from the chapter.
3. Compile the Beamer slide deck into a PDF.
4. Synthesize slide-by-slide narration.
5. Render the final MP4 from the slide PDF and narration WAV files.

## Scripts

### `tools/preprocess_voice_reference.py`

Purpose:
- trims and normalizes a voice sample for cloning

Default input and output:
- input: `inputs/voice/my_voice.wav`
- output: `artifacts/voice/reference_30s.wav`

Example:

```powershell
python .\tools\preprocess_voice_reference.py
```

Useful options:
- `--start-seconds`
- `--duration-seconds`
- `--mono`
- `--peak`

### `tools/generate_inverse_functions_demo.py`

Purpose:
- reads the Chapter 1 LaTeX source
- extracts one specific section
- builds a structured deck JSON
- writes Beamer slide source
- writes a narration script markdown file
- optionally compiles the Beamer PDF

Generated files:
- `artifacts/slide_spec/ch01_inverse_functions.json`
- `artifacts/slides/ch01_inverse_functions.tex`
- `artifacts/slides/ch01_inverse_functions.pdf`
- `artifacts/scripts/ch01_inverse_functions.md`

Example:

```powershell
python .\tools\generate_inverse_functions_demo.py --compile auto
```

Compile modes:
- `--compile auto`: compile if LaTeX/Beamer tools are available
- `--compile never`: skip PDF compilation
- `--compile require`: fail if compilation prerequisites are missing

Beamer compilation depends on:
- `latexmk`
- `pdflatex`
- `beamer.cls`

### `tools/synthesize_section_audio.py`

Purpose:
- synthesizes one WAV file per slide using Coqui TTS

Default outputs:
- audio directory: `artifacts/audio/ch01_inverse_functions/`
- manifest: `artifacts/audio/ch01_inverse_functions/manifest.json`

Default mode:
- XTTS v2 voice cloning from `artifacts/voice/reference_30s.wav`

Basic example:

```powershell
python .\tools\synthesize_section_audio.py --coqui-tos-agreed
```

Important notes:
- XTTS v2 requires explicit agreement to Coqui CPML terms.
- Device can be selected with `--device auto|cpu|cuda`.
- The script writes one WAV per slide and a manifest with chunking metadata.

Example with built-in Jenny voice instead of cloning:

```powershell
python .\tools\synthesize_section_audio.py `
  --voice-mode builtin `
  --model-name tts_models/en/jenny/jenny `
  --output-dir artifacts\audio\ch01_inverse_functions_jenny `
  --manifest artifacts\audio\ch01_inverse_functions_jenny\manifest.json
```

Useful options:
- `--max-slides`
- `--split-sentences`
- `--speed`
- `--repetition-penalty`
- `--max-chars-per-chunk`
- `--inter-chunk-pause-ms`

### `tools/synthesize_section_audio_f5.py`

Purpose:
- synthesizes one WAV file per slide using F5-TTS

Default outputs:
- audio directory: `artifacts/audio/ch01_inverse_functions_f5_clone/`
- manifest: `artifacts/audio/ch01_inverse_functions_f5_clone/manifest.json`

Clone example:

```powershell
python .\tools\synthesize_section_audio_f5.py `
  --reference-mode clone `
  --output-dir artifacts\audio\ch01_inverse_functions_f5_clone `
  --manifest artifacts\audio\ch01_inverse_functions_f5_clone\manifest.json
```

Example-reference mode:

```powershell
python .\tools\synthesize_section_audio_f5.py `
  --reference-mode example `
  --output-dir artifacts\audio\ch01_inverse_functions_f5_example `
  --manifest artifacts\audio\ch01_inverse_functions_f5_example\manifest.json
```

Useful options:
- `--device auto|cpu|cuda`
- `--max-slides`
- `--nfe-step`
- `--cfg-strength`
- `--sway-sampling-coef`
- `--cross-fade-duration`
- `--speed`
- `--fix-duration`

### `tools/render_section_video.py`

Purpose:
- renders the slide PDF into images
- pairs each slide image with its narration WAV
- creates one MP4 segment per slide
- concatenates all segments into a final MP4

Default inputs and output:
- deck JSON: `artifacts/slide_spec/ch01_inverse_functions.json`
- slide PDF: `artifacts/slides/ch01_inverse_functions.pdf`
- audio directory: `artifacts/audio/ch01_inverse_functions/`
- final video: `artifacts/video/ch01_inverse_functions.mp4`

Basic example:

```powershell
python .\tools\render_section_video.py
```

Example using the Jenny audio set:

```powershell
python .\tools\render_section_video.py `
  --audio-dir artifacts\audio\ch01_inverse_functions_jenny `
  --output artifacts\video\ch01_inverse_functions_jenny.mp4
```

Useful options:
- `--dpi-scale`
- `--lead-in-seconds`
- `--target-width`
- `--target-height`
- `--crf`

The renderer also creates intermediate files under:
- `artifacts/video/<output_stem>/frames/`
- `artifacts/video/<output_stem>/segments/`
- `artifacts/video/<output_stem>/segments.txt`

## End-to-End Examples

### Path A: Beamer slides + Coqui XTTS clone + MP4

```powershell
python .\tools\preprocess_voice_reference.py
python .\tools\generate_inverse_functions_demo.py --compile auto
python .\tools\synthesize_section_audio.py --coqui-tos-agreed
python .\tools\render_section_video.py
```

### Path B: Beamer slides + built-in Jenny voice + MP4

```powershell
python .\tools\generate_inverse_functions_demo.py --compile auto
python .\tools\synthesize_section_audio.py `
  --voice-mode builtin `
  --model-name tts_models/en/jenny/jenny `
  --output-dir artifacts\audio\ch01_inverse_functions_jenny `
  --manifest artifacts\audio\ch01_inverse_functions_jenny\manifest.json
python .\tools\render_section_video.py `
  --audio-dir artifacts\audio\ch01_inverse_functions_jenny `
  --output artifacts\video\ch01_inverse_functions_jenny.mp4
```

### Path C: Beamer slides + F5 clone + MP4

```powershell
python .\tools\preprocess_voice_reference.py
python .\tools\generate_inverse_functions_demo.py --compile auto
python .\tools\synthesize_section_audio_f5.py `
  --reference-mode clone `
  --output-dir artifacts\audio\ch01_inverse_functions_f5_clone `
  --manifest artifacts\audio\ch01_inverse_functions_f5_clone\manifest.json
python .\tools\render_section_video.py `
  --audio-dir artifacts\audio\ch01_inverse_functions_f5_clone `
  --output artifacts\video\ch01_inverse_functions_f5_clone.mp4
```

## Current Generated Assets

The repository already contains generated examples for several voice variants:

- `artifacts/audio/ch01_inverse_functions/`
- `artifacts/audio/ch01_inverse_functions_jenny/`
- `artifacts/audio/ch01_inverse_functions_f5_clone/`
- `artifacts/audio/ch01_inverse_functions_f5_example/`
- `artifacts/video/ch01_inverse_functions.mp4`
- `artifacts/video/ch01_inverse_functions_jenny.mp4`
- `artifacts/video/ch01_inverse_functions_f5_clone.mp4`
- `artifacts/video/ch01_inverse_functions_f5_example.mp4`

## Assumptions and Constraints

- The deck-generation script is currently hard-coded to one chapter section.
- The generated deck format is validated against `schemas/slide_deck.schema.json`.
- The video renderer expects one WAV per slide, named as `NN_slide_id.wav`.
- Most scripts rely on repo-local dependencies in `.deps/`.
- F5-TTS relies on additional packages in `.deps_f5/`.
- Model downloads and caches are stored under `.cache/`.

## Troubleshooting

### Beamer PDF is not generated

Check that all of the following are available:
- `latexmk`
- `pdflatex`
- `beamer.cls`

If you only want JSON and `.tex`, run:

```powershell
python .\tools\generate_inverse_functions_demo.py --compile never
```

### XTTS run fails before synthesis

Common causes:
- `--coqui-tos-agreed` was not provided
- the reference WAV is missing
- CUDA was requested but not available

### Final MP4 render fails

Common causes:
- slide PDF missing
- narration WAVs missing or named incorrectly
- slide count in PDF does not match slide count in the deck JSON
- ffmpeg executable could not be resolved through `imageio_ffmpeg`

## Suggested Maintenance Rule

Keep the separation clear:

- `chapters/` is human-authored textbook content
- `tools/` and `schemas/` are pipeline code
- `inputs/` is reusable raw input
- `artifacts/` is generated output

That separation is enough to keep the repository understandable without a larger directory refactor.
