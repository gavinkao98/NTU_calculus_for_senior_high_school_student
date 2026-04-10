from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from runtime_bootstrap import REPO_ROOT, bootstrap_repo_deps, ensure_directory, require_path

bootstrap_repo_deps()

import fitz
import imageio_ffmpeg
import soundfile as sf


DEFAULT_DECK = REPO_ROOT / "artifacts" / "slide_spec" / "ch01_inverse_functions.json"
DEFAULT_PDF = REPO_ROOT / "artifacts" / "slides" / "ch01_inverse_functions.pdf"
DEFAULT_AUDIO_DIR = REPO_ROOT / "artifacts" / "audio" / "ch01_inverse_functions"
DEFAULT_OUTPUT = REPO_ROOT / "artifacts" / "video" / "ch01_inverse_functions.mp4"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a static-slide MP4 from the section PDF and per-slide narration WAV files."
    )
    parser.add_argument("--deck-json", type=Path, default=DEFAULT_DECK)
    parser.add_argument("--slides-pdf", type=Path, default=DEFAULT_PDF)
    parser.add_argument("--audio-dir", type=Path, default=DEFAULT_AUDIO_DIR)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dpi-scale", type=float, default=4.0)
    parser.add_argument("--lead-in-seconds", type=float, default=1.0)
    parser.add_argument("--target-width", type=int, default=1920)
    parser.add_argument("--target-height", type=int, default=1080)
    parser.add_argument("--crf", type=int, default=18)
    return parser.parse_args()


def load_deck(path: Path) -> dict:
    with require_path(path.resolve(), "slide deck JSON").open("r", encoding="utf-8") as handle:
        return json.load(handle)


def render_slide_images(pdf_path: Path, image_dir: Path, page_count: int, dpi_scale: float) -> list[Path]:
    ensure_directory(image_dir)
    images: list[Path] = []
    document = fitz.open(str(require_path(pdf_path.resolve(), "slide deck PDF")))
    if document.page_count != page_count:
        raise ValueError(
            f"PDF page count ({document.page_count}) does not match slide count ({page_count})."
        )

    matrix = fitz.Matrix(dpi_scale, dpi_scale)
    for page_number in range(document.page_count):
        page = document.load_page(page_number)
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        image_path = image_dir / f"slide_{page_number + 1:02d}.png"
        pixmap.save(str(image_path))
        images.append(image_path)
    document.close()
    return images


def audio_duration(path: Path) -> float:
    info = sf.info(str(require_path(path.resolve(), "slide audio")))
    return info.frames / info.samplerate


def run_ffmpeg(command: list[str]) -> None:
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise RuntimeError(
            "ffmpeg command failed.\n"
            f"Command: {' '.join(command)}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )


def build_video(
    deck: dict,
    pdf_path: Path,
    audio_dir: Path,
    output_path: Path,
    dpi_scale: float,
    lead_in_seconds: float,
    target_width: int,
    target_height: int,
    crf: int,
) -> None:
    if lead_in_seconds < 0:
        raise ValueError(f"lead_in_seconds must be non-negative, got {lead_in_seconds}.")
    if target_width <= 0 or target_height <= 0:
        raise ValueError(f"target dimensions must be positive, got {target_width}x{target_height}.")

    output_path = output_path.resolve()
    work_dir = ensure_directory(output_path.parent / output_path.stem)
    image_dir = ensure_directory(work_dir / "frames")
    segment_dir = ensure_directory(work_dir / "segments")
    images = render_slide_images(pdf_path, image_dir, len(deck["slides"]), dpi_scale)

    ffmpeg_path = Path(imageio_ffmpeg.get_ffmpeg_exe()).resolve()
    concat_file = work_dir / "segments.txt"
    concat_lines: list[str] = []

    for slide, image_path in zip(deck["slides"], images):
        slide_number = int(slide["slide_number"])
        slide_id = slide["slide_id"]
        wav_path = require_path(
            (audio_dir / f"{slide_number:02d}_{slide_id}.wav").resolve(),
            f"audio for slide {slide_number}",
        )
        duration = audio_duration(wav_path)
        total_duration = duration + lead_in_seconds
        segment_path = segment_dir / f"{slide_number:02d}_{slide_id}.mp4"

        command = [
            str(ffmpeg_path),
            "-y",
            "-loop",
            "1",
            "-framerate",
            "1",
            "-i",
            str(image_path),
            "-i",
            str(wav_path),
            "-c:v",
            "libx264",
            "-preset",
            "slow",
            "-tune",
            "stillimage",
            "-vf",
            (
                f"scale={target_width}:{target_height}:force_original_aspect_ratio=decrease,"
                f"pad={target_width}:{target_height}:(ow-iw)/2:(oh-ih)/2:color=white"
            ),
            "-af",
            f"adelay={int(round(lead_in_seconds * 1000))}:all=1",
            "-crf",
            str(crf),
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-ar",
            "48000",
            "-t",
            f"{total_duration:.3f}",
            "-shortest",
            str(segment_path),
        ]
        run_ffmpeg(command)
        concat_lines.append(f"file '{segment_path.as_posix()}'")
        print(f"Rendered video segment for slide {slide_number}")

    concat_file.write_text("\n".join(concat_lines) + "\n", encoding="utf-8")

    final_command = [
        str(ffmpeg_path),
        "-y",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        str(concat_file),
        "-c",
        "copy",
        str(output_path),
    ]
    run_ffmpeg(final_command)
    print(f"Wrote final video to {output_path}")


def main() -> int:
    args = parse_args()
    deck = load_deck(args.deck_json)
    build_video(
        deck=deck,
        pdf_path=args.slides_pdf,
        audio_dir=args.audio_dir.resolve(),
        output_path=args.output,
        dpi_scale=args.dpi_scale,
        lead_in_seconds=args.lead_in_seconds,
        target_width=args.target_width,
        target_height=args.target_height,
        crf=args.crf,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
