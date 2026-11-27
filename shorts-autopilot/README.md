# Shorts Autopilot

Every morning a GitHub Action takes the next idea from `topics/`, has Claude write a 60-second "you vs. the AI mascot" script in the same format as the reference videos (breakdown in `VIDEO_BREAKDOWN.md`), and renders it to a 1080x1920 MP4 with voiceover and word-highlighted captions. It then opens a GitHub issue with the download link, the post caption and a fact-check list. Your part is to watch it, tick the boxes and post it.

A sample render made in this repo is in `samples/podcast-clipper/video.mp4`. It uses the offline robot voice because the build sandbox has no internet. The daily job uses natural Microsoft neural voices.

## One-time setup (about 15 minutes)

1. Get an Anthropic API key at console.anthropic.com, then go to this repo on GitHub and open Settings → Secrets and variables → Actions → New repository secret. Name it `ANTHROPIC_API_KEY`. One script costs a few cents.
2. Copy `topics/EXAMPLE.yml` to a new file such as `topics/001-clip-generator.yml` and edit it. Put only facts you copied from the tool's README under `facts:`, because the script is not allowed to claim anything else. Add 5 to 10 topics so the queue never runs dry.
3. Go to the Actions tab, open "Daily short (shorts-autopilot)" and click Run workflow to test it. After that it runs every day at 08:17 Phnom Penh time.
4. Set up the comment-to-DM reply on each platform (ManyChat for Instagram and TikTok) so the keyword in the video (for example CLIPS) sends the link automatically.

## Your daily routine (about 3 minutes)

When the "Review short: …" issue arrives, open the run link and download the artifact (video.mp4, caption.txt, REVIEW.md). Watch the video once with sound. Check every item in REVIEW.md, especially anything under "Check these claims". If it's good, post the video on TikTok, Reels and Shorts with the caption from caption.txt, add a trending sound at low volume in the app, and close the issue. If it's bad, close the issue with a comment and fix the topic brief.

## Language

English is the default. Khmer works too: set `language: km` in a topic brief, or choose `km` when you run the workflow by hand. Claude then writes the dialogue in spoken Khmer, the voices switch to the Khmer neural voices (Piseth and Sreymom), and the captions show the English translation. Claude's Khmer is good but not native-perfect, so have a Khmer speaker check the first few before you post.

## Running it locally

```bash
cd shorts-autopilot
pip install -r requirements.txt && python -m playwright install chromium   # plus ffmpeg on your system
export ANTHROPIC_API_KEY=...
python pipeline/run_next.py                     # next topic: write + render
python pipeline/make_video.py samples/podcast-clipper/script.json   # re-render an existing script
```

You can also skip the API and ask Claude Code in chat to "write a script.json for topic X", then run `make_video.py` on it.

## How it works

`pipeline/write_script.py` sends the topic brief to Claude (`claude-opus-5-5`, structured output) with the format rules: hook with a number, the GitHub reveal, the "what's the catch" beat, three steps, a twist, and a comment CTA. The output follows `pipeline/schema.py`. Claude has to list anything unverified under `claims_to_verify` and is told never to make earnings claims or name clients.

`pipeline/tts.py` voices each line with edge-tts and records the timing of every word. If edge-tts can't connect, it falls back to espeak-ng.

`pipeline/make_video.py` draws each scene (`pipeline/scene.html`: hook title, card, speaker tag, mascot) in headless Chromium. The mouth flaps while a line is spoken, karaoke captions are burned in with ffmpeg, and it writes `video.mp4`, `caption.txt` and `REVIEW.md`.

The mascot is called PITOU. Change it with the `HOST_NAME` variable in the workflow. Don't call it "Claude" on your channel unless you are fine with it looking like an official Anthropic character.

## Rules this pipeline enforces (and you should too)

No earnings or income claims. The reference videos say a creator makes $400k a month, and that is exactly what not to copy. No client or brand names without permission. Every number on screen is either from the brief or part of an obviously fictional joke. One niche, one style, post daily.

## Next upgrades (not built yet)

Auto-publishing after you approve, by uploading to YouTube Shorts through the YouTube Data API when you comment `/post` on the issue. TikTok and Instagram APIs need app review, so post those by hand for now. A Telegram bot that sends the video straight to your phone. A trending-repo finder that drafts topic briefs from GitHub's fastest-growing AI repos each week, for you to approve.
