"""Voiceover for each scene, with per-word timings for karaoke captions.

Primary engine: Microsoft Edge neural voices via the free `edge-tts` package
(natural voices, English and Khmer). Fallback: espeak-ng (robotic, offline),
used only when Edge is unreachable, e.g. inside a locked-down sandbox.
"""
import asyncio
import json
import shutil
import subprocess
from pathlib import Path

VOICES = {
    "en": {"you": "en-US-AndrewNeural", "host": "en-US-AvaNeural"},
    "km": {"you": "km-KH-PisethNeural", "host": "km-KH-SreymomNeural"},
}
ESPEAK = {"you": ("en-us+m3", 175), "host": ("en-us+f3", 165)}


def _duration(path: Path) -> float:
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
        capture_output=True, text=True, check=True,
    )
    return float(out.stdout.strip())


def _even_words(text: str, dur: float, lead: float = 0.05):
    """Spread words across the clip by character length (used when no word timings)."""
    words = text.split()
    total = sum(len(w) + 1 for w in words) or 1
    t, out = lead, []
    span = max(dur - lead - 0.1, 0.1)
    for w in words:
        d = span * (len(w) + 1) / total
        out.append({"word": w, "start": round(t, 3), "end": round(t + d, 3)})
        t += d
    return out


async def _edge(text: str, voice: str, mp3: Path):
    import edge_tts

    try:
        comm = edge_tts.Communicate(text, voice, rate="+8%", boundary="WordBoundary")
    except TypeError:  # older edge-tts without the boundary option
        comm = edge_tts.Communicate(text, voice, rate="+8%")
    words = []
    with open(mp3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                s = chunk["offset"] / 1e7
                words.append({"word": chunk["text"], "start": round(s, 3),
                              "end": round(s + chunk["duration"] / 1e7, 3)})
    return words


def synth(text: str, speaker: str, lang: str, out_base: Path, engine: str = "auto"):
    """Write out_base.wav and return (wav_path, duration_s, words)."""
    wav = out_base.with_suffix(".wav")
    words = None
    if engine in ("auto", "edge"):
        try:
            mp3 = out_base.with_suffix(".mp3")
            words = asyncio.run(_edge(text, VOICES[lang][speaker], mp3))
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(mp3), "-ar", "44100", "-ac", "1", str(wav)], check=True)
        except Exception as e:  # network blocked, voice missing, etc.
            if engine == "edge":
                raise
            print(f"  edge-tts unavailable ({type(e).__name__}); falling back to espeak-ng")
            words = None
    if words is None:
        if not shutil.which("espeak-ng"):
            raise SystemExit("No TTS engine: install edge-tts (needs internet) or espeak-ng.")
        v, rate = ESPEAK[speaker]
        subprocess.run(["espeak-ng", "-v", v, "-s", str(rate), "-w", str(wav), text], check=True)
        words = []
    dur = _duration(wav)
    if lang == "km":  # Khmer has no spaces; captions use the English subtitle instead
        words = []
    elif not words:  # espeak gives no timings: estimate them from word length
        words = _even_words(text, dur)
    return wav, dur, words


if __name__ == "__main__":
    import sys
    w, d, ws = synth(sys.argv[1], "host", "en", Path("/tmp/tts_test"))
    print(w, d, json.dumps(ws)[:300])
