---
name: astra-advisor
description: Consult GPT-6 Astra (via the Codex CLI) for an independent opinion on a plan, design or technical approach, then have Codex review the finished change. Use when the user asks for an Astra or Codex second opinion, or when the task is complicated enough that the CLAUDE.md AI Collaboration Rules apply.
---

Save this file as ~/.claude/skills/astra-advisor/SKILL.md (global) or .claude/skills/astra-advisor/SKILL.md (one project).
Reconstructed from the terminal output in the source video; the original skill was not published.

# Astra advisor

## Preconditions

1. Check the Codex CLI is installed and logged in: `codex --version` and `codex login status`. If missing, tell the user to run `npm install -g @openai/codex` and `codex login`, then stop.
2. Set `TASK_PROJECT` to the project root and `TASK_TMP` to a scratchpad directory (`mkdir -p "$TMP/astra_<task>"`).
3. Count consults. Maximum 3 Astra consults per task. Announce each one as `interaction N/3` and the trigger (user asked, or the task is complicated per CLAUDE.md).

## Step 1. Write the brief

Write `$TASK_TMP/astra_brief.md` with: the goal in two sentences, the constraints (stack, deadline, budget, content guardrails from CLAUDE.md), what has already been decided, and the exact question for Astra. Keep it under 60 lines. Do not paste secrets or credentials.

## Step 2. Consult Astra

```
cd "$TASK_PROJECT" && codex exec --model gpt-6-astra \
  --sandbox read-only --ephemeral --color never \
  --output-last-message "$TASK_TMP/astra_verdict.txt" \
  "Read the brief at $TASK_TMP/astra_brief.md and give an independent recommendation. Be specific. List the top three risks."
```

Read `astra_verdict.txt`. Summarise it in five lines for the user as "What Astra recommended".

## Step 3. Decide and build

Decide what to take from Astra's advice and what to reject, and say so in two lines ("What I decided to do"). Then implement the change in the main session. Do not send the implementation to Astra.

## Step 4. Codex review

```
cd "$TASK_PROJECT" && codex exec --sandbox read-only --ephemeral --color never \
  --cd "$TASK_PROJECT" \
  --output-last-message "$TASK_TMP/codex_review.txt" \
  "Review the changed files for bugs, security issues and violations of CLAUDE.md. Report only real problems with file and line."
```

Run it in the background if it will take more than a minute. Read `codex_review.txt`. Fix every valid finding. Reject findings that are wrong and say why.

## Step 5. Finish

Run the project's tests or build (from the CLAUDE.md Commands section). Then report in this order: what Astra recommended, what you decided to do, what Codex found and what was fixed, the final result.
