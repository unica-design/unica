---
name: ůnica Design System
description: Precision crafted design — Swiss-grid rigor and warm editorial craft, proven with an engineer's states table.
colors:
  ultraviolet: "#8955F2"
  berry: "#FC97B9"
  mint: "#04D995"
  pool: "#003330"
  citron: "#DBEB76"
  violet: "#D9C8FA"
  apricot: "#F79257"
  ink: "#0F1726"
  ink-hover: "#2E384D"
  cream: "#F2EFED"
  section-white: "#FCF9F7"
  page-white: "#FFFFFF"
typography:
  display:
    fontFamily: "Unna, Georgia, serif"
    fontSize: "64px"
    fontWeight: 400
    lineHeight: "64px"
    letterSpacing: "-0.03em"
  headline:
    fontFamily: "Unna, Georgia, serif"
    fontSize: "48px"
    fontWeight: 400
    lineHeight: "56px"
    letterSpacing: "-0.02em"
  title:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "24px"
    fontWeight: 600
    lineHeight: "28px"
  body:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: "22px"
  label:
    fontFamily: "Inter, system-ui, -apple-system, sans-serif"
    fontSize: "12px"
    fontWeight: 600
    letterSpacing: "0.08em"
rounded:
  square: "0px"
  xxs: "4px"
  xs: "8px"
  s: "12px"
  m: "16px"
  l: "24px"
  xl: "32px"
  round: "9999px"
spacing:
  "100": "4px"
  "200": "8px"
  "300": "12px"
  "400": "16px"
  "500": "24px"
  "600": "32px"
  "800": "48px"
  "1000": "64px"
components:
  button-filled:
    backgroundColor: "{colors.ink}"
    textColor: "{colors.page-white}"
    rounded: "{rounded.round}"
    padding: "0 16px"
    height: "48px"
  button-filled-hover:
    backgroundColor: "{colors.ink-hover}"
    rounded: "{rounded.m}"
  button-outlined:
    backgroundColor: "transparent"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    padding: "0 16px"
    height: "48px"
  chip-default:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.round}"
    padding: "0 14px"
    height: "32px"
  text-field:
    backgroundColor: "{colors.page-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.m}"
    padding: "0 16px 0 12px"
    height: "48px"
---

# Design System: ůnica

## 1. Overview

**Creative North Star: "The Precision Atelier"**

ůnica is a working studio, not a sterile lab: Swiss-grid rigor and warm editorial craft share a bench. Every page opens with a component treated like an object worth photographing — generous whitespace, an Unna-serif title set like a magazine dek — then backs that up with an engineer's proof: full states matrices, exhaustive prop tables, real accessibility callouts. Neither half is decoration for the other; a component page that only looked good would fail the brief as surely as one that only worked.

The palette is warm by choice, not by default. Café (the signature cream, `#F2EFED`) is the system's home surface — a considered departure from stark white, not the flattened "SaaS-cream" of a default AI neutral. Against that warmth, a small set of expressive colors (Ultraviolet, Berry, Mint, Pool, Citron, Violet, Apricot) appear as moments, not backgrounds. This is explicitly not a generic docs-site template (Material/GitBook/Docusaurus default), not glassmorphism or gradient-driven decoration, and not stark soulless minimalism — restraint here carries warmth, it doesn't erase it.

**Key Characteristics:**
- Warm cream (`#F2EFED`) as signature surface, white as the true page floor
- Unna serif for editorial display moments; Inter for everything functional
- Buttons and controls that change *shape*, not elevation, to signal state
- A small, named set of expressive brand colors — never a rainbow, never absent
- Documentation depth (states, a11y, props) treated as a visual-quality requirement, not an afterthought

## 2. Colors

The palette reads as warm neutrals doing the daily work, with a disciplined set of eight named brand colors reserved for moments of expression and system feedback.

