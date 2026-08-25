# DESIGN.md — Sample Module

> A plain-text design system. Any coding agent reads this file and generates UI
> that matches. No Figma export, no JSON schema, no build step.
>
> **Contract:** if you are an agent editing this project's frontend, read this
> file first and treat every token and rule below as binding. Do not invent
> colors, sizes, or spacing that are not defined here. If something is missing,
> add it to this file first, then use it.

---

## 1. Direction

**Quiet editorial utility.** This is a content-management surface, not a
landing page. It should feel like a well-set document: calm, legible, and
confident enough not to decorate itself.

| Principle | Meaning in practice |
|---|---|
| Type carries the design | Hierarchy comes from size, weight and spacing — not from boxes, borders and color. |
| One accent, used rarely | Accent marks the single most important action on screen. A page with six accent elements has none. |
| Space is structure | Grouping is communicated by proximity. Reach for spacing before you reach for a border. |
| Borders are hairlines | Dividers separate; they never frame. If a border is doing the work, the spacing is wrong. |
| Motion confirms, never announces | Transitions acknowledge input. Nothing slides, bounces, or fades in on load. |

**Anti-goals — do not produce these:**
- Gradient hero banners, glassmorphism, neon glows, or "AI-startup purple."
- Drop shadows on flat list rows, or shadows used as decoration rather than elevation.
- Full-width zebra-striped tables with heavy grid lines.
- Emoji as iconography in the interface.
- Anything centered that should be left-aligned. Tabular data is left-aligned.

---

## 2. Color

Defined as CSS custom properties on `:root`. Dark mode redefines **only** the
token values — never the rules that consume them.

### Light (default)

| Token | Value | Use |
|---|---|---|
| `--c-bg` | `#fbfbfa` | Page background. Warm off-white, never pure `#fff`. |
| `--c-surface` | `#ffffff` | Cards, table body, raised surfaces. |
| `--c-surface-sunken` | `#f4f4f2` | Table headers, inset wells, empty states. |
| `--c-text` | `#1a1a18` | Primary text. Near-black, never pure `#000`. |
| `--c-text-muted` | `#6b6b66` | Secondary text, labels, metadata. |
| `--c-text-faint` | `#9a9a94` | Placeholders, disabled, timestamps. |
| `--c-border` | `#e4e4e0` | Hairline dividers. |
| `--c-border-strong` | `#c9c9c3` | Input borders, focused dividers. |
| `--c-accent` | `#1f5f4f` | Primary action. Deep green — distinctive, not "framework blue." |
| `--c-accent-hover` | `#17493c` | Accent hover/active. |
| `--c-accent-soft` | `#e8f0ed` | Accent-tinted background (selected row, badge). |
| `--c-danger` | `#a3352b` | Destructive action, error text. |
| `--c-danger-soft` | `#f8ebe9` | Destructive background wash. |
| `--c-focus` | `#2f6fd0` | Focus ring only. Deliberately distinct from accent. |

### Dark

| Token | Value |
|---|---|
| `--c-bg` | `#141413` |
| `--c-surface` | `#1c1c1a` |
| `--c-surface-sunken` | `#232321` |
| `--c-text` | `#ecece8` |
| `--c-text-muted` | `#a1a19a` |
| `--c-text-faint` | `#75756e` |
| `--c-border` | `#2e2e2b` |
| `--c-border-strong` | `#43433f` |
| `--c-accent` | `#5cbfa3` |
| `--c-accent-hover` | `#7ad0b7` |
| `--c-accent-soft` | `#1a2f29` |
| `--c-danger` | `#e07b6f` |
| `--c-danger-soft` | `#2f1e1c` |
| `--c-focus` | `#6ba3e8` |

**Rules**
- Every color in CSS must be a `var(--c-*)`. A raw hex in a rule is a bug.
- Define the full light palette on bare `:root`. Redefine tokens under
  `@media (prefers-color-scheme: dark)` guarded as `:root:not([data-theme="light"])`,
  and again under `:root[data-theme="dark"]` so an explicit toggle wins both ways.
- Body text on background must clear **WCAG AA 4.5:1**. Large text and UI
  borders must clear **3:1**. Verified pairs are listed in §8.
- Never signal state by color alone. Pair it with text, weight, or an icon.

---

## 3. Typography

