# Global rules for all Pitou AI and Pitou Foods projects

Save this file as ~/.claude/CLAUDE.md so every project on this machine inherits it.
Per-project CLAUDE.md files should only add Overview, Commands, Architecture and Conventions.

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

# Roles

- Main Claude Code session: boss. Owns context, decides, writes the final result.
- GPT-6 Astra (via `codex exec --model gpt-6-astra`): worker and second opinion for architecture, design direction, long briefs and bulk drafting.
- Codex review (via `/codex:review` or `codex exec --sandbox read-only`): reviewer of the final diff or document before finishing.
- Cap Astra consults at 3 per task. Say when a consult is skipped and why.
- When reporting, show three things: what Astra recommended, what was decided, what Codex found.

# Content and business guardrails (apply to both Claude and Astra output)

- Pitou Foods: never state or imply Halal certification.
- Never write a price, earnings claim or client name as fact unless it is confirmed in the project's own notes. Flag it as unconfirmed instead.
- Keep responses concise. Lead with the answer, then the reasoning.
- No em dashes.
