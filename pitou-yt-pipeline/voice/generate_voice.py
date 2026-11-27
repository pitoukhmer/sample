#!/usr/bin/env python3
"""The Small Shop AI: narrator voice station (VoxCPM 2).

Three commands:

  design   One-time. Generate candidate master-voice takes with VoxCPM 2
           Voice Design: "(<voice prompt>)<reference script>".
  lock     One-time. Copy the chosen take to voice/narrator_ref.wav and
           write its exact transcript to voice/narrator_ref.txt.
  render   Every episode. Clone the locked narrator and render a script
           (episodes/epXX/script.md) to voice.wav + timings.json.

Examples:
  python voice/generate_voice.py design --version A --takes 3
  python voice/generate_voice.py design --version B --takes 3
  python voice/generate_voice.py lock --take voice/takes/A_take2.wav
  python voice/generate_voice.py render episodes/ep01/script.md
  python voice/generate_voice.py render episodes/ep01/script.md --mode hifi
  python voice/generate_voice.py render episodes/ep01/script.md --dry-run

Script format read by `render` (the Episode Script doc exports to this):
  - Lines starting with "#" are section headings (logged in timings).
  - [PAUSE] inserts 1.0 s of silence.
  - [STYLE: calm, clear pace] sets a VoxCPM style tag for the following
    paragraphs (Controllable mode only). [STYLE: none] clears it.
  - Any other [BRACKET] line, "> " quote lines, list lines ("1. ", "- "),
    table lines ("|"), code fences and *italic notes* are production cues
    and are NOT spoken.
  - Every other non-empty line is one spoken paragraph.

Requires: pip install voxcpm soundfile numpy   (a CUDA GPU is strongly advised)
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

import numpy as np

MODEL_ID = "openbmb/VoxCPM2"
VOICE_DIR = Path(__file__).resolve().parent
REF_WAV = VOICE_DIR / "narrator_ref.wav"
REF_TXT = VOICE_DIR / "narrator_ref.txt"
TAKES_DIR = VOICE_DIR / "takes"

TARGET_SR = 48_000
CFG_VALUE = 2.0
INFERENCE_TIMESTEPS = 10
PAUSE_SECONDS = 1.0
PARAGRAPH_GAP_SECONDS = 0.35
MAX_REF_SECONDS = 15.0

# Master voice prompts (see SOP, "Master narrator voice").
VOICE_PROMPTS = {
    "A": (
        "An adult male narrator in his mid-30s with a warm, clear, authoritative voice. "
        "Medium-low pitch, smooth and steady. Calm, confident pace of about 150 words per minute, "
        "with natural pauses between sentences. Friendly expert tone, like a trusted teacher "
        "explaining something useful to a busy shop owner. Neutral international English accent, "
        "crisp consonants. No vocal fry, no exaggerated excitement, no sales-pitch energy. "
        "Clean studio recording, close microphone, no background noise or reverb."
    ),
    "B": (
        "An adult female narrator in her mid-30s with a warm, clear, authoritative voice. "
        "Medium pitch, smooth and steady. Calm, confident pace of about 150 words per minute, "
        "with natural pauses between sentences. Friendly expert tone, like a trusted teacher "
        "explaining something useful to a busy shop owner. Neutral international English accent, "
        "crisp consonants. No vocal fry, no exaggerated excitement, no sales-pitch energy. "
        "Clean studio recording, close microphone, no background noise or reverb."
    ),
}

REF_TEXT = (
    "Welcome to The Small Shop AI. Every week, we take one task from a small business "
    "and hand it to AI, step by step. Can it answer customers at midnight? "
    "Write fifty product descriptions? Let's find out, and keep what works."
)

# Spoken-form fixes applied to narration before synthesis.
# Add an entry if the pronunciation check fails (for example "Pitou": "Pee-too").
PRONUNCIATIONS = {
    "24/7": "twenty-four seven",
}


# --------------------------------------------------------------------------- #
# Model helpers
# --------------------------------------------------------------------------- #
def load_model():
    try:
        from voxcpm import VoxCPM
    except ImportError:
        sys.exit("voxcpm is not installed. Run: pip install voxcpm soundfile")
    # Reference clip is already clean studio audio, so the denoiser stays off.
    model = VoxCPM.from_pretrained(MODEL_ID, load_denoiser=False)
    sr = int(model.tts_model.sample_rate)
    if sr != TARGET_SR:
        print(f"WARNING: model outputs {sr} Hz, expected {TARGET_SR} Hz. Files are written at {sr} Hz.")
    return model, sr


def seed_everything(seed: int) -> None:
    import random

    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
    except ImportError:
        pass


def write_wav(path: Path, audio: np.ndarray, sr: int) -> None:
    import soundfile as sf

    path.parent.mkdir(parents=True, exist_ok=True)
    sf.write(str(path), audio.astype(np.float32), sr, subtype="PCM_24")


def spoken(text: str) -> str:
    for written, said in PRONUNCIATIONS.items():
        text = re.sub(rf"(?<![\w/]){re.escape(written)}(?![\w/])", said, text)
    return text


# --------------------------------------------------------------------------- #
# design / lock
# --------------------------------------------------------------------------- #
def cmd_design(args) -> None:
    prompt = VOICE_PROMPTS[args.version]
    model, sr = load_model()
    TAKES_DIR.mkdir(parents=True, exist_ok=True)
    # Voice Design mode: the description goes in parentheses right before the text.
    text = f"({prompt}){REF_TEXT}"
    for i in range(1, args.takes + 1):
        seed = args.seed + i
        seed_everything(seed)
        wav = model.generate(
            text=text,
            cfg_value=CFG_VALUE,
            inference_timesteps=INFERENCE_TIMESTEPS,
            retry_badcase=True,
        )
        out = TAKES_DIR / f"{args.version}_take{i}.wav"
        write_wav(out, wav, sr)
        secs = len(wav) / sr
        flag = "  <-- over 15 s, cut 'step by step' and re-run" if secs > MAX_REF_SECONDS else ""
        print(f"{out}  {secs:.1f}s  seed={seed}{flag}")
    print("Listen to every take, pick one, then run: lock --take <file>")


def cmd_lock(args) -> None:
    import soundfile as sf

    take = Path(args.take)
    if not take.exists():
        sys.exit(f"Take not found: {take}")
    info = sf.info(str(take))
    if info.duration > MAX_REF_SECONDS:
        sys.exit(f"Take is {info.duration:.1f}s. The reference must be {MAX_REF_SECONDS:.0f}s or less. "
                 "Regenerate with a shorter ref text; do not trim the audio.")
    if REF_WAV.exists() and not args.force:
        sys.exit(f"{REF_WAV} already exists. The narrator is locked. Use --force only on founder approval.")
    shutil.copyfile(take, REF_WAV)
    REF_TXT.write_text(REF_TEXT + "\n", encoding="utf-8")
    print(f"Locked {take} -> {REF_WAV} ({info.samplerate} Hz, {info.duration:.1f}s)")
    print(f"Transcript -> {REF_TXT}")


# --------------------------------------------------------------------------- #
# render
# --------------------------------------------------------------------------- #
CUE_SKIP = re.compile(r"^(>|\||```|\d+\.\s|[-*]\s|\*[^*].*\*$|_.*_$)")


def parse_script(path: Path) -> list[dict]:
    """Turn an episode script into an ordered list of speak / pause / section items."""
    items: list[dict] = []
    style = ""
    in_fence = False
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or not line:
            continue
        if line.startswith("#"):
            items.append({"type": "section", "title": line.lstrip("#").strip()})
            continue
        if line.upper() == "[PAUSE]":
            items.append({"type": "pause", "seconds": PAUSE_SECONDS})
            continue
        m = re.match(r"^\[STYLE:\s*(.*?)\]$", line, re.IGNORECASE)
        if m:
            style = "" if m.group(1).lower() in ("", "none") else m.group(1)
            continue
        if line.startswith("[") or CUE_SKIP.match(line):
            continue  # production cue, not narration
        text = re.sub(r"\*\*(.+?)\*\*|\*(.+?)\*|`(.+?)`", lambda g: next(x for x in g.groups() if x), line)
        items.append({"type": "speak", "text": text, "style": style})
    return items


def cmd_render(args) -> None:
    script = Path(args.script)
    if not script.exists():
        sys.exit(f"Script not found: {script}")
    items = parse_script(script)
    speak_items = [it for it in items if it["type"] == "speak"]
    words = sum(len(it["text"].split()) for it in speak_items)
    print(f"{len(speak_items)} paragraphs, {words} words, ~{words / 150:.1f} min at 150 wpm")

    if args.dry_run:
        for it in items:
            if it["type"] == "section":
                print(f"\n== {it['title']}")
            elif it["type"] == "pause":
                print("   [pause 1.0s]")
            else:
                tag = f"({it['style']}) " if it["style"] else ""
                print(f"   {tag}{spoken(it['text'])}")
        return

    unfilled = sorted({m for it in speak_items for m in re.findall(r"\{[A-Z_]+\}", it["text"])})
    if unfilled:
        sys.exit(f"Fill these placeholders in the script before rendering: {', '.join(unfilled)}")

    if not REF_WAV.exists() or not REF_TXT.exists():
        sys.exit("No locked narrator. Run design, then lock, first.")
    ref_text = REF_TXT.read_text(encoding="utf-8").strip()

    if args.mode == "hifi" and any(it["style"] for it in speak_items):
        print("NOTE: hifi mode ignores [STYLE] tags (VoxCPM does not combine style control with prompt_text).")

    model, sr = load_model()
    seed_everything(args.seed)
    gap = np.zeros(int(PARAGRAPH_GAP_SECONDS * sr), dtype=np.float32)
    chunks: list[np.ndarray] = []
    timings: list[dict] = []
    cursor = 0.0
    section = ""

    for it in items:
        if it["type"] == "section":
            section = it["title"]
            continue
        if it["type"] == "pause":
            n = int(it["seconds"] * sr)
            chunks.append(np.zeros(n, dtype=np.float32))
            cursor += n / sr
            continue

        text = spoken(it["text"])
        kwargs = dict(
            cfg_value=CFG_VALUE,
            inference_timesteps=INFERENCE_TIMESTEPS,
            retry_badcase=True,
            reference_wav_path=str(REF_WAV),
        )
        if args.mode == "hifi":
            # Hi-Fi Ultimate Cloning: continuation prompt + reference timbre.
            kwargs.update(prompt_wav_path=str(REF_WAV), prompt_text=ref_text)
        elif it["style"]:
            # Controllable Cloning: style tag in parentheses before the text.
            text = f"({it['style']}){text}"

        wav = np.asarray(model.generate(text=text, **kwargs), dtype=np.float32)
        start = cursor
        chunks.extend([wav, gap])
        cursor += (len(wav) + len(gap)) / sr
        timings.append({"section": section, "start": round(start, 3),
                        "end": round(start + len(wav) / sr, 3), "text": it["text"]})
        print(f"[{start:7.2f}s] {it['text'][:70]}")

    out_dir = Path(args.out) if args.out else script.parent
    audio = np.concatenate(chunks) if chunks else np.zeros(1, dtype=np.float32)
    peak = float(np.max(np.abs(audio))) or 1.0
    audio = audio / peak * 0.89  # about -1 dBFS peak
    write_wav(out_dir / "voice.wav", audio, sr)
    (out_dir / "timings.json").write_text(json.dumps(timings, indent=2), encoding="utf-8")
    print(f"\nWrote {out_dir / 'voice.wav'} ({len(audio) / sr / 60:.1f} min, {sr} Hz) and timings.json")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("design", help="generate master-voice candidate takes")
    d.add_argument("--version", choices=sorted(VOICE_PROMPTS), default="A")
    d.add_argument("--takes", type=int, default=3)
    d.add_argument("--seed", type=int, default=1000)
    d.set_defaults(func=cmd_design)

    lk = sub.add_parser("lock", help="lock a take as the narrator reference")
    lk.add_argument("--take", required=True)
    lk.add_argument("--force", action="store_true")
    lk.set_defaults(func=cmd_lock)

    r = sub.add_parser("render", help="render an episode script with the locked narrator")
    r.add_argument("script")
    r.add_argument("--mode", choices=["controllable", "hifi"], default="controllable")
    r.add_argument("--seed", type=int, default=7)
    r.add_argument("--out", help="output folder (default: the script's folder)")
    r.add_argument("--dry-run", action="store_true", help="print what will be spoken, no model needed")
    r.set_defaults(func=cmd_render)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
