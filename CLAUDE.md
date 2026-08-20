# ůnica Design System — Claude Code Context

## Design Context

Strategic and visual design context lives alongside this file — read them before any `/impeccable` design task:
- **[PRODUCT.md](PRODUCT.md)** — register (product), users, brand personality, anti-references, design principles, accessibility bar (WCAG 2.1 AA).
- **[DESIGN.md](DESIGN.md)** — visual system: real tokens (colors, typography, shape, elevation), component specs, Do's and Don'ts. Sidecar at `.impeccable/design.json` extends it with tonal ramps and self-contained component snippets.

## What this project is
A single-file coded design system documentation site for **ůnica** — Elona Jaquez's personal design system and studio brand. The doc site itself is one file: `index.html`. All CSS is in `<style>` blocks at the top, all JS inline at the bottom. No build step. No framework. No npm.

**Design tokens live outside index.html, in `tokens/tokens.css`** (linked via `<link rel="stylesheet" href="tokens/tokens.css">`), so the same tokens ship as the actual design system package and get consumed by the doc site's `var(--token-name)` usages. `index.html` never *declares* a `--space-*`/`--breakpoint-*`/`--grid-*`/etc. custom property — only `tokens/tokens.css` does. When adding or auditing a token, check there, not in index.html.

**Live site:** https://unica-design.github.io/unica  
**GitHub:** https://github.com/unica-design/unica  
**Figma file:** https://www.figma.com/design/gmjSnvSRO1Xb4WKwb4YXsv/unica-design-system  
**Local path:** `/Users/elona/ůnica/Claude/Unica Design System/`

---

## Critical architecture: one 26,000-line HTML file

`index.html` is ~26,500 lines. Every component page is a `<div class="page-panel" id="page-[name]">` inside a shared shell. The sidebar uses `data-page` attributes and JS to show/hide panels. **Never split this into multiple files.**

### Finding things in the file
```bash
# Find a component page
grep -n 'id="page-list-accordion"' index.html

# Find a CSS rule
grep -n '__body-text' index.html

# Find a JS function
grep -n 'initDropdown\|initLaPreview' index.html

# Find a symbol in the SVG sprite
grep -n 'id="ico-' index.html
```

### File regions (approximate lines)
| Region | Lines |
|---|---|
| CSS (all component + doc styles) | 1 – ~8150 |
| SVG sprite (`<defs>`) | ~8155 – 8290 |
| Sidebar + nav shell | ~8290 – 8400 |
| Foundation pages (Color, Type, Spacing…) | ~8400 – 8660 |
| Component pages | ~8660 – 19200 |
| Global JS (initDropdown, navigation, etc.) | ~19200 – 22500 |

---

## Component pages — current status

### ✅ Fully built
| Page ID | Component |
|---|---|
| `page-button` | Button |
| `page-choice-button` | Choice Button |
| `page-chips` | Chips |
| `page-tags` | Tags |
| `page-link` | Link Standalone |
| `page-text-fields` | Text Fields & Selects |
| `page-checkbox` | Check Box |
| `page-radio` | Radio |
| `page-switch` | Switch (Toggle) |
| `page-segmented-control` | Segmented Control |
| `page-stepper` | Stepper |
| `page-bottom-nav` | Bottom Navigation |
| `page-tabs` | Tabs |
| `page-date-tabs` | Date Tabs |
| `page-pagination` | Pagination |
| `page-toast` | Toast |
| `page-badge` | Badge |
| `page-progress` | Progress Indicators |
| `page-scrim` | Scrim |
| `page-modal` | Modal Dialog |
| `page-bottom-sheet` | Bottom Sheet |
| `page-date-picker` | Date Picker Calendar |
| `page-card` | Card (base) |
| `page-card-color-block` | Card — Color Block |
| `page-card-media` | Card — Media |
| `page-card-multi` | Card — Multifunctional |
| `page-list` | List |
| `page-list-accordion` | List Accordion |
| `page-avatar` | Avatar |
| `page-divider` | Divider |
| `page-icon-bullet` | Icon Bullet |
| `page-search-field` | Search Field |
| `page-top-nav-app` | Top Navigation App |
| `page-top-nav-web` | Top Navigation Web |
| `page-comp-overview` | Components Overview |
| `page-breakpoints` | Breakpoints & Grid (Foundations) |

