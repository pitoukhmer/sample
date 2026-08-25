# The Frontend Polish Playbook

A repeatable process for taking an existing, working-but-unpolished interface to
launch quality — and a service you can sell.

This document is the operator's manual. The machine-readable half lives in
`.claude/skills/polish-frontend/SKILL.md`; the worked example is this repository.

---

## What this is, and what it is not

**It is:** a finishing process for software that already works. The product
decisions are made, the routes exist, the data flows. What's missing is
typography, spacing, states, responsiveness, and accessibility.

**It is not:** product design, brand identity, or a rewrite. If the client
doesn't know what the screen is *for*, polish cannot save it — that's a
different, more expensive engagement.

This distinction is the whole business model. "Redesign my app" is an unbounded
project that goes over budget. "Polish these 6 screens to a written standard,
verified by an automated gate" is a fixed-scope job you can quote, deliver, and
prove in days.

---

## Why it works (the actual mechanism)

Asking any model to "make this look good" fails for a structural reason: it's an
under-specified request, so the model answers with the mean of its training
data. That mean is the gradient hero, the glassmorphic card, the purple accent —
what people call "AI slop." The output isn't bad because the model is weak. It's
bad because the prompt had no pass/fail condition.

The fix is two files and one loop:

1. **`DESIGN.md`** — turn the aesthetic into a written spec with real values and
   an explicit list of what you are ruling out. Now "make it look good" has a
   right answer.
2. **A browser gate** — turn the quality bar into an executable check that exits
   non-zero. Now "it looks fine to me" has evidence behind it.
3. **Render → gate → look → fix** — loop until the gate passes *and* your eye
   passes. The gate has no taste; you still have to look at the screenshots.

Everything else is detail.

---

## The five phases

| Phase | Output | Typical time |
|---|---|---|
| 0. Inventory | Stack constraints, every state that must render, scoping boundary | 30–60 min |
| 1. `DESIGN.md` | Tokens, components, a11y gates, anti-goals | 1–2 h (once per client) |
| 2. Implement | Token-driven CSS + semantic markup | 2–6 h per screen group |
| 3. Fixture renderer | Real templates → static HTML, no DB needed | 1–2 h (once per stack) |
| 4. Gate | Pass/fail across page × theme × breakpoint, screenshots | minutes per run |
| 5. Report | Before/after, gate output, "what did not change" | 30 min |

Phases 1 and 3 are one-time per client or per stack. From the second project
onward you are mostly running phases 0, 2, 4, 5 — which is where the margin is.

---

## Phase 0 — Inventory

Do this before writing a line of CSS. Getting it wrong wastes the entire pass.

**Stack constraints.** Is there a build step? What template syntax? Which files
are safe to edit? Is the UI embedded in a host shell whose styles you must not
disturb?

**Every state.** Populated, empty, error, loading, long content, longest
realistic string. Empty states are the most-skipped and most-seen screen in any
CMS-backed product.

**The scoping boundary.** If this ships inside someone else's application, every
selector needs one root class. A style leak into a client's admin panel is the
fastest way to lose the account.

---

## Phase 1 — `DESIGN.md`

A plain-text design system at the project root that any coding agent reads
before generating UI. No Figma export, no JSON schema, no tooling.

The format is a real convention — introduced by Google Stitch and collected at
[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md),
which holds 73 `DESIGN.md` files extracted from real sites. Two ways to use it:

- **Borrow a direction:** copy the closest file from that collection as a
  starting point, then edit it to the client's brand.
- **Write one from the brand:** if the client has real brand assets, encode
  those instead. This is the version you charge for.

See `DESIGN.md` in this repository for a complete worked example.

**The single most important section is the anti-goals list.** Positive
instructions ("clean, modern, professional") are what produce generic output —
every model agrees on what those mean. Negative constraints are what make the
result specific:

> No gradient hero banners, no glassmorphism, no neon glows, no
> "AI-startup purple." No drop shadows on flat list rows. No emoji as
> iconography. Tabular data is left-aligned.

Second most important: **ground the direction in a real reference, not an
adjective.** Name a site whose restraint you're matching. A reference beats a
vibe, every time.

---

## Phase 2 — Implement

Rules that keep the output consistent and reviewable:

