# Breakdown of the 3 reference videos

All three come from the same faceless "AI tools" format. A viewer stand-in talks to an AI mascot that it calls "Claude". The mascot introduces one free GitHub project, explains it in three or four steps, lands a joke, and closes with "Comment KEYWORD" so the comment can trigger an automatic DM with the link. Each runs 61 to 81 seconds and is built in code: 3D characters, UI cards drawn as HTML, word-by-word captions with the spoken word highlighted, and a progress bar of steps along the top.

## Video 1: "Your own AI streamer" (61s, comment LIVE)

The guy asks the mascot about an AI girl who streams on Twitch. The mascot says yes, he can build one, and explains in three parts.

"Who she is" introduces Neuro-sama, an AI VTuber who chats, sings and plays games live for hours. The video claims 160,000 people pay to watch her and that her creator makes about $400,000 a month without ever showing his face.

"How she works": someone types in chat, an AI reads it and writes a reply, a voice reads the reply aloud, and an animated face lip-syncs every word. A counter shows the AI doing all the talking (1,267 words) while the human says nothing.

"How you make yours" covers Open-LLM-VTuber, which is free on GitHub and runs on your own laptop. You pick a face, a voice and a personality ("sweet, savage, total chaos"), and she can watch your screen while you play. The joke ending has her roasting the player every time he falls ("Fall number twelve. A new record."). On-screen copy reads "That's the whole show".

Frame details: a split screen, with the info card on top and a podcast-studio scene below that has an "ON AIR" sign and fake chat messages ("wait, she is LIVE?", "400K A MONTH"). The end card reads "Send this to the friend who says 'I'd go live, but…' · Comment LIVE for the free setup guide".

Flag: the $400,000/month and 160,000 paid subscriber numbers are unverified earnings claims. Don't repeat them.

## Video 2: "6-Hour GTA 6 Stream, 11 Views" (81s, comment CLIPS)

A noob character in a hoodie complains: GTA 6 is out, everyone is posting clips, and he streamed six hours for 11 views. The mascot tells him to stop scrubbing the timeline and introduces "AI YouTube Shorts Generator", a free, MIT-licensed, open-source alternative to Opus Clip. It watches the whole stream, finds the best moments and cuts vertical shorts, with no watermark and no credits.

"What's the catch?" "No catch. Three steps." Step 1: clone the repo and add an OpenAI or Gemini key (the screen shows `git clone …SamurAIGPT/AI-Youtube-Shorts-Generator` and a `.env` with `LLM_PROVIDER=openai`). Step 2: drop in the recording and ask for five clips (`python main.py gta6_stream.mp4 --num-clips`). Step 3: it transcribes all six hours, scores every moment for hooks and emotional peaks, and crops the winners from 16:9 to 9:16.

Twist: the top clip scores 94/100, and it isn't the car chase. It's him on the phone with his mom saying "It's not violent, Mom. It's educational. I'm learning about Florida." He begs them not to post it, the mascot answers "You said post the best one", the clip gets 12,000 views, and he says "Make me four more." Comment CLIPS for the link.

Note: the repo now lives at Anil-matcha/AI-Youtube-Shorts-Generator (about 6.6k stars, MIT, updated this week). The 12,000 views are part of the joke, not a real result.

## Video 3: "Starting a new Instagram page" (65s, comment FILM)

The guy wants to start an Instagram page, go viral and make money. The mascot points him to a free toolbox with 59 kinds of video, which is Lemo-Opuscar, a Claude Code plugin.

Step 1: paste two lines into Claude Code (`claude plugin marketplace add lemomo-ai/lemo-opuscar`, then `claude plugin install lemo-opuscar@lemolab`). Step 2: pick a look, and each style comes with the niche it suits. Watercolor is for calm stories and travel, crayon picture book for kids' stories ("parents share these"), 16-bit pixel game for gaming and life recaps, Japanese woodblock for history and myths, fifties cartoon for how-to guides, and tiny toy city for satisfying city scenes. "Which one goes viral? The one you post every day, not the one you post once." Step 3: give it a style and a story, for example "Make a 45-second vertical film in the watercolor style. A lost dog finds his way home." It draws the film, adds music and narrates it in about 30 to 60 minutes. Step 4: one style, one topic, post every day. A grid fills up over 30 days to 2,480 followers. Using all 59 styles on one page means "nobody knows what your page is". The closing joke is that his style is crayon book: "Simple. Colorful. A little confused."

Note: Lemo-Opuscar is real and now has 99 styles and about 21k stars. Its license reports as non-standard on GitHub, so read it before you use it commercially. The 2,480 followers is an illustration.

## What they have in common (the formula)

1. Hook in the first 2 seconds: a painful number ("6 hours, 11 views") pinned as a title for the whole video.
2. Two characters, so the video plays as a conversation instead of a lecture. The skeptic asks "what's the catch?", which keeps people watching.
3. One free, open-source tool, shown as a GitHub card with Free and MIT badges.
4. Three numbered steps with real commands on screen, which is why people save these (751 saves on video 2).
5. A comedic twist near the end, which earns comments and shares.
6. A "Comment KEYWORD" CTA. The comments push reach, and an auto-DM tool (ManyChat or similar) sends the link and collects leads.
7. Word-highlighted captions, constant visual change every 1 to 2 seconds, no face, no camera.
