/**
 * Design gate for the Sample module.
 *
 * Loads the rendered previews in a real browser and asserts the release gates
 * from DESIGN.md §10. Exits non-zero on any failure, so it can run in CI or as
 * an agent's verification step.
 *
 * Setup:  npm install playwright && npx playwright install chromium
 * Run:    php preview/render.php && node preview/verify.mjs
 *
 * If Chromium is already on the machine, point at it instead of downloading:
 *   CHROMIUM_PATH=/path/to/chrome node preview/verify.mjs
 */

import { chromium } from 'playwright';
import { pathToFileURL } from 'node:url';
import { mkdirSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const root = resolve(here, '..');
const shotDir = resolve(root, 'preview/screenshots');
mkdirSync(shotDir, { recursive: true });

const VIEWPORTS = [
  { name: 'mobile', width: 360, height: 780 },
  { name: 'tablet', width: 768, height: 900 },
  { name: 'desktop', width: 1280, height: 900 },
];

const PAGES = ['index', 'empty'];
const THEMES = ['light', 'dark'];

const failures = [];
const notes = [];
const fail = (m) => { failures.push(m); console.log(`  ✗ ${m}`); };
const pass = (m) => console.log(`  ✓ ${m}`);

/* --- WCAG contrast -------------------------------------------------------- */

const srgb = (c) => (c <= 0.03928 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4);

function luminance([r, g, b]) {
  return 0.2126 * srgb(r / 255) + 0.7152 * srgb(g / 255) + 0.0722 * srgb(b / 255);
}

function contrast(fg, bg) {
  const [a, b] = [luminance(fg), luminance(bg)].sort((x, y) => y - x);
  return (a + 0.05) / (b + 0.05);
}

const parseRGB = (s) => (s.match(/\d+(\.\d+)?/g) || []).slice(0, 3).map(Number);

/* --- run ------------------------------------------------------------------ */

// Honour a preinstalled Chromium when one is provided (CI images, sandboxes).
// Locally, `npx playwright install chromium` makes this unnecessary.
const executablePath = process.env.CHROMIUM_PATH || undefined;
const browser = await chromium.launch(executablePath ? { executablePath } : {});

for (const theme of THEMES) {
  for (const pageName of PAGES) {
    for (const vp of VIEWPORTS) {
      const label = `${pageName}/${theme}/${vp.name}`;
      const context = await browser.newContext({
        viewport: { width: vp.width, height: vp.height },
        colorScheme: theme,
        deviceScaleFactor: 2,
      });
      const page = await context.newPage();

      // Gate: zero console errors and warnings (DESIGN.md §10)
      const consoleMsgs = [];
      page.on('console', (m) => {
        if (m.type() === 'error' || m.type() === 'warning') consoleMsgs.push(`${m.type()}: ${m.text()}`);
      });
      page.on('pageerror', (e) => consoleMsgs.push(`pageerror: ${e.message}`));

      await page.goto(pathToFileURL(resolve(root, `preview/${pageName}.html`)).href, {
        waitUntil: 'load',
      });

      console.log(`\n▸ ${label}`);

      if (consoleMsgs.length) fail(`${label}: console output — ${consoleMsgs.join('; ')}`);
      else pass('no console errors or warnings');

      // Gate: no horizontal page scroll (DESIGN.md §10)
      const overflow = await page.evaluate(() => ({
        scrollW: document.documentElement.scrollWidth,
        clientW: document.documentElement.clientWidth,
      }));
      if (overflow.scrollW > overflow.clientW + 1) {
        fail(`${label}: horizontal scroll — content ${overflow.scrollW}px in ${overflow.clientW}px viewport`);
      } else pass(`no horizontal scroll (${overflow.scrollW}px ≤ ${overflow.clientW}px)`);

      // Gate: tap targets ≥ 44×44 (DESIGN.md §7.3)
      const small = await page.evaluate(() => {
        const out = [];
        for (const el of document.querySelectorAll('a, button, input, select, textarea')) {
          const r = el.getBoundingClientRect();
          if (r.width === 0 && r.height === 0) continue;
          if (r.width < 44 || r.height < 44) {
            out.push(`${el.tagName.toLowerCase()}"${(el.textContent || '').trim().slice(0, 20)}" ${Math.round(r.width)}×${Math.round(r.height)}`);
          }
        }
        return out;
      });
      if (small.length) fail(`${label}: tap target under 44px — ${small.join(', ')}`);
      else pass('all tap targets ≥ 44×44');

      // Gate: focus is always visible (DESIGN.md §7.2)
      const focusables = await page.locator('a, button, input, select, textarea').all();
      let focusBad = 0;
      for (const el of focusables) {
        if (!(await el.isVisible())) continue;
        await el.focus();
        const ok = await el.evaluate((node) => {
          const s = getComputedStyle(node);
          const w = parseFloat(s.outlineWidth) || 0;
          return (s.outlineStyle !== 'none' && w >= 1) || s.boxShadow !== 'none';
        });
        if (!ok) focusBad++;
      }
      if (focusBad) fail(`${label}: ${focusBad} focusable element(s) with no visible focus indicator`);
      else pass(`focus visible on all ${focusables.length} focusable element(s)`);

      // Gate: text contrast (DESIGN.md §7.4 / §8)
      const samples = await page.evaluate(() => {
        const bgOf = (el) => {
          let n = el;
          while (n) {
            const bg = getComputedStyle(n).backgroundColor;
            if (bg && bg !== 'rgba(0, 0, 0, 0)' && bg !== 'transparent') return bg;
            n = n.parentElement;
          }
          return 'rgb(255,255,255)';
        };
        const sel = [
          '.sample-header__title', '.sample-data__th', '.sample-data__name',
          '.sample-data__slug', '.sample-empty__title', '.sample-empty__hint',
          '.sample-pagination .current', '.sample-pagination a',
        ];
        const out = [];
        for (const s of sel) {
          const el = document.querySelector(s);
          if (!el) continue;
          const cs = getComputedStyle(el);
          out.push({ sel: s, fg: cs.color, bg: bgOf(el), size: parseFloat(cs.fontSize), weight: cs.fontWeight });
        }
        return out;
      });

      for (const s of samples) {
        const ratio = contrast(parseRGB(s.fg), parseRGB(s.bg));
        // WCAG "large text": ≥24px, or ≥18.66px when bold
        const large = s.size >= 24 || (s.size >= 18.66 && Number(s.weight) >= 700);
        const gate = large ? 3 : 4.5;
        if (ratio < gate) fail(`${label}: ${s.sel} contrast ${ratio.toFixed(2)}:1 < ${gate}:1`);
        else notes.push(`${label} ${s.sel} ${ratio.toFixed(2)}:1`);
      }
      pass(`contrast checked on ${samples.length} text role(s)`);

      // Clear focus so the reference screenshot is not left showing a focus ring.
      await page.evaluate(() => document.activeElement?.blur());

      await page.screenshot({
        path: resolve(shotDir, `${pageName}-${theme}-${vp.name}.png`),
        fullPage: true,
      });

      await context.close();
    }
  }
}

await browser.close();

console.log('\n' + '─'.repeat(64));
if (failures.length) {
  console.log(`DESIGN GATE FAILED — ${failures.length} issue(s):`);
  for (const f of failures) console.log(`  • ${f}`);
  process.exit(1);
}
console.log(`DESIGN GATE PASSED — ${PAGES.length * THEMES.length * VIEWPORTS.length} view(s), ${notes.length} contrast checks, 0 failures.`);
console.log(`Screenshots: preview/screenshots/`);