### Primary
- **Ultraviolet** (`#8955F2`): the system's single standout accent — interactive/focus emphasis (`--color-border-interactive`), and the one color in the set that isn't derived from a 10-step primitive ramp. Its rarity is what makes it read as a signature rather than a UI color.

### Secondary
- **Berry** (`#FC97B9`, brand token drawn from Berry-400): warm pink-magenta, used for expressive/decorative moments and the danger/error color family at deeper steps.

### Tertiary
- **Mint** (`#04D995`, Mint-500): fresh green, used for success feedback and as an expressive accent alongside Berry and Ultraviolet.
- **Pool** (`#003330`, drawn from the deepest Pool-1000 step — deliberately dark, not mid-tone), **Citron** (`#DBEB76`, Citron-300), **Violet** (`#D9C8FA`, Violet-300), **Apricot** (`#F79257`, Apricot-500): the extended expressive family. Each is a full 10-step primitive ramp (100–1000); only one representative step is promoted to a named brand token, and that promoted step varies deliberately by color (Ink and Pool use their darkest step; Berry, Mint, Citron, Violet, Apricot use lighter-to-mid steps) rather than following a single mechanical rule.

### Neutral
- **Ink** (`#0F1726`): primary content and default-action color. Cool near-black, not warm — despite the warm palette around it, text itself stays crisp and legible.
- **Ink Hover** (`#2E384D`): the one-step-lighter hover state for filled ink surfaces (buttons, primary actions).
- **Cream** (`#F2EFED`, Café-200): the signature container/section surface — this is the color that makes ůnica feel like ůnica. Used for elevated containers and card backgrounds, not the page floor itself.
- **Section White** (`#FCF9F7`, Café-100): a near-white step between true white and signature cream, used for section backgrounds that sit above the page but below a fully "creamed" container.
- **Page White** (`#FFFFFF`): the true page background in light mode. Cream is reserved for surfaces that sit *on* the page, not the page itself.

### Named Rules
**The Considered Cream Rule.** Cream (`#F2EFED`) is a chosen brand color, not a default neutral — it must always read as deliberate warmth, never as an undifferentiated off-white. If a surface could be swapped for generic "AI cream" without anyone noticing, it's being used wrong.

**The Rarity Rule.** Ultraviolet appears sparingly — as a focus/interactive signal, not a fill color. If it's covering more than a small fraction of any given screen, it has stopped being a signature and started being decoration.

## 3. Typography

**Display Font:** Unna (with Georgia, serif fallback)
**Body Font:** Inter (with system-ui, -apple-system, sans-serif fallback)

**Character:** Unna carries every editorial, headline-scale moment — page titles, hero numerals, the type-scale showcase itself — with warmth and a slight literary weight. Inter handles everything functional: body copy, labels, controls, code. The pairing is a deliberate contrast axis (serif display / sans body), never blended within the same text run.

### Hierarchy
- **Display** (400, 64px / 64px line-height, -0.03em, Unna): reserved for true hero scale — the type foundation showcase and largest editorial moments.
- **Headline** (400, 48px / 56px, -0.02em, Unna): component page titles (`.comp-title`) and section-level editorial headings. This is the size most visitors actually see most often — it's the system's real "front door" typography.
- **Title** (600, 24px / 28px, Inter): sub-section headings, card titles, dialog titles.
- **Body** (400, 16px / 22px, Inter): default running text and UI copy; cap prose at 65–75ch.
- **Label** (600, 12px, 0.08em tracking, uppercase, Inter): the `.comp-eyebrow` category breadcrumb ("Components · Actions") that sits above every page title, and small metadata/status text throughout.

