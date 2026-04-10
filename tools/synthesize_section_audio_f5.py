from __future__ import annotations

import argparse
import json
import os
from importlib.resources import files
from pathlib import Path

from runtime_bootstrap import (
    F5_DEPS_DIR,
    HF_CACHE_DIR,
    REPO_ROOT,
    bootstrap_repo_deps,
    ensure_directory,
    require_path,
)

bootstrap_repo_deps(F5_DEPS_DIR)

import soundfile as sf
import torch
import yaml
import imageio_ffmpeg
from huggingface_hub import hf_hub_download

from f5_tts.infer.utils_infer import infer_process, load_model, load_vocoder, preprocess_ref_audio_text
from f5_tts.model.backbones.dit import DiT
from f5_tts.model.backbones.mmdit import MMDiT
from f5_tts.model.backbones.unett import UNetT


DEFAULT_DECK = REPO_ROOT / "artifacts" / "slide_spec" / "ch01_inverse_functions.json"
DEFAULT_REFERENCE = REPO_ROOT / "artifacts" / "voice" / "reference_30s.wav"
DEFAULT_OUTPUT_DIR = REPO_ROOT / "artifacts" / "audio" / "ch01_inverse_functions_f5_clone"
DEFAULT_MANIFEST = DEFAULT_OUTPUT_DIR / "manifest.json"
DEFAULT_MODEL = "F5TTS_v1_Base"
DEFAULT_CONFIG = Path(files("f5_tts").joinpath(f"configs/{DEFAULT_MODEL}.yaml"))
DEFAULT_VOCAB = Path(files("f5_tts").joinpath("infer/examples/vocab.txt"))
DEFAULT_EXAMPLE_REFERENCE = Path(files("f5_tts").joinpath("infer/examples/basic/basic_ref_en.wav"))
DEFAULT_EXAMPLE_TEXT = "Some call me nature, others call me mother nature."

BACKBONES = {
    "DiT": DiT,
    "MMDiT": MMDiT,
    "UNetT": UNetT,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Synthesize per-slide narration audio with F5-TTS from the section JSON artifact."
    )
    parser.add_argument("--deck-json", type=Path, default=DEFAULT_DECK)
    parser.add_argument("--reference-mode", choices=("clone", "example"), default="clone")
    parser.add_argument("--reference-wav", type=Path, default=DEFAULT_REFERENCE)
    parser.add_argument("--reference-text", default="")
    parser.add_argument("--output-dir", type=Path, default=DEFAULT_OUTPUT_DIR)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--model-name", default=DEFAULT_MODEL)
    parser.add_argument("--config-path", type=Path, default=DEFAULT_CONFIG)
    parser.add_argument("--vocab-file", type=Path, default=DEFAULT_VOCAB)
    parser.add_argument("--device", choices=("auto", "cpu", "cuda"), default="auto")
    parser.add_argument("--max-slides", type=int)
    parser.add_argument("--nfe-step", type=int, default=32)
    parser.add_argument("--cfg-strength", type=float, default=2.0)
    parser.add_argument("--sway-sampling-coef", type=float, default=-1.0)
    parser.add_argument("--cross-fade-duration", type=float, default=0.15)
    parser.add_argument("--speed", type=float, default=1.0)
    parser.add_argument("--fix-duration", type=float)
    return parser.parse_args()


def resolve_device(requested: str) -> str:
    if requested == "cpu":
        return "cpu"
    if requested == "cuda":
        if not torch.cuda.is_available():
            raise RuntimeError("CUDA was requested but torch.cuda.is_available() is false.")
        return "cuda"
    return "cuda" if torch.cuda.is_available() else "cpu"


def load_deck(path: Path) -> dict:
    with require_path(path.resolve(), "slide deck JSON").open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_model_config(path: Path) -> dict:
    with require_path(path.resolve(), "F5 model config YAML").open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def resolve_model_checkpoint(model_name: str, mel_spec_type: str) -> tuple[str, str]:
    if model_name == "F5TTS_v1_Base":
        return "SWivid/F5-TTS", "F5TTS_v1_Base/model_1250000.safetensors"
    if model_name == "F5TTS_Base":
        filename = "F5TTS_Base/model_1200000.pt"
        if mel_spec_type == "bigvgan":
            filename = "F5TTS_Base_bigvgan/model_1200000.pt"
        return "SWivid/F5-TTS", filename
    if model_name == "E2TTS_Base":
        return "SWivid/E2-TTS", "E2TTS_Base/model_1200000.pt"
    raise ValueError(f"Unsupported F5-TTS model_name: {model_name}")


