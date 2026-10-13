# GPT-6 Astra as the worker, Fable 5.1 as the boss: frame-by-frame breakdown and rollout playbook for all Pitou projects

This document is a frame-by-frame and word-by-word read of a 40-second vertical video (720x1280, 29.97 fps, 1,202 frames) showing how to run OpenAI's GPT-6 Astra inside Claude Code so Claude delegates work to Astra and asks Codex to review it. Part 1 is the transcript. Part 2 is every on-screen command and text, with timestamps. Part 3 is the step-by-step setup. Part 4 is how to roll it out across every Pitou AI and Pitou Foods project. Part 5 lists what was verified and what was not. Compiled 2026-10-13 from the video's burned-in captions and screen recordings (the audio track could not be machine-transcribed in this environment, so the transcript is reconstructed from the one-word-at-a-time captions; two checks against the speaker's lip movement and context are noted inline).

## Part 1. Full transcript (reconstructed from captions, in order)

"Most people don't know you can run OpenAI's new GPT-6 Astra inside of Claude Code and stop burning through your token limits. To do this, you make Fable the boss and Astra the worker. They hand work back and forth and cover each other's gaps. You get both models while using less of each one. Setting up is easy. First, make sure you have a ChatGPT account and a Claude account. Then you'll need Codex and Claude Code installed. Then install the plugin that connects both of them. Last, paste a few sections into your CLAUDE.md that tell them how to hand off work, check each other's work. After that, you're good to go. Make sure you save this video so you can come back to it later and try this for yourself."

Caption notes: at 11.0s the caption reads "Their" but the sentence is "They hand work back and forth". At 34.0s the caption "work" repeats three times over the CLAUDE.md screen; it is one word, held while the file is highlighted.

## Part 2. Frame-by-frame: every screen, command and on-screen text

| Time | What is on screen | Exact on-screen text or command |
|---|---|---|
| 0.0 to 1.2s | Fable 5.1 logo (orange asterisk) connected by an animated line to the OpenAI logo | `FABLE 5.1` and `GPT-6 ASTRA` labels |
| 1.2 to 4.0s | OpenAI logo, then the model title and a code chip | `GPT-6 ASTRA`, chip reads `model: gpt-6-astra` |
| 3.8 to 5.4s | Windows PowerShell running Claude Code in a project folder | `Claude Code v2.1.280`, `Sonnet 5 with medium effort`, `Claude Max`, `~\astra-demo`, then `Consulting GPT-6 Astra on the plan`, `Ran 1 shell command`, footer `auto mode on (shift+tab to cycle)` |
| 5.4 to 7.8s | "STOP BURNING YOUR LIMITS" comparison graphic | Row 1 `CLAUDE ONLY` fills to `100%` with `5-hour limit reached · resets 4:00 PM`. Row 2 `FABLE + ASTRA` stops at `40%` with a green `still running` badge |
| 7.8 to 10.8s | Org chart | Top card `FABLE 5.1` tagged `BOSS`. Bottom card `GPT-6 ASTRA` tagged `WORKER`. Arrows labelled `delegates` (down) and `returns` (up) |
| 11.0 to 12.8s | Claude Code terminal, end of the user's prompt and the first steps | Prompt tail: `Show me what Astra recommended, what you decided to do, and what Codex found. If Codex finds a real problem, fix it. Then give me the final result.` Then `Skill(astra-advisor:astra-advisor)` → `Successfully loaded skill`, `Read 2 files, ran 2 shell commands`, `Codex CLI is available. Now I'll write the brief and consult Astra.`, `Ensuring scratchpad directory exists` → `mkdir -p "$TMP/astra_landing"` |
| 13.0 to 13.8s | Claude consults Astra through the Codex CLI | `Made 1 scratchpad edit +42, ran 2 shell commands`. `Consulting GPT-6 Astra on landing page structure/design/tech approach (trigger: user explicitly requested Astra second opinion, interaction 1/3).` `Running Astra consult via Codex CLI · 6s` with env vars `TASK_TMP="/c/Users/ADMINI~1/AppData/Local/Temp/claude/.../scratchpad"`, `TASK_PROJECT="/c/Users/Administrator/astra-demo"`, then `codex exec --model gpt-6-astra \` (rest of the command is cut off) |
| 14.0 to 15.4s | Claude builds the page from Astra's advice | `Astra's verdict is in. Now I'll build the landing page directly with plain HTML/CSS/JS as recommended.` `Write(index.html)` → `Wrote 424 lines to index.html` (title `Flowstate – Focus on what matters`). `The page is built. Now let's have Codex review it.` |
| 15.6 to 16.2s | Codex review command | `Running Codex review with explicit cd flag` → `codex exec --sandbox read-only --ephemeral --color never --cd "C:\Users\Administrator\astra-demo" --output-last-message "C:\Users\...\scratchpad\codex_review.txt" "Review the file index.html in t..."` with `(ctrl+b to run in background)`. Status line `Elucidating… (4m 21s · ↓ 8.3k tokens)` |
| 16.4 to 17.0s | Claude applies Codex's findings | `Update(index.html)`: `.btn-primary` background `var(--accent)` → `var(--accent-dark)`; hover `var(--accent-dark)` → `#8f3f1b`; `.hero-note` → `.hero-copy .hero-note`. Then `Both fixes applied. Now let's verify the page renders correctly in a browser.` Status `(5m 9s · ↓ 10.4k tokens)` |
| 19.2 to 22.2s | "YOU NEED BOTH ACCOUNTS" | Card 1 `ChatGPT`, badge `ChatGPT Plus $20/mo`, `READY`. Card 2 `Claude`, badge `Claude Max $100/mo`, `READY` |
| 22.4 to 23.4s | Install Codex CLI | `npm install -g @openai/codex` → `installed`, then `OpenAI Codex (v0.155.1)`, `model: gpt-6-astra  /model to change`, `directory: ~` |
| 23.6 to 25.0s | Install Claude Code | `npm install -g @anthropic-ai/claude-code` → `installed`, `Claude Code v2.1.280`, `Sonnet 5 with medium effort`, `Claude Max` |
| 25.2 to 25.8s | Add the plugin marketplace inside Claude Code | `/plugin marketplace add openai/codex-plugin-cc` → `Successfully added marketplace: openai-codex`. `/reload-plugins` → `Reloaded: 8 plugins · 83 skills · 6 agents · 3 hooks · 35 plugin MCP servers · 0 plugin LSP servers`. Then `/plugin install codex@openai-codex` |
| 26.0 to 27.4s | Plugin details dialog | `codex  Version: 1.0.6`, `Use Codex from Claude Code to review code or delegate tasks.`, `By: OpenAI`, `Will install: Components will be discovered at installation`, plus the standard trust warning |
| 27.6 to 28.4s | Windows Explorer | Folder `astra-demo` containing one file, `CLAUDE.md` |
| 28.6 to 29.4s | CLAUDE.md template open in an editor | `astra-demo` / `Overview` (`TODO: describe what this project is and does.`) / `Commands` (`TODO: add build/test/lint/run commands once the project has code.`) / `Architecture` (`TODO: note key directories, entry points, and design decisions as they emerge.`) / `Conventions` (`TODO: record any project-specific conventions (naming, style, testing approach).`) |
| 29.6 to 34.2s | The pasted "AI Collaboration Rules" section, each line highlighted in turn | Full text reproduced in Part 3, step 6 |
| 34.4 to 40.1s | Speaker only | Outro ("After that you're good to go…") |

## Part 3. Step-by-step setup (what the video does, in the right order)

Step 1. Have both accounts. A ChatGPT account and a Claude account. The video shows ChatGPT Plus and Claude Max. Prices shown in the video ($20 and $100 per month) are the creator's figures and are not confirmed here; check both pricing pages before paying. A ChatGPT subscription or an OpenAI API key is what the Codex plugin needs; Astra access on the Plus tier was staged after Pro and Enterprise according to third-party reports, so confirm your tier actually exposes `gpt-6-astra` before relying on it.

Step 2. Install the Codex CLI.

```
npm install -g @openai/codex
codex login
codex
```

Inside Codex, type `/model` and pick `gpt-6-astra`. The video shows Codex v0.155.1 with Astra already the default. Third-party notes put Astra support at Codex CLI 0.153.x or newer, so upgrade if `/model` does not list it.

Step 3. Install Claude Code.

```
npm install -g @anthropic-ai/claude-code
claude
```

The video runs Claude Code v2.1.280 on a Claude Max plan, default model Sonnet 5 at medium effort.

Step 4. Connect them with OpenAI's official plugin. Inside a Claude Code session:

```
/plugin marketplace add openai/codex-plugin-cc
/plugin install codex@openai-codex
/reload-plugins
/codex:setup
```

The video runs `/reload-plugins` before the install. Run it after the install, or the `/codex:*` skills do not appear. `/codex:setup` checks that Codex is installed and logged in. The plugin provides `/codex:review`, `/codex:rescue`, `/codex:status`, `/codex:result` and `/codex:cancel`, and background execution. It does not bundle Codex; it calls the `@openai/codex` binary you installed in step 2.

Step 5. Put a CLAUDE.md in the project. The video starts from the four-section template (Overview, Commands, Architecture, Conventions). If a project has no CLAUDE.md yet, run `/init` in Claude Code to generate one.

Step 6. Paste the AI Collaboration Rules into CLAUDE.md. This is the exact text from the video:

```
# AI Collaboration Rules

When a task is complicated, use Codex or Astra for a second opinion.

For important technical decisions:
1. Ask Astra for an independent opinion.
2. Review the advice.
3. Make the final decision.
4. Implement the change.
5. Use Codex to review the final changes.
6. Fix valid problems found by the review.
7. Run the tests before finishing.

Do not use Astra or Codex for every small task.

The main Claude Code session remains responsible for the final decision.
```

Step 7. Reproduce the `astra-advisor` skill. The video's Claude session loads a skill called `astra-advisor` that is not part of OpenAI's plugin; it is the creator's own. What it does is visible on screen: write a brief to a scratchpad, run `codex exec --model gpt-6-astra` with that brief, cap consults at three per task ("interaction 1/3"), then build, then run a read-only Codex review with `--output-last-message` into a text file, then fix what the review found. A paste-ready equivalent is in `reports/astra-worker-setup/astra-advisor-SKILL.md`. Save it as `~/.claude/skills/astra-advisor/SKILL.md` so it is available in every project.

Step 8. Prompt pattern. The video's prompt ends with the lines that make the loop visible, so reuse them:

```
[Describe the task.]
Ask Astra for a second opinion on the approach before building.
Show me what Astra recommended, what you decided to do, and what Codex found.
If Codex finds a real problem, fix it.
Then give me the final result.
```

## Part 4. Rolling this out across all Pitou AI and Pitou Foods projects

Install once, globally. Codex CLI, Claude Code and the plugin are per machine, not per project. Do steps 2 to 4 once on each machine you work from.

Put the rules at user level, not per project. Claude Code reads `~/.claude/CLAUDE.md` for every project on the machine. Paste the AI Collaboration Rules there once, and every repo inherits them. A paste-ready version with Pitou-specific guardrails is at `reports/astra-worker-setup/global-CLAUDE.md`. Per-project `CLAUDE.md` files then only need Overview, Commands, Architecture and Conventions plus anything project-specific.

Decide the roles explicitly. The video's split works for code and should stay the default:

- Fable (or whatever model the main Claude Code session runs) is the boss: owns context, makes decisions, writes the final result.
- Astra is the worker and second opinion: architecture choices, design direction, long briefs, bulk drafting, anything where a fresh model with no shared context is useful.
- Codex is the reviewer: read-only review of the diff before finishing.

Use Astra for the expensive parts, not every call. The video's own rule is "do not use Astra or Codex for every small task." In practice that means Astra on planning, big drafts and reviews of large changes, and the main session on edits, file reads and small fixes. That is what produced the 40% versus 100% usage graphic in the video; the number is the creator's, not a benchmark.

Non-code projects work the same way. The handoff is just a brief in a text file and a `codex exec` call, so marketing pages, product copy, research notes and Pitou Foods content can go through the same loop. For those, swap step 5 of the rules ("Use Codex to review the final changes") for a Codex review of the document against the project's guardrails.

Guardrails that must live in the global CLAUDE.md so both models obey them:

- Pitou Foods: never state or imply Halal certification.
- Flag any price, earnings figure or client name that is not confirmed in the project's own notes instead of writing it as fact.
- The main Claude session keeps the final decision; Astra and Codex advise.

Suggested order for turning it on across projects:

1. This machine: steps 2 to 4, then the global CLAUDE.md and the global skill.
2. One low-risk project first (an internal tool or this repo), run the step 8 prompt end to end, and read the three outputs (Astra's advice, the decision, Codex's findings).
3. Then each Pitou AI client project, adding its own `CLAUDE.md` Commands section so step 7 of the rules ("run the tests") has something to run.
4. Pitou Foods content and marketing repos last, with the Halal and pricing guardrails confirmed in their project CLAUDE.md as well as the global one.

## Part 5. What was verified and what was not

Verified against the video frames: every command, version number, plugin name, model ID string, CLAUDE.md text and prompt wording in Part 2.

Verified against current public sources (2026-10-13): OpenAI's `codex-plugin-cc` is real and official, installed with `/plugin marketplace add openai/codex-plugin-cc` then `/plugin install codex@openai-codex` then `/reload-plugins`, needs Node 18.18+, and needs a ChatGPT subscription or OpenAI API key ([DEV Community](https://dev.to/creeta/openai-ships-codex-into-claude-code-two-commands-or-four-c7l), [SmartScope](https://smartscope.blog/en/blog/codex-plugin-cc-openai-claude-code-2026/), [Zenn](https://zenn.dev/zenchaine/articles/codex-plugin-for-claude-code?locale=en)). GPT-6 Astra is reported as rolling out in Codex CLI from early September 2026 with the model string `gpt-6-astra` ([Daniel Vaughan: configuration](https://codex.danielvaughan.com/2026/09/03/gpt-6-astra-codex-cli-configuration-context-notes-safety/), [Daniel Vaughan: integration guide](https://codex.danielvaughan.com/2026/09/04/gpt-6-astra-codex-cli-integration-guide-critical-cyber-threshold/)).

Not verified, treat as the creator's claims: the $20 and $100 monthly prices; the 40% versus 100% usage comparison; that Plus-tier ChatGPT accounts have Astra today (reports say Pro and Enterprise got it first); the exact Codex CLI minimum version (sources say 0.153.0 or 0.153.3); and the plugin version (the video shows 1.0.6, one source says 1.0.5). The `astra-advisor` skill is the creator's own and is not published anywhere I could find, so the version in this repo is a reconstruction from what the terminal shows, not a copy.

Also not covered by the video: cost of Astra calls on an API key instead of a subscription, and whether Codex plugin runs on your Cambodia network without a proxy. Both are worth a five-minute test before rolling out to client work.
