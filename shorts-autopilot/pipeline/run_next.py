"""Daily job: pick the next topic brief, write the script with Claude, render it.

    python pipeline/run_next.py [--lang en|km]

Skips topics/EXAMPLE.yml. Output goes to out/<topic-file-name>/ and the brief
is moved to topics/done/ so tomorrow's run picks the next one.
"""
import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "pipeline"))
from write_script import write_script  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default=None)
    a = ap.parse_args()
    todo = sorted(p for p in (ROOT / "topics").glob("*.yml") if p.stem != "EXAMPLE")
    if not todo:
        print("No new topics in topics/. Add a brief and run again.")
        return
    topic = todo[0]
    brief = yaml.safe_load(topic.read_text())
    lang = a.lang or brief.get("language", "en")
    out = ROOT / "out" / topic.stem
    out.mkdir(parents=True, exist_ok=True)
    print(f"topic: {topic.name} ({lang})")
    script = write_script(brief)
    (out / "script.json").write_text(json.dumps(script.model_dump(), indent=2, ensure_ascii=False))
    subprocess.run([sys.executable, str(ROOT / "pipeline" / "make_video.py"), str(out / "script.json"), "--lang", lang], check=True)
    (ROOT / "topics" / "done").mkdir(exist_ok=True)
    topic.rename(ROOT / "topics" / "done" / topic.name)
    print(f"READY_DIR={out}")


if __name__ == "__main__":
    main()
