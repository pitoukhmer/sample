"""Render a script.json into a finished 1080x1920 MP4 with voiceover and captions.

Usage:
    python pipeline/make_video.py out/<slug>/script.json [--lang en|km] [--tts auto|edge|espeak]

Writes next to the script:
    video.mp4      the short, ready to upload
    caption.txt    post caption + hashtags
    REVIEW.md      what to check before you press post
"""
import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from schema import VideoScript  # noqa: E402
from tts import synth  # noqa: E402

HERE = Path(__file__).parent
HOST_NAME = os.environ.get("HOST_NAME", "PITOU")
GAP = 0.18          # silence after each line (s)
FLAP = 0.13         # mouth open/close interval while talking (s)
FPS = 30


def run(cmd):
    subprocess.run(cmd, check=True)


def render_frames(script: VideoScript, work: Path):
    """Two PNGs per scene (mouth closed / open) via headless Chromium."""
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        exe = os.environ.get("CHROMIUM_PATH")
        browser = p.chromium.launch(executable_path=exe) if exe else p.chromium.launch()
        page = browser.new_page(viewport={"width": 1080, "height": 1920})
        page.goto((HERE / "scene.html").as_uri())
        page.wait_for_timeout(800)
        for i, sc in enumerate(script.scenes):
            for mouth in (0, 1):
                data = {**sc.model_dump(), "hook_title": script.hook_title,
                        "hook_highlight": script.hook_highlight, "host_name": HOST_NAME, "mouth": mouth}
                page.evaluate("s => setScene(s)", data)
                page.screenshot(path=str(work / f"s{i:02d}_{mouth}.png"))
        browser.close()


def ass_time(t: float) -> str:
    h, rem = divmod(max(t, 0), 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


ASS_HEAD = """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Poppins,62,&H00FFFFFF,&H00FFFFFF,&H00101010,&H99000000,1,0,0,0,100,100,0,0,1,6,2,8,90,90,1190,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def chunks(words, n=4):
    for i in range(0, len(words), n):
        yield words[i:i + n]


def build_ass(timeline) -> str:
    """Karaoke-style captions: 3-4 words on screen, the spoken word in yellow."""
    lines = [ASS_HEAD]
    for t0, dur, sc, words in timeline:
        if not words:  # no word timings (espeak / Khmer): show the subtitle text in groups
            text = (sc.subtitle or sc.line).split()
            groups = list(chunks(text, 5))
            step = dur / max(len(groups), 1)
            for k, g in enumerate(groups):
                lines.append(f"Dialogue: 0,{ass_time(t0 + k * step)},{ass_time(t0 + (k + 1) * step)},Cap,,0,0,0,,{' '.join(g)}")
            continue
        for g in chunks(words, 4):
            g_end = g[-1]["end"]
            for k, w in enumerate(g):
                start = t0 + w["start"]
                end = t0 + (g[k + 1]["start"] if k + 1 < len(g) else g_end + 0.12)
                txt = " ".join(("{\\c&H3FD2FF&}" + x["word"] + "{\\c&HFFFFFF&}") if j == k else x["word"]
                               for j, x in enumerate(g))
                lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Cap,,0,0,0,,{txt}")
    return "\n".join(lines) + "\n"


def mouth_sequence(i, dur, words, work: Path):
    """Concat-demuxer entries that flap the mouth while words are being spoken."""
    spans = [(w["start"], w["end"]) for w in words] or [(0.05, dur - 0.1)]
    entries, t, open_ = [], 0.0, 0
    while t < dur + GAP - 1e-6:
        step = min(FLAP, dur + GAP - t)
        talking = any(a <= t < b + 0.05 for a, b in spans)
        open_ = (1 - open_) if talking else 0
        entries.append((work / f"s{i:02d}_{open_}.png", step))
        t += step
    return entries


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--lang", default="en", choices=["en", "km"])
    ap.add_argument("--tts", default="auto", choices=["auto", "edge", "espeak"])
    a = ap.parse_args()

    script_path = Path(a.script)
    script = VideoScript.model_validate_json(script_path.read_text())
    out = script_path.parent
    work = out / "_work"
    work.mkdir(parents=True, exist_ok=True)

    print("1/4 voiceover")
    timeline, t, concat, audio_list = [], 0.0, [], []
    for i, sc in enumerate(script.scenes):
        wav, dur, words = synth(sc.line, sc.speaker, a.lang, work / f"a{i:02d}", engine=a.tts)
        padded = work / f"p{i:02d}.wav"
        run(["ffmpeg", "-v", "error", "-y", "-i", str(wav), "-af", f"apad=pad_dur={GAP}", "-ar", "44100", "-ac", "1", str(padded)])
        timeline.append((t, dur, sc, words))
        audio_list.append(padded)
        t += dur + GAP

    print("2/4 frames")
    render_frames(script, work)
    for i, (_, dur, _, words) in enumerate(timeline):
        concat += mouth_sequence(i, dur, words, work)

    print("3/4 captions")
    (work / "captions.ass").write_text(build_ass(timeline), encoding="utf-8")
    with open(work / "frames.txt", "w") as f:
        for path, d in concat:
            f.write(f"file '{path.resolve()}'\nduration {d:.3f}\n")
        f.write(f"file '{concat[-1][0].resolve()}'\n")
    with open(work / "audio.txt", "w") as f:
        for p in audio_list:
            f.write(f"file '{p.resolve()}'\n")
    run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(work / "audio.txt"), str(work / "voice.wav")])

    print("4/4 encode")
    video = out / "video.mp4"
    run(["ffmpeg", "-v", "error", "-y",
         "-f", "concat", "-safe", "0", "-i", str(work / "frames.txt"),
         "-i", str(work / "voice.wav"),
         "-vf", f"fps={FPS},format=yuv420p,subtitles={work / 'captions.ass'}",
         "-c:v", "libx264", "-preset", "medium", "-crf", "20",
         "-c:a", "aac", "-b:a", "160k", "-shortest", "-movflags", "+faststart", str(video)])

    tags = " ".join("#" + h.lstrip("#") for h in script.hashtags)
    (out / "caption.txt").write_text(f"{script.post_caption}\n\n{tags}\n", encoding="utf-8")
    review = ["# Review before posting", "", f"Video: `video.mp4` ({t:.0f}s)", "",
              "## Check these claims", *[f"- [ ] {c}" for c in script.claims_to_verify or ["(none flagged)"]],
              "", "## Sources", *[f"- {s}" for s in script.sources],
              "", "## Checklist",
              "- [ ] Watched it once with sound, captions match the voice",
              "- [ ] Every command / repo name on screen is correct",
              "- [ ] No earnings claims, no client names without permission",
              f"- [ ] Comment keyword `{script.cta_keyword}` is set up in your DM auto-reply"]
    (out / "REVIEW.md").write_text("\n".join(review) + "\n", encoding="utf-8")
    print(f"done: {video} ({t:.1f}s)")


if __name__ == "__main__":
    main()