- Tokens once, as CSS custom properties. Every later value is `var(--…)`. A raw
  literal in a rule is a bug you can grep for.
- Define the complete light palette on the base selector. Redefine **only token
  values** for dark, under both `prefers-color-scheme` and an explicit
  `[data-theme]` selector. Never let a color's only definition live inside a
  media query — that's the usual cause of half-broken dark mode.
- Mobile-first. A table that scrolls sideways on a phone is a failure; reflow it
  to cards with the column name as a label.
- Semantic markup first. Real `<th scope>`, real `<label for>`, real `<nav>`.
  Most accessibility gates pass for free when the HTML is honest.
- Match the file's existing indentation and comment style. Polish should look
  like it belongs to the project.

---

## Phase 3 — The fixture renderer

Most real projects can't be seen without booting a database, a CMS, or an
authenticated session. So build a small script that renders the **real
templates** against fixture data and writes plain HTML.

This is the step almost everyone skips, and it's what makes the process
repeatable. It renders the actual template — so verification can't drift from
reality the way a hand-copied mock does — and it runs anywhere, with no
credentials.

Make the fixtures hostile on purpose: the longest realistic string, the empty
set, a unicode name. Those are the cases that break layouts in production.

See `preview/render.php` for a 120-line example that handles a template
language, a language file, loops, and conditionals.

---

## Phase 4 — The gate

`preview/verify.mjs` loads every rendered page in real Chromium and asserts,
across page × theme × breakpoint:

- Zero console errors and warnings
- No horizontal page scroll at 360 / 768 / 1280
- Every tap target ≥ 44×44px
- Every focusable element has a visible focus indicator
- Text contrast ≥ 4.5:1 (≥ 3:1 large), computed from real rendered colors
- A screenshot captured for the record

It exits non-zero on any failure, so it runs in CI.

```bash
npm install playwright && npx playwright install chromium
php preview/render.php && node preview/verify.mjs
```

**Then look at the screenshots.** The gate has no taste. It will happily pass a
page that is accessible, responsive, and ugly. Judging hierarchy, crowding, and
whether the empty state says anything useful is still your job. Loop until both
the machine and your eye agree.

---

## Phase 5 — The client report

Deliver four things:

1. Before/after screenshots at each breakpoint, light and dark.
2. The gate output — the pass line is the proof.
3. The file diff.
4. **An explicit statement of what did not change.** Behaviour, routes, form
   fields, data access.

Item 4 is what earns trust. A client's real fear about a redesign is that
something silently breaks. Saying "these 4 files changed, all presentational,
your form fields are byte-identical, here's the diff" answers the fear directly.

---

## Packaging it as a service

**Scope it per screen group, not per app.** "The 6 screens in the customer
portal" is quotable. "The app" is not.

**Fixed-price, three tiers:**

| Tier | Includes | Good for |
|---|---|---|
| Audit | Phase 0 + 1 + a gate run against the current UI, with the failure list | Selling the next tier. Cheap, fast, and the failure list sells itself |
| Polish | Phases 0–5 on an agreed screen list | The core offer |
| System | Polish + `DESIGN.md` + gate wired into their CI, so it holds | Highest value; the gate keeps earning after you leave |

**Lead with the audit.** Run the gate against a prospect's existing site and
send them the failure list: the contrast failures, the tap targets under 44px,
the horizontal scroll on mobile. It's concrete, it's checkable, and it isn't an
opinion about their taste. It converts far better than a portfolio.

**What to promise:** a written standard, a verified result, and no behaviour
change. **What not to promise:** more conversions. You cannot verify that in a
gate, so don't sell it.

---

## Honest limits

- The gate checks correctness, not beauty. It cannot tell you the design is
  good, only that it isn't broken. Human judgement is still load-bearing.
- Contrast checks sample representative elements, not every node. They catch
  systematic token problems, not every one-off.
- Automated checks cover a real but partial slice of accessibility. Screen
  reader behaviour, focus order sanity, and whether your labels actually make
  sense still need a person.
- This process cannot rescue an interface whose underlying product is unclear.
- None of this is exclusive knowledge. The advantage is in running it
  consistently and being able to *prove* the result — not in knowing it exists.
