from __future__ import annotations

import argparse
from pathlib import Path

from runtime_bootstrap import REPO_ROOT, bootstrap_repo_deps, ensure_directory, require_path

bootstrap_repo_deps()

import numpy as np
import soundfile as sf


INPUTS_DIR = REPO_ROOT / "inputs" / "voice"
DEFAULT_INPUT = INPUTS_DIR / "my_voice.wav"
LEGACY_INPUT = REPO_ROOT / "my_voice.wav"
DEFAULT_OUTPUT = REPO_ROOT / "artifacts" / "voice" / "reference_30s.wav"


def default_input_path() -> Path:
    if DEFAULT_INPUT.exists():
        return DEFAULT_INPUT
    return LEGACY_INPUT


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Trim and normalize a short reference clip for local voice cloning."
    )
    parser.add_argument("--input", type=Path, default=default_input_path())
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--start-seconds", type=float, default=0.0)
    parser.add_argument("--duration-seconds", type=float, default=30.0)
    parser.add_argument("--mono", action="store_true")
    parser.add_argument("--peak", type=float, default=0.95)
    return parser.parse_args()


def normalize_audio(audio: np.ndarray, peak: float) -> np.ndarray:
    max_value = float(np.max(np.abs(audio))) if audio.size else 0.0
    if max_value == 0.0:
        return audio
    scale = min(peak / max_value, 1.0 / max_value)
    return audio * scale


def main() -> int:
    args = parse_args()
    input_path = require_path(args.input.resolve(), "voice reference input")
    output_path = args.output.resolve()
    ensure_directory(output_path.parent)

    audio, sample_rate = sf.read(str(input_path), always_2d=True)
    start_frame = max(int(args.start_seconds * sample_rate), 0)
    end_frame = start_frame + max(int(args.duration_seconds * sample_rate), 1)
    clipped = audio[start_frame:end_frame]
    if clipped.size == 0:
        raise ValueError("The selected time range produced an empty clip.")

    if args.mono:
        clipped = np.mean(clipped, axis=1, keepdims=True)

    clipped = normalize_audio(clipped, args.peak).astype(np.float32)
    sf.write(str(output_path), clipped, sample_rate)

    duration = clipped.shape[0] / sample_rate
    channels = clipped.shape[1]
    print(
        f"Wrote reference clip to {output_path} "
        f"({duration:.2f}s, {sample_rate} Hz, {channels} channel(s))."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