def build_reference(args: argparse.Namespace) -> tuple[Path, str]:
    if args.reference_mode == "example":
        return require_path(DEFAULT_EXAMPLE_REFERENCE.resolve(), "F5 example reference WAV"), DEFAULT_EXAMPLE_TEXT
    return require_path(args.reference_wav.resolve(), "voice reference WAV"), args.reference_text


def main() -> int:
    args = parse_args()
    ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
    os.environ["IMAGEIO_FFMPEG_EXE"] = ffmpeg_exe
    os.environ["PATH"] = str(Path(ffmpeg_exe).parent) + os.pathsep + os.environ.get("PATH", "")
    deck = load_deck(args.deck_json)
    output_dir = ensure_directory(args.output_dir.resolve())
    manifest_path = args.manifest.resolve()
    ensure_directory(manifest_path.parent)
    model_config = load_model_config(args.config_path)
    vocab_file = require_path(args.vocab_file.resolve(), "F5 vocabulary file")
    reference_wav, reference_text = build_reference(args)
    device = resolve_device(args.device)

    model_settings = model_config["model"]
    backbone_name = model_settings["backbone"]
    if backbone_name not in BACKBONES:
        raise ValueError(f"Unsupported backbone '{backbone_name}'.")
    arch_config = model_settings["arch"]
    mel_spec_type = model_settings["mel_spec"]["mel_spec_type"]

    repo_id, filename = resolve_model_checkpoint(args.model_name, mel_spec_type)
    checkpoint_path = hf_hub_download(repo_id=repo_id, filename=filename, cache_dir=str(HF_CACHE_DIR))

    model_obj = load_model(
        model_cls=BACKBONES[backbone_name],
        model_cfg=arch_config,
        ckpt_path=checkpoint_path,
        mel_spec_type=mel_spec_type,
        vocab_file=str(vocab_file),
        device=device,
    )
    vocoder = load_vocoder(mel_spec_type, is_local=False, local_path="", device=device, hf_cache_dir=str(HF_CACHE_DIR))

    processed_reference_wav, processed_reference_text = preprocess_ref_audio_text(
        str(reference_wav),
        reference_text,
        show_info=print,
    )

    slides = deck["slides"]
    if args.max_slides is not None:
        slides = slides[: args.max_slides]

    manifest = {
        "deck_id": deck["deck_id"],
        "model_name": args.model_name,
        "reference_mode": args.reference_mode,
        "reference_wav": str(reference_wav),
        "reference_text": processed_reference_text,
        "device": device,
        "nfe_step": args.nfe_step,
        "cfg_strength": args.cfg_strength,
        "sway_sampling_coef": args.sway_sampling_coef,
        "cross_fade_duration": args.cross_fade_duration,
        "speed": args.speed,
        "slides": [],
    }

    for slide in slides:
        slide_number = int(slide["slide_number"])
        slide_id = slide["slide_id"]
        output_wav = output_dir / f"{slide_number:02d}_{slide_id}.wav"
        script = slide["script"].strip()
        if not script:
            raise ValueError(f"Slide {slide_number} has an empty script.")

        audio, sample_rate, _ = infer_process(
            ref_audio=processed_reference_wav,
            ref_text=processed_reference_text,
            gen_text=script,
            model_obj=model_obj,
            vocoder=vocoder,
            mel_spec_type=mel_spec_type,
            show_info=print,
            progress=None,
            nfe_step=args.nfe_step,
            cfg_strength=args.cfg_strength,
            sway_sampling_coef=args.sway_sampling_coef,
            cross_fade_duration=args.cross_fade_duration,
            speed=args.speed,
            fix_duration=args.fix_duration,
            device=device,
        )
        if audio is None:
            raise RuntimeError(f"F5-TTS returned no audio for slide {slide_number}.")

        sf.write(str(output_wav), audio, sample_rate)
        manifest["slides"].append(
            {
                "slide_number": slide_number,
                "slide_id": slide_id,
                "audio_file": str(output_wav),
                "script": script,
                "audio_seconds": round(len(audio) / sample_rate, 3),
            }
        )
        print(f"Synthesized slide {slide_number}: {output_wav.name}")
        if device == "cuda":
            torch.cuda.empty_cache()

    manifest_path.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote synthesis manifest to {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