### 🚧 Stub (In Progress pill, no content yet)
Foundation pages only: `page-style`, `page-icons`, `page-logo`, `page-photography`, `page-illustration`

---

## Global JS functions (defined ~line 19536)

**`initDropdown(el, onChange)`** — wires a `.dropdown` element. `el` is the root dropdown div. `onChange(value)` fires when an option is selected. Called from inline page `<script>` blocks.

**CRITICAL:** Page-level `<script>` blocks are parsed before the global script at line ~19536. Always wrap page init in `window.addEventListener('DOMContentLoaded', fn)` or the `initDropdown` call will throw a ReferenceError and kill all controls silently.

**`toggleCodeReveal(btn, id)`** — expand/collapse code snippet panels. Called inline via `onclick`.

**`wireProp(id, attr)`** — local pattern (defined inside each page's init), not global. Wires a checkbox toggle to set/remove a `data-no-[attr]` attribute on the preview phone mock. Unchecked = attribute present = property hidden.

**`initBreakpointsPreview()`** — local pattern (IIFE inside `#page-breakpoints`'s own `<script>` block), not global. Drives the Breakpoints & Grid page: binds the dropdown and the two `.bp-drag-handle` elements (`#bp-handle-l`/`#bp-handle-r`) to one shared `index` state (0–4, XS→XL) with free continuous drag via pointer capture on both edge handles, live px readout during drag, snap to the nearest tier only on pointer-up. (The drag mechanics were originally ported from `#top-nav-web`'s resize-handle logic — that page has since dropped its draggable stage entirely, see `initTnwPreview` below, but this page keeps its own copy since its 5 stops each represent a genuinely reachable pixel width, unlike top-nav-web's.) Candidate widths are each tier's representative width (375/768/1024/1440/1920) scaled by `min(1, getAvailW() / 1920)`, recomputed via `ResizeObserver` on `.bp-stage-outer` (deferred until the panel has real layout, since `page-panel` is `display:none` until active). The grid overlay's column count/margin/gutter scale by the same factor. `.bp-stage` itself reuses the `.tnw-desktop-shell` recipe exactly (14px radius, `--shadow-elevation-s`, no light-mode border — see DESIGN.md § 4, "The Device-Shell Consistency Rule"). Keyboard access to the 5 tiers is via the dropdown only (`initDropdown`'s existing arrow/enter/escape handling) — the drag handles are a pointer-only enhancement.

**`initTnwPreview()`** — local pattern (IIFE inside `#page-top-nav-web`'s own `<script>` block). Drives the Web Header page's preview — an S/M/L click toggle (no drag handles) that changes both the shell's width and the header's internal layout.

Two earlier approaches were tried and abandoned here — worth knowing before touching this again. First, a segmented control bound to the 5 Foundations breakpoint tiers (XS–XL) with draggable resize handles, snapping to their real pixel widths. That broke because this doc site's own content column caps at ~750–850px (`.page-panel{max-width:960px}` minus sidebar/padding) — nowhere close to M/L/XL's real widths (1024/1440/1920), so dragging could only ever visually reach XS/S, with a pixel readout that read identically for every larger tier. Second problem, worse: the header's actual layout-switching `@container` rules (see below) *also* never fire in this column — the real rendered width never gets anywhere near their 767px/1023px thresholds, so the header sat permanently in its narrowest layout no matter what was "selected." A second attempt kept the drag handles but tracked the drag's true unclamped width separately from the visually clamped display width, so dragging past the visible edge still registered as progress toward M/L — this fixed the snapping, but the resize handles themselves were still pointless UI once nothing past ~M ever visually moved. Neither problem was fixable by picking better numbers or better drag math — the column is just too narrow, permanently, regardless of monitor size.

Current approach: no drag handles — clicking S/M/L is a discrete, click-only jump, not a drag gesture. The control shows the component's own **3 Figma `Size=` variants (S/M/L)** instead of the 5 viewport-breakpoint tiers — a different axis entirely (see [Figma node 1497:4276](https://www.figma.com/design/gmjSnvSRO1Xb4WKwb4YXsv/unica-design-system?node-id=1497-4276)), same relationship as Button's `size=s/m/l` prop has to breakpoints — not meant to line up with XS–XL at all. `applyState(key)` does two independent things: sets `.tnw-desktop-shell`'s width (`STATE_WIDTH = {s:375, m:768, l:null}` — S/M are fixed representative widths matching the Foundations page's own convention; `l:null` means "fill `getAvailW()`", i.e. whatever the content column actually has, since a real ≥1024px L can never fit and claiming a specific number for it would be dishonest), and sets `data-tnw-force="s"|"m"|"l"` on `#tnw-mock` to drive the header's *internal* layout via CSS overrides (`#tnw-mock[data-tnw-force="..."] .tnw-*`, right after the two `@container` blocks) that hand-mirror what each `@container` rule would do — necessary because the real container can never get wide enough to trigger them itself regardless of the shell's own width. `L`'s override is just the base CSS restated (undoes both `@container` blocks); `M` mirrors the ≤1023px block; `S` mirrors both simultaneously (both are active together at any real width this narrow). These two effects are intentionally decoupled — the shell's pixel width and the header's layout state don't have to agree with what a real `@container` at that width would produce, since neither one is claiming to be a physically accurate live-resize; both play by their own explicit `STATE_WIDTH`/`data-tnw-force` mapping. No pixel readout — once "L" doesn't mean 1440px, a px counter is more misleading than informative. `ResizeObserver` on `.preview-canvas` re-applies the current state on resize (so L keeps tracking the column's real width, and S/M stay clamped via `Math.min(target, avail)` on narrow screens) and defers the very first `applyState` call until the panel has real layout (`page-panel` is `display:none` until active).