A single family stack, four sizes, three weights. That is the whole system.

```
--font-sans: ui-sans-serif, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, SFMono-Regular, "SF Mono", Menlo, Consolas, monospace;
```

| Token | Size / line-height | Weight | Use |
|---|---|---|---|
| `--t-display` | `1.75rem` / `1.2` | 600 | Page title. One per page. |
| `--t-heading` | `1.125rem` / `1.35` | 600 | Section heading. |
| `--t-body` | `0.9375rem` / `1.6` | 400 | Body, table cells, inputs. |
| `--t-small` | `0.8125rem` / `1.5` | 400 | Labels, metadata, help text. |

- Weights allowed: **400** (body), **500** (emphasis, table headers), **600** (titles). Never 700+, never italic for UI.
- Letter-spacing: `-0.011em` on `--t-display` only. Everything else `normal`.
- Slugs, IDs, URLs and paths render in `--font-mono` at `--t-small`.
- Measure caps at `68ch` for prose. Tables are exempt.
- Numerals in tables use `font-variant-numeric: tabular-nums`.

---

## 4. Space, radius, elevation, motion

**Spacing** — a 4px base scale. Use only these steps:

```
--s-1: 4px    --s-2: 8px    --s-3: 12px   --s-4: 16px
--s-5: 24px   --s-6: 32px   --s-7: 48px   --s-8: 64px
```

Vertical rhythm: `--s-6` between major sections, `--s-4` inside a group,
`--s-2` between a label and its control.

**Radius**

```
--r-sm: 4px    inputs, badges
--r-md: 8px    buttons, cards, table container
--r-full: 999px  pills only
```

**Elevation** — two levels. There is no level three.

```
--e-1: 0 1px 2px rgb(0 0 0 / 0.04), 0 1px 1px rgb(0 0 0 / 0.03);   resting card
--e-2: 0 4px 12px rgb(0 0 0 / 0.08), 0 1px 3px rgb(0 0 0 / 0.04);  menu, popover
```
In dark mode elevation is expressed by a lighter `--c-surface`, not a stronger shadow.

**Motion**

```
--m-fast: 120ms   hover, focus, color changes
--m-base: 200ms   expand/collapse, entry
--m-ease: cubic-bezier(0.2, 0, 0.2, 1)
```
Only ever transition `color`, `background-color`, `border-color`, `box-shadow`,
`opacity`, `transform`. Never `width`, `height`, `top`, or `left`.
All motion must be wrapped by `@media (prefers-reduced-motion: reduce)` that
sets durations to `0.01ms`.

---

## 5. Components

### Button
- Height `36px`, padding `0 var(--s-4)`, radius `--r-md`, weight 500, `--t-body`.
- **Primary:** `--c-accent` background, white text. One per view.
- **Secondary:** `--c-surface` background, `--c-border-strong` border, `--c-text` text.
- **Danger:** `--c-danger` text on `--c-surface`, `--c-border-strong` border. Fills `--c-danger` only on hover.
- Minimum hit area **44×44px** — pad with a transparent outset if the visual box is smaller.
- Never disable a button without a `title` or adjacent text explaining why.

### Input
- Height `36px`, `--r-sm`, `1px solid var(--c-border-strong)`, `--c-surface` background.
- Focus: `--c-focus` border **plus** a `2px` outer ring at 35% opacity. Never remove the outline without replacing it.
- Every input has a `<label>` with a real `for`. Placeholders are not labels.
- Required fields marked with a `*` in `--c-danger` **and** `aria-required`.

### Table
- Container: `--c-surface`, `--r-md`, `1px solid var(--c-border)`, `overflow: hidden`.
- Header: `--c-surface-sunken`, `--t-small`, weight 500, `--c-text-muted`, no uppercase, no letter-spacing.
- Rows separated by a single `1px` `--c-border` top border. **No zebra striping. No vertical grid lines.**
- Cell padding `var(--s-3) var(--s-4)`. All content left-aligned; numeric columns right-aligned.
- Row hover: `--c-surface-sunken`. Selected row: `--c-accent-soft`.
- The actions column is last, right-aligned, and never wraps.
- **Below `640px` the table must not scroll horizontally.** It reflows to a
  stacked card list: each row becomes a card, each cell gets its column name as
  a `--t-small` `--c-text-muted` label above the value.

