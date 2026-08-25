---
name: polish-frontend
description: Take an existing, unpolished frontend to launch quality using a DESIGN.md design system plus an automated browser gate. Use when asked to polish, restyle, redesign, or "make launch-ready" any existing UI, or to set up a DESIGN.md for a project. Not for greenfield product design.
---

# Polish Frontend

A repeatable pass that takes a working-but-ugly interface to launch quality
**without redesigning the product**. It is deliberately boring: the leverage is
in writing the design system down *before* generating UI, and in verifying the
result in a real browser *after*.

## Non-negotiables

1. **Never change behaviour.** Form `name` attributes, form actions, route
   handlers, template variables and field access stay byte-identical. If a
   polish step requires a behaviour change, stop and ask.
2. **Never add a dependency the project doesn't already have.** No CSS
   framework, icon package, or webfont unless the project already ships one.
3. **Never skip the gate.** A change that has not been loaded in a browser is
   not finished, regardless of how good the diff looks.
4. **Never invent a token.** If a value isn't in `DESIGN.md`, add it to
   `DESIGN.md` first, then use it.

## Phase 0 — Inventory (do not skip)

Before writing any CSS, establish and write down:

- **Stack constraints.** Build step or not? Template engine and its syntax?
  Which files are safe to touch? A wrong assumption here wastes the whole pass.
- **Every state that must render.** Populated, empty, error, loading, long
  content, and the longest realistic string. Empty states are the most commonly
  missed and the most visible.
- **The existing visual contract.** If the UI is embedded in a host application
  (a CMS admin, a dashboard shell), your styles must be scoped so they cannot
  leak into it.

Report the inventory before proceeding.

## Phase 1 — Write DESIGN.md first

Create `DESIGN.md` at the project root. This is the highest-leverage step in the
whole process: it converts "make it look good" — which an agent will answer with
generic output — into a spec with a pass/fail condition.

It must contain, concretely and with real values:

| Section | Must specify |
|---|---|
| Direction | 3–5 principles, **plus an explicit anti-goals list** |
| Color | Every token, light **and** dark, as hex |
| Typography | Font stack, a 4-step scale, allowed weights |
| Space / radius / elevation / motion | Fixed scales; no ad-hoc values |
| Components | Per component: sizes, states, and the mobile behaviour |
| Accessibility | Numeric gates (contrast ratios, hit-area px) |
| Stack constraints | What must not be introduced |
| Definition of done | A checklist that can actually be checked |

**The anti-goals list is what prevents generic output.** "Make it look
professional" produces the same gradient-and-glassmorphism result every time.
"No gradient heroes, no glassmorphism, no emoji icons, tables are left-aligned"
produces something specific. Write down what you are ruling out.

Ground the direction in a **real reference**, not an adjective. Name a site or
product whose restraint you are matching, or point at an existing
`DESIGN.md`. A reference beats a vibe.

## Phase 2 — Implement against the tokens

- Define tokens once as CSS custom properties. Every subsequent value is a
  `var(--…)`. A raw hex, px, or ms literal in a rule is a bug.
- Define the full light palette on the base selector. Redefine **only token
  values** under `@media (prefers-color-scheme: dark)` and again under an
  explicit `[data-theme="dark"]` selector so a manual toggle wins both ways.
  Never give a color its only definition inside a media query.
- Write mobile-first. Add complexity at `min-width`, never subtract at
  `max-width`, except where a layout genuinely inverts (a table becoming cards).
- Semantic HTML first: real `<thead>`/`<th scope>`, real `<label for>`, real
  `<nav>`. Most accessibility gates pass for free if the markup is honest.
- Match the file's existing indentation and comment density. Polish should look
  like the project, not like a different author arrived.

## Phase 3 — Make it renderable

If the UI can only be seen by booting a full application (a CMS, an
authenticated app, a staging deploy), **build a fixture renderer**: a small
script that renders the real templates against sample data and writes plain
HTML.

This is the step most people skip, and it is what makes the rest repeatable:

- It renders the **real template**, so verification is meaningful — not a
  hand-copied mock that drifts.
- It runs in CI and in a sandbox with no database and no credentials.
- Fixtures deliberately include the pathological cases: the longest string, the
  empty set, the unicode name.

## Phase 4 — Gate it in a real browser

Run the design gate. Do not accept a change until it passes. Check, per page ×
per theme × per breakpoint:

- [ ] Zero console errors and warnings
- [ ] No horizontal page scroll at 360 / 768 / 1280
- [ ] Every tap target ≥ 44×44px
- [ ] Every focusable element has a visible focus indicator
- [ ] Text contrast ≥ 4.5:1 (≥ 3:1 for large text), computed not estimated
- [ ] A screenshot is captured for the record

Then **look at the screenshots**. The gate catches correctness, not taste. It
will happily pass a page that is accessible, responsive, and ugly. Read the
images and judge: is the hierarchy right? Is anything crowded? Does the empty
state say something useful?

Fix, re-render, re-gate. Loop until both the gate and your eye pass.

## Phase 5 — Report

Deliver: before/after screenshots at each breakpoint, the gate output, the file
diff, and an explicit statement of what was **not** changed (behaviour, routes,
data). The last item is what earns trust on a client project.

## Common failure modes

| Symptom | Cause | Fix |
|---|---|---|
| Output looks like every other AI page | No anti-goals, no reference | Phase 1 — name what you're ruling out |
| Passes the gate, still looks wrong | Nobody read the screenshots | Look at the images; the gate has no taste |
| Dark mode partly broken | A color defined only inside a media query | Define all tokens on the base selector first |
| Broke on real data | Fixtures were all short and tidy | Add the longest realistic string to fixtures |
| Styles leaked into the host app | Unscoped selectors | Scope every rule under one root class |
| Client says "you changed my form" | Renamed an input or action | Diff `name=`/`action=` before and after; they must match |