The "Breakpoints" static illustration section further down the same page (5 strips, `.tnw-variant-strip`, real ranges XS–XL) is unrelated to this control and unaffected by any of this — it's static markup, not live-rendered, so the column-width ceiling doesn't apply to it.

The two `@container` rules that document the header's *real* responsive contract for actual implementers (hamburger at ≤1023px, stacked search at ≤767px — see lines ~9376/9389) are untouched and still correct; only the interactive preview's ability to demonstrate them live is what's constrained. They stay literal numbers with an explanatory comment (CSS custom properties can't be used inside `@container`/`@media` conditions) — keep them in sync with `--breakpoint-s-max`/`--breakpoint-xs-max`, and keep the `data-tnw-force` overrides in sync with *them*, by hand, if either ever changes.

---

## SVG sprite (lines ~8155–8290)

All icons are `<symbol>` elements in a hidden `<svg>` at the top of `<body>`. Reference with `<use href="#ico-[name]"/>`.

### Currently defined symbols
`ico-unica`, `ico-fire`, `ico-heart`, `ico-leaf`, `ico-moon`, `ico-sun`, `ico-bulb`, `ico-bell`, `ico-message`, `ico-cloud`, `ico-arrow`, `ico-eye-show`, `ico-search`, `ico-x-sm`, `ico-x-circle`, `ico-caret-right`, `ico-caret-dn`, `ico-eye-hide`

### Icon rules
- All icons use `viewBox="0 0 24 24"`. Never change the viewBox.
- Set display size via `width`/`height` on the `<svg>` wrapper, not on `<use>`.
- All icons sourced from the **ůnica Figma icon set** (node 37:246). Never hand-draw paths.
- Fetch paths from: `https://raw.githubusercontent.com/Iconscout/unicons/master/svg/line/[name].svg`
- Exception: `ico-leaf` is a custom ůnica path (not in Unicons). Use the existing symbol.
- `ico-caret-dn` points down at rest; CSS rotates it 180° when open (`transform: rotate(180deg)`).

---

## Accordion component — technical details

**CSS classes:**
- `.list-accordion` — root wrapper
- `.list-accordion__header` — `<button>`, carries `aria-expanded` and `aria-controls`
- `.list-accordion__control` — 40×40px chevron button container
- `.list-accordion__control-inner` — animated inner (background + border-radius change on hover/pressed)
- `.list-accordion__chevron` — the SVG icon, rotates on open
- `.list-accordion__body` — grid height container (`grid-template-rows: 0fr → 1fr`)
- `.list-accordion__body-inner` — `overflow: hidden` (required for grid-rows trick)
- `.list-accordion__body-text` — padding: `0 space-400 space-500` (no left indent)
- `.list-accordion__divider` — separator line below each item

**Hover/pressed state:** Only the `__control-inner` element shows state, not the full row.
- Hover: `background: color-action-hover-subtle; border-radius: corner-radius-m`
- Pressed: `background: color-action-active-subtle; border-radius: corner-radius-round; transform: scale(0.96)`
- **Persists when open:** `aria-expanded="true"` on the header triggers the hover background on `__control-inner`