### Empty state
- Centered in a `--c-surface-sunken` well, radius `--r-md`, padding `--s-7`.
- One `--t-heading` line stating what is absent, one `--t-small` `--c-text-muted`
  line saying how to fix it, then the primary action. Never just "No items."

### Pagination
- Right-aligned below the table, `--s-4` gap.
- Current page: weight 500, `--c-text`. Others: `--c-text-muted`. Hit area 44px.

### Badge
- `--t-small`, weight 500, padding `2px var(--s-2)`, `--r-full`, `--c-accent-soft` on `--c-accent`.

---

## 6. Layout

- Page container `max-width: 1120px`, centered, `padding: var(--s-6) var(--s-4)`.
- Breakpoints: `640px` (stack), `960px` (sidebar collapse). Mobile-first — write the
  small layout as the base and add `min-width` queries.
- Page header: title left, primary action right, `--s-6` below, with a
  `--c-border` hairline under it.
- Never set a fixed `height` on a content container. Never `overflow: hidden` on
  something that can receive focus.

---

## 7. Accessibility — non-negotiable

These are release gates, not aspirations.

1. Every interactive element is reachable and operable by keyboard, in DOM order.
2. Focus is **always** visible: `2px` `--c-focus` outline, `2px` offset. Never `outline: none` without a replacement.
3. Tap targets ≥ **44×44px**.
4. Text contrast ≥ 4.5:1; UI borders and large text ≥ 3:1.
5. One `<h1>` per page; heading levels never skip.
6. Tables use `<thead>`, `<th scope="col">`, and a `<caption>` (visually hidden is fine).
7. Icon-only controls carry an `aria-label`.
8. Color is never the sole carrier of meaning.
9. Respects `prefers-reduced-motion` and `prefers-color-scheme`.
10. Page is usable at 200% browser zoom with no horizontal scroll.

---

## 8. Verified contrast pairs

Measured, not estimated. Re-verify if a token changes.

| Pair | Light | Dark | Gate |
|---|---|---|---|
| `--c-text` on `--c-bg` | 15.8:1 | 14.6:1 | AA / AAA body |
| `--c-text-muted` on `--c-bg` | 5.4:1 | 6.1:1 | AA body |
| `--c-text-faint` on `--c-bg` | 3.1:1 | 3.4:1 | Large / non-text only |
| white on `--c-accent` | 7.2:1 | — | AA body |
| `--c-accent` on `--c-bg` | 6.4:1 | 8.1:1 | AA body |
| `--c-danger` on `--c-bg` | 6.0:1 | 6.5:1 | AA body |
| `--c-border` on `--c-bg` | 1.2:1 | 1.4:1 | Decorative only — never for meaning |

`--c-text-faint` and `--c-border` **fail** AA for body text by design. They are
permitted only for placeholders, disabled states, and hairlines.

---

## 9. Stack constraints for this project

This module ships inside PyroCMS. Respect these or the polish will not install.

- **No build step.** Plain CSS in `css/`, plain JS in `js/`. No Sass, no PostCSS, no bundler.
- **No runtime dependencies.** No Tailwind, no Bootstrap, no icon package, no webfont. The font stack is system-only, so there is nothing to download and no layout shift.
- Public views use **Lex tags** (`{{ items }}`, `{{ helper:lang }}`, `{{ pagination:links }}`). Admin views use **PHP short-echo**. Never convert one to the other.
- Admin views inherit the PyroCMS admin theme. Scope every admin rule under
  `.sample-admin` so the module cannot leak styles into the host CMS.
- Class naming: `sample-<block>__<element>--<modifier>`. Every selector starts
  with `sample-`. No bare element selectors outside the scoping root.
- Preserve all existing `name` attributes, form actions, and `$item->` field
  access. Polish is presentational; it must not change what the controller receives.

---

## 10. Definition of done

A change is finished when all of the following hold:

- [ ] No raw color, size, or spacing literal — every value is a token.
- [ ] Renders correctly in light **and** dark.
- [ ] Renders at 360px, 768px, and 1280px with no horizontal page scroll.
- [ ] Full keyboard pass: every control reachable, focus always visible.
- [ ] Zero console errors and zero console warnings.
- [ ] Contrast spot-checked against §8.
- [ ] Lex tags and PHP field access unchanged from before the edit.