### Named Rules
**The Serif-Is-Earned Rule.** Unna only appears at headline scale and above (≥48px), or as a deliberate editorial flourish (e.g. the stepper's serif numeral). It never sets body copy, labels, or UI chrome — the contrast between the two families is the point, and diluting it into small sizes collapses the hierarchy.

**The Eyebrow-Is-a-Breadcrumb Rule.** The uppercase tracked label above each component title is a taxonomy breadcrumb ("Components · Actions"), not a decorative kicker — it always carries real category information. It is not to be added above sections purely as rhythm or scaffolding.

## 4. Elevation

ůnica is flat by default; shape carries state instead of shadow. The three-step shadow scale (`--shadow-elevation-xs/s/l`, all built from the same ink-tinted shadow color at increasing blur/spread) exists for genuinely floating surfaces — the sticky site header, modals, dropdowns, popovers — not for everyday cards or containers, which stay flat and rely on the cream/white surface contrast for separation. Interactive elements (buttons, chips) communicate hover and press through a corner-radius morph and a 4% scale change, not through added shadow.

### Shadow Vocabulary
- **elevation-xs** (`0 0 4px rgba(8,5,13,0.25)`, dark mode `0.60`): the lightest touch — used behind the sticky header alongside a 1px border for hairline separation from content.
- **elevation-s** (`0 1px 8px rgba(8,5,13,0.25)`, dark mode `0.60`): standard floating-surface shadow — phone/desktop preview shells, dropdown menus.
- **elevation-l** (`0 2px 24px rgba(8,5,13,0.25)`, dark mode `0.70`): the deepest shadow, reserved for modal dialogs and the highest-priority overlays.

### Named Rules
**The Shape-Not-Shadow Rule.** A button's rest state is a full pill (`--corner-radius-round`); on hover it softens toward `--corner-radius-m`; on press it snaps back to a pill and scales to 0.96. State is legible from silhouette alone — never bolt on a hover shadow as a substitute for this morph.

**The Dark-Mode Border Swap Rule.** Any shell that uses `box-shadow` for separation in light mode (phone/desktop preview shells, cards) switches to `box-shadow: none` plus a solid 1px border in dark mode — shadows don't read against a dark background the way borders do.

**The Device-Shell Consistency Rule.** Every preview surface that represents a device or browser frame (phone mock, desktop/browser shell, responsive-preview stage) reuses the same shell recipe — never a one-off stroke or radius invented per component. Canonical reference: [Top Navigation — Web](https://unica-design.github.io/unica/#top-nav-web) (`.tnw-desktop-shell`).
- Light mode: `border-radius: 14px` (desktop/browser shells) or `24px` (phone shells); `box-shadow: 0 1px 8px 0 rgba(8,5,13,0.25)` (`--shadow-elevation-s`); **no border.**
- Dark mode: `box-shadow: none`; `border: var(--border-width-default) solid var(--color-border-default)`; radius unchanged.
- Never combine a border with a shadow in the same mode, and never substitute a different radius or a stroke-only treatment "for variety" — a new preview shell should look like a sibling of the existing ones, not a new pattern.

## 5. Components

### Buttons
- **Shape:** full pill at rest (`border-radius: 9999px`); morphs to `--corner-radius-m` (16px, or `--corner-radius-s`/12px for the small size) on hover; returns to a pill and scales to 0.96 on press.
- **Filled (primary):** `background: var(--color-action-default)` (ink), `color: var(--color-inverse)` (white). Hover darkens to `--color-action-hover` (ink-800, `#2E384D`); disabled swaps to a neutral disabled background with a 1.5px border.
- **Outlined:** transparent background, 1.5px ink-strength border, ink text. Hover fills with a subtle translucent ink tint (`--color-action-hover-subtle`, 8% opacity) rather than a solid color change.
- **Reversed suite:** every filled/outlined style has a `-reversed` counterpart for use on dark surfaces (inverts action/content tokens), plus a Super CTA variant reserved for high-emphasis, conversion-sensitive moments.
- **Sizes:** Large/Medium share 48px/40px heights at 16px horizontal padding; Small is 32px at 12px padding. Icon-only variants go square (width = height, no horizontal padding).

### Chips
- **Style:** pill shape, 32px height, 1.5px border in the default resting state, page-white background, 14px horizontal padding, 500-weight label text.
- **State:** unselected chips get a subtle background shift on hover/active; selected/toggled chips (`aria-pressed="true"`) double the border weight and pick up a tinted background. A `--strong` selected variant inverts to a solid ink fill with page-bg text instead of the tinted border treatment — reserved for filter/toggle contexts where selection needs to read at a glance.

### Text Fields
- **Style:** 48px height, `--corner-radius-m` (16px), 1px default border in `--color-border-default`, white background, 12–16px asymmetric horizontal padding (12px leading, 16px trailing) to balance an inline leading icon.
- **Focus/typing:** border thickens to `--border-width-strong` (1.5px) and darkens to `--color-border-strong` — no glow, no color-family change, just weight and contrast.
- **Error:** same thickened border treatment, but in the danger color family. **Disabled:** background shifts to the disabled surface token; border and text both mute.

### Navigation
- **Site header:** sticky, page-white background, a hairline bottom border plus `elevation-xs` shadow for separation as content scrolls beneath it. Wordmark set at 36px, weight 300, Inter (not Unna) — a deliberately light-weight sans treatment for the logotype, distinct from the serif used for content headlines.
- **Sidebar / doc nav:** category-grouped, uses the same label typography (12px, uppercase, 0.08em tracking) as the eyebrow breadcrumb for section headers.

### Documentation Chrome (signature pattern)
The doc-page template is itself a designed component, not scaffolding: `comp-header` (eyebrow breadcrumb → Unna headline → body description → capability badges) always precedes a `Preview` section with inline controls, a collapsible `</> Show code` reveal, a `Variants & States` section, and a closing `Accessibility` table. Two-column variant comparisons always use the `bs-variants-grid` pattern (max-width 760px, collapses to one column ≤640px); full-width component states (list rows, accordions) use a 5-column `ls-states-grid` instead of a boxed states matrix. Every variant/state tile label uses the same small-caps `avatar-group-label` class — never a bespoke label style per component.

## 6. Do's and Don'ts

### Do:
- **Do** treat Cream (`#F2EFED`) as a deliberate, named brand color — describe it and use it as "signature cream," never as a generic neutral.
- **Do** let interactive elements change shape (corner-radius morph + scale) to signal hover/press, before reaching for a shadow or color change.
- **Do** reserve Unna serif for headline scale (≥48px) and genuine editorial flourishes; keep every functional and small-scale text in Inter.
- **Do** pair every visual flourish with documentation rigor — a states matrix, an accessibility table, real prop coverage. A beautiful page with thin documentation fails the brief.
- **Do** use the eyebrow label only as a real taxonomy breadcrumb ("Components · Actions"), carrying genuine category information.

### Don't:
- **Don't** default to "SaaS-cream AI slop" — a warm sand/cream background used because it's the safe 2026 default rather than because it's *this* brand's considered cream. If the surface could be swapped for generic AI neutral without anyone noticing, it's wrong.
- **Don't** reach for glassmorphism, heavy gradients, or bouncy/elastic motion — anything optimized to look striking today and dated in two years is explicitly rejected (per PRODUCT.md's anti-references).
- **Don't** default to generic docs-site chrome (Material/GitBook/Docusaurus look-alikes) — the documentation shell itself is a designed component, not off-the-shelf scaffolding.
- **Don't** ship stark, personality-free minimalism — restraint here is edited, not empty; it must still carry the cream/ink warmth.
- **Don't** add a colored `border-left`/`border-right` stripe as a decorative accent on any card, list item, or callout.
- **Don't** invent a new label class for variant/state tiles — always `avatar-group-label`.
- **Don't** use a boxed states matrix for full-width components (list rows, accordions) — use the `ls-states-grid` pattern instead.
- **Don't** add a left indent to accordion body text or otherwise deviate from the established uniform horizontal padding pattern without a documented reason.