**Directional animation (MUST use this pattern):**
```javascript
if (expanding) {
  body.style.transition = 'grid-template-rows 350ms cubic-bezier(0.16, 1, 0.3, 1)'; // ease-out-expo
  body.classList.add('is-open');
} else {
  accordion.classList.add('is-closing');
  body.style.transition = 'grid-template-rows 200ms cubic-bezier(0.4, 0, 1, 1)'; // ease-in
  body.classList.remove('is-open');
}
// Clean up inline style + is-closing on transitionend
```
The `is-closing` class also swaps the chevron's CSS transition curve for the rotation animation.

---

## CSS patterns used throughout

### Phone preview shell
```css
.xxx-phone-shell {
  width: 375px;
  background: var(--color-background-page);
  border-radius: 24px;
  box-shadow: 0 1px 8px 0 rgba(8,5,13,0.25);
  overflow: hidden;
}
[data-theme="dark"] .xxx-phone-shell {
  box-shadow: none;
  border: var(--border-width-default) solid var(--color-border-default);
}
```

### Preview controls placement
Controls (dropdowns, toggles) always go in `.btn-controls` **between the `<hr class="doc-rule">` and the preview wrapper** — never inside the colored preview area.

### Optional property toggles
Use `.card-prop-bar` below the preview canvas with `toggle-switch--small` checkboxes. Unchecked = property hidden. Always use `data-no-[prop]` on the phone mock root and CSS selectors like `#mock[data-no-leading] .leading { display: none; }`.

### Variants grid (2-col, responsive)
```html
<div class="bs-variants-grid">
  <div class="bs-variant-item">
    <p class="avatar-group-label">Label</p>
    <!-- component -->
  </div>
</div>
```
`bs-variants-grid`: `grid-template-columns: 1fr 1fr; gap: space-500; max-width: 760px`. Collapses to 1 column at ≤640px. Use this for Default/Open, or any 2-variant side-by-side display.

### Full-width states grid
For components that span full width (list items, accordions): use `.ls-states-grid.ls-states-grid--5col` → 5 columns at desktop, 2 at tablet, 1 at mobile. Each cell is `.ls-state-item` with an `.avatar-group-label` (margin:0) above a `.la-cell-wrap`.

### Dropdown layout rule
All dropdowns use **horizontal inline layout** — icon/dot + text on one line. `display: flex; align-items: center; gap: 6px` on option and trigger. Width always hugs content.

### Section labels
Always `class="avatar-group-label"` for variant/state tile labels. Never invent a new label class.

---

## Token quick reference

```css
/* Brand */
--color-brand-ink            /* near-black #1F182E */
--color-brand-ultraviolet    /* accent purple #8955F2 */
--primitive-cafe-200         /* signature cream #F2EFED */

/* Most-used semantic tokens */
--color-background-page      /* page surface */
--color-background-subtle    /* slightly elevated surface */
--color-background-selection /* hover/selected bg */
--color-content-default      /* primary text */
--color-content-subtle       /* secondary text */
--color-border-default       /* standard border */
--color-border-subtle        /* lighter border */
--color-action-hover-subtle  /* hover state bg */
--color-action-active-subtle /* pressed state bg */

/* Spacing scale — verified against tokens/tokens.css and Figma (2026-08-19); all 14 steps match exactly */
--space-100: 4px   --space-200: 8px   --space-300: 12px  --space-400: 16px
--space-500: 24px  --space-600: 32px  --space-700: 40px  --space-800: 48px
--space-900: 56px  --space-1000: 64px --space-1100: 72px --space-1200: 80px
--space-1300: 88px --space-1400: 96px

/* Breakpoints (Layout/Breakpoint/* in Figma) */
--breakpoint-xs-min: 360px  --breakpoint-xs-max: 767px
--breakpoint-s-min:  768px  --breakpoint-s-max:  1023px
--breakpoint-m-min:  1024px --breakpoint-m-max:  1439px
--breakpoint-l-min:  1440px --breakpoint-l-max:  1919px
--breakpoint-xl-min: 1920px

/* Grid — columns / margin / gutter (Grid/XS…XL styles in Figma) */
--grid-xs-columns: 4  --grid-xs-margin: 16px --grid-xs-gutter: 16px
--grid-s-columns:  8  --grid-s-margin:  24px --grid-s-gutter:  24px
--grid-m-columns:  12 --grid-m-margin:  32px --grid-m-gutter:  24px
--grid-l-columns:  12 --grid-l-margin:  48px --grid-l-gutter:  24px
--grid-xl-columns: 12 --grid-xl-margin: 64px --grid-xl-gutter: 24px

/* Shape */
--corner-radius-m      /* medium rounding */
--corner-radius-l      /* large rounding */
--corner-radius-round  /* pill / full round */

/* Type */
--font-family-sans: 'Inter', sans-serif
--font-family-serif: 'Unna', Georgia, serif
--font-weight-semibold: 600
```

