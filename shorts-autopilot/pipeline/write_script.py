"""Ask Claude to write one short-form video script from a topic brief.

Usage:
    python pipeline/write_script.py topics/my-topic.yml out/my-topic/script.json

The topic brief is a small YAML file (see topics/EXAMPLE.yml). Only facts in
the brief may appear as claims in the video; everything else must be listed
in claims_to_verify so a human checks it before posting.
"""
import json
import sys
from pathlib import Path

import anthropic
import yaml

sys.path.insert(0, str(Path(__file__).parent))
from schema import VideoScript  # noqa: E402

MODEL = "claude-opus-5-5"

SYSTEM = """You write 55-75 second vertical videos (TikTok / Reels / Shorts) for a faceless
tech channel. The format is a dialogue between two animated characters:

- "you": the viewer stand-in. Has a relatable problem, is impatient, skeptical, funny.
- "host": the AI mascot. Calm, dry, a little savage. Explains a free tool in steps.

Structure (follow it, it is what makes this format retain viewers):
1. HOOK (0-6s): "you" states a painful, specific problem with a number in it.
   The host answers with one short, cheeky line. hook_title is the problem in
   ~6 words (e.g. "6-Hour Stream, 11 Views"); hook_highlight is its punchy end.
2. REVEAL (6-20s): the host names the free tool. Show a "github" card
   (title = owner/repo, subtitle = what it does), then "badges" (Free, open
   source, license) only if the brief confirms them.
3. "What's the catch?" beat from "you".
4. STEPS (20-50s): "No catch. Three steps." Each step is its own scene with a
   "terminal" card (real commands from the brief only) or "bullets" card with
   the active step highlighted. Keep every line under 14 words.
5. PAYOFF / TWIST (50-65s): a short funny moment that shows the result
   (a "number" card works well). Never invent statistics: if you show a number
   it is clearly part of the joke story, or it comes from the brief.
6. CTA (last scene): host says "Comment <KEYWORD> and I'll send you the link."
   Use a "cta" card with title = KEYWORD.

Rules:
- Lines are spoken aloud: short, plain words, contractions, no emoji, no hashtags,
  no em dashes. 14-22 scenes total.
- Only state facts that appear in the brief. Put any other factual-sounding claim
  (earnings, user counts, star counts, prices) in claims_to_verify, or leave it out.
- Never claim income or earnings for anyone.
- Never mention real people, creators, or companies as clients or endorsers.
- sources = the URLs from the brief.
- post_caption: 2-4 short lines, first line is the hook, end with the comment CTA.
- hashtags: 5-8, lowercase, without the # sign.
- If the brief says language is "km", write `line` in natural spoken Khmer and put the
  English translation in `subtitle`. Otherwise write English `line` and leave subtitle empty.
"""


def write_script(brief: dict) -> VideoScript:
    client = anthropic.Anthropic()
    user = "Topic brief (YAML):\n\n" + yaml.safe_dump(brief, allow_unicode=True, sort_keys=False)
    response = client.messages.parse(
        model=MODEL,
        max_tokens=16000,
        output_config={"effort": "high"},
        system=SYSTEM,
        messages=[{"role": "user", "content": user}],
        output_format=VideoScript,
    )
    if response.stop_reason == "refusal":
        raise SystemExit(f"Claude declined this topic: {response.stop_details}")
    return response.parsed_output


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    brief = yaml.safe_load(Path(sys.argv[1]).read_text())
    script = write_script(brief)
    out = Path(sys.argv[2])
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(script.model_dump(), indent=2, ensure_ascii=False))
    print(f"wrote {out} ({len(script.scenes)} scenes)")


if __name__ == "__main__":
    main()