---

## Doc page structure template

Every component page follows this structure:
```html
<div class="page-panel" id="page-[name]">
  <!-- 1. Component header -->
  <div class="comp-header">
    <p class="comp-eyebrow">Components · Category</p>
    <h1 class="comp-title">Component Name</h1>
    <p class="comp-description">One sentence.</p>
    <div class="comp-badges">...</div>
  </div>

  <!-- 2. Preview section -->
  <div class="doc-section">
    <h2 class="doc-section-title">Preview</h2>
    <hr class="doc-rule">
    <div class="btn-controls"><!-- dropdowns --></div>
    <div class="xxx-wrap"><!-- phone shell / preview --></div>
    <div class="card-prop-bar"><!-- optional property toggles --></div>
  </div>

  <!-- 3. Code reveal -->
  <button class="code-reveal-btn" ...>Show code</button>
  <div class="code-reveal" hidden>...</div>

  <!-- 4. Variants & States -->
  <div class="doc-section">
    <h2 class="doc-section-title">Variants &amp; States</h2>
    ...
  </div>

  <!-- 5. Accessibility table -->
  <div class="doc-section">
    <h2 class="doc-section-title">Accessibility</h2>
    ...
  </div>

  <!-- 6. Page script (MUST be in DOMContentLoaded) -->
  <script>
  window.addEventListener('DOMContentLoaded', function() {
    (function initXxxPreview() { ... })();
  });
  </script>
</div>
```

---

## Design principles (never compromise these)

Elona is a design leader with 12+ years experience building design systems at CVS Health, connectRN, athenahealth, and Care.com. The bar is **world-class pixel-perfection**. Every decision traces back to two principles:

1. **Enduring.** Timeless over trendy. No decorative excess. Every element earns its place.
2. **Precise.** Spacing is sacred. Every typographic relationship is deliberate. Swiss School rigor.

References: Dieter Rams ("Less, but better"), Josef Albers lineage, editorial fashion photography (Vogue, Dazed & Confused).

**Aesthetic:** Warm cream/apricot neutrals. Moments of expressive color (violet, ultraviolet, berry, mint). Unna for editorial display moments. Inter for UI precision.

---

## What NOT to do

- ❌ Never split index.html into multiple files
- ❌ Never hand-draw SVG icon paths — always fetch from ůnica sprite or Unicons
- ❌ Never call `initDropdown()` at parse time — always wrap in `DOMContentLoaded`
- ❌ Never add a left-indent to `.list-accordion__body-text` — padding is `0 space-400 space-500` (uniform horizontal)
- ❌ Never use `getNodeById()` in Figma execute scripts — use `await figma.getNodeByIdAsync()`
- ❌ Never place Figma components on blank canvas — always inside a Section or Frame
- ❌ Never add `ico-caret-dn` to references without confirming it's defined in the sprite (it now is, at line ~8235)
- ❌ Never create new label classes for variant tiles — use `.avatar-group-label`
- ❌ Never add a `states-matrix` for full-width components — use `ls-states-grid` instead

---

## Reference pages for patterns

| Pattern needed | Look at |
|---|---|
| Phone preview + prop toggles | `#page-list`, `#page-list-accordion` |
| States matrix (button-sized) | `#page-button`, `#page-date-picker` |
| Full-width states grid | `#page-list`, `#page-list-accordion` |
| 2-col variants grid (bs-variants-grid) | `#page-bottom-sheet`, `#page-list-accordion` |
| Dropdown wiring with DOMContentLoaded | `#page-list-accordion` (script block ~line 18430) |
| Desktop browser chrome shell | `#page-modal`, `#page-scrim` |
| Dark mode logo swap | `#page-progress` |
