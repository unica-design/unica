#!/usr/bin/env python3
"""
Component tiles v3: category bg + corner shapes (no center shape) +
actual component rendered at natural size in the center.
Inspired by Pinterest Gestalt / Material 3 overview style.
"""

import re

FILE = '/Users/elona/ůnica/Claude/index.html'

# ─── Shape paths ─────────────────────────────────────────────────────────────
FLOR     = "M65 240C85.8858 240 104.471 230.149 116.363 214.841C118.166 212.519 121.834 212.519 123.637 214.841C135.529 230.149 154.114 240 175 240C210.898 240 240 210.898 240 175C240 154.114 230.149 135.529 214.841 123.637C212.519 121.834 212.519 118.166 214.841 116.363C230.149 104.471 240 85.8858 240 65C240 29.1015 210.898 0 175 0C154.114 0 135.529 9.85068 123.637 25.1595C121.834 27.4812 118.166 27.4812 116.363 25.1595C104.471 9.85068 85.8858 0 65 0C29.1015 0 0 29.1015 0 65C0 85.8858 9.85068 104.471 25.1595 116.363C27.4812 118.166 27.4812 121.834 25.1595 123.637C9.85068 135.529 0 154.114 0 175C0 210.898 29.1015 240 65 240Z"
CUSHION  = "M224.712 104.04C219.768 114.072 219.768 125.928 224.712 135.96C243.408 173.976 245.76 208.872 227.304 227.304C208.872 245.76 173.976 243.408 135.96 224.712C125.928 219.768 114.072 219.768 104.04 224.712C66.024 243.408 31.128 245.76 12.696 227.304C-5.76 208.872 -3.408 173.976 15.288 135.96C20.232 125.928 20.232 114.072 15.288 104.04C-3.408 66.024 -5.76 31.128 12.696 12.696C31.128 -5.76 66.024 -3.408 104.04 15.288C114.072 20.232 125.928 20.232 135.96 15.288C173.976 -3.408 208.872 -5.76 227.304 12.696C245.76 31.128 243.408 66.024 224.712 104.04Z"
SUNBURST = "M107.232 3.528C115.08 -1.176 124.896 -1.176 132.768 3.528L155.328 16.968C158.208 18.648 161.496 19.392 164.76 19.128L191.232 16.92C200.232 16.176 208.944 20.592 213.648 28.296L227.088 50.832C228.768 53.712 231.216 56.064 234.12 57.648L257.856 69.984C265.872 74.16 270.576 82.656 270.072 91.68L268.392 118.2C268.2 121.464 268.992 124.728 270.696 127.584L284.736 149.784C289.632 157.656 289.272 167.616 284.184 175.104L270.504 197.064C268.8 199.92 267.984 203.208 268.128 206.472L269.28 232.992C269.712 242.016 265.2 250.56 257.424 254.712L233.4 267.312C230.52 268.896 228.096 271.224 226.392 274.08L212.976 296.256C208.248 303.984 199.632 308.4 190.608 307.656L164.136 305.376C160.896 305.112 157.608 305.88 154.752 307.536L132.192 320.976C124.344 325.68 114.528 325.68 106.656 320.976L84.096 307.536C81.24 305.856 77.952 305.112 74.712 305.376L48.24 307.656C39.216 308.4 30.576 303.984 25.872 296.256L12.456 274.08C10.752 271.2 8.304 268.872 5.448 267.312L-18.576 254.712C-26.352 250.56 -30.864 242.016 -30.432 232.992L-29.28 206.472C-29.136 203.208 -29.952 199.92 -31.656 197.064L-45.336 175.104C-50.424 167.592 -50.784 157.656 -45.888 149.784L-31.848 127.584C-30.144 124.728 -29.352 121.44 -29.544 118.2L-31.224 91.68C-31.728 82.656 -27.024 74.136 -19.008 69.984L4.728 57.648C7.608 56.064 9.984 53.736 11.616 50.832L25.056 28.296C29.784 20.568 38.376 16.176 47.376 16.92L73.848 19.128C77.112 19.392 80.424 18.648 83.28 16.968L107.232 3.528Z"
LEAF     = "M240 0H60C26.863 0 0 26.863 0 60V240H180C213.137 240 240 213.137 240 180V0Z"
MOD      = "M31.992 0C14.328 0 0 14.328 0 31.992V88.008C0 97.488 3.864 106.56 10.776 113.136L113.136 213.24C126.888 226.512 126.888 248.136 113.136 261.408L68.424 305.208C54.672 318.48 54.672 340.104 68.424 353.376L90.312 374.712C103.944 387.864 125.448 388.368 139.656 375.744L150.456 366.096C163.848 354.168 164.376 333.456 151.584 320.88L143.496 312.936C135.528 305.064 135.528 292.128 143.496 284.256L229.224 200.16C236.112 193.488 240 184.32 240 174.84V31.992C240 14.328 225.672 0 207.984 0H31.992Z"
MONDRIAN = "M190.008 31.992C190.008 14.328 175.68 0 157.992 0H31.992C14.328 0 0 14.328 0 31.992V157.992C0 175.68 14.328 190.008 31.992 190.008H52.008C65.256 190.008 76.008 200.76 76.008 214.008V388.008C76.008 405.672 90.336 420 108 420H159.984C177.648 420 191.976 405.672 191.976 388.008V358.008C191.976 344.76 202.728 334.008 215.976 334.008H388.008C405.672 334.008 420 319.68 420 301.992V214.008C420 200.76 430.752 190.008 444 190.008H484.008C501.672 190.008 516 175.68 516 158.016V31.992C516 14.328 501.672 0 484.008 0H238.008C220.344 0 205.992 14.328 205.992 31.992H190.008Z"

SHAPES = [FLOR, CUSHION, SUNBURST, LEAF, MOD, MONDRIAN]

CATS = {
    'button': 'actions', 'choice-button': 'actions', 'chips': 'actions',
    'tags': 'actions', 'link': 'actions',
    'text-fields': 'inputs', 'checkbox': 'inputs', 'radio': 'inputs',
    'switch': 'inputs', 'segmented-control': 'inputs', 'stepper': 'inputs', 'search-field': 'inputs',
    'bottom-nav': 'nav', 'tabs': 'nav', 'date-tabs': 'nav', 'pagination': 'nav',
    'top-nav-app': 'nav', 'top-nav-web': 'nav',
    'toast': 'feedback', 'badge': 'feedback', 'progress': 'feedback',
    'scrim': 'feedback', 'modal': 'feedback', 'bottom-sheet': 'feedback',
    'avatar': 'display', 'card': 'display', 'card-color-block': 'display',
    'card-media': 'display', 'card-multi': 'display', 'list': 'display',
    'list-accordion': 'display', 'date-picker': 'display', 'divider': 'display', 'icon-bullet': 'display',
}

TILE_ORDER = [
    'button', 'choice-button', 'chips', 'tags', 'link',
    'text-fields', 'checkbox', 'radio', 'switch', 'segmented-control', 'stepper', 'search-field',
    'bottom-nav', 'tabs', 'date-tabs', 'pagination', 'top-nav-app', 'top-nav-web',
    'toast', 'badge', 'progress', 'scrim', 'modal', 'bottom-sheet',
    'avatar', 'card', 'card-color-block', 'card-media', 'card-multi',
    'list', 'list-accordion', 'date-picker', 'divider', 'icon-bullet',
]
SHAPE_IDX = {t: i % 6 for i, t in enumerate(TILE_ORDER)}

# ─── Checkbox + radio path ────────────────────────────────────────────────────
CHK = 'M9.44038 0.240068C9.72214 -0.0635401 10.1963 -0.0817123 10.5 0.200029C10.8034 0.481649 10.8213 0.955964 10.54 1.2596L4.5146 7.75179L3.97456 8.33382L3.42378 7.76155L0.208937 4.41585C-0.0778684 4.11718 -0.0681694 3.64225 0.230422 3.3553C0.529095 3.0685 1.00403 3.0782 1.29097 3.37679L3.95503 6.14925L6.42769 3.48616L9.44038 0.240068Z'

def chk_span(checked=True):
    state = ' checked' if checked else ''
    return (
        f'<span class="checkbox"><input type="checkbox"{state} tabindex="-1">'
        '<span class="checkbox-box">'
        f'<svg class="checkbox-check" viewBox="0 0 10.7398 8.33382" fill="none"><path d="{CHK}" fill="currentColor"/></svg>'
        '<span class="checkbox-dash"></span>'
        '</span></span>'
    )

def radio_span(checked=True):
    state = ' checked' if checked else ''
    return (
        f'<span class="radio"><input type="radio"{state} tabindex="-1">'
        '<span class="radio-circle"><span class="radio-dot"></span></span></span>'
    )

# ─── Component HTML per tile ──────────────────────────────────────────────────
# Style: natural size, real CSS classes, 1 instance, minimal text, centered
# Shadow lifts component off the colored bg. pointer-events:none throughout.

COMPS = {

# ── ACTIONS ───────────────────────────────────────────────────────────────────

# Button: two stacked buttons (filled + outlined) — shows the hierarchy
'button': (
    '<div style="display:flex;flex-direction:column;gap:10px;align-items:center;pointer-events:none;">'
    '<button class="btn btn-filled" tabindex="-1">'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><use href="#ico-fire"/></svg>'
    'Get started</button>'
    '<button class="btn btn-outlined" tabindex="-1">Learn more</button>'
    '</div>'
),

# Choice button: one selected vertical choice-btn with avatar
'choice-button': (
    '<div style="display:flex;gap:10px;pointer-events:none;">'
    '<div class="choice-btn choice-btn--vertical" aria-pressed="true" tabindex="-1" style="min-width:72px;">'
    '<div class="choice-btn-accessory">'
    '<div class="avatar avatar--medium avatar--circle" style="background:var(--primitive-violet-200);color:var(--color-content-default);font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;">EJ</div>'
    '</div>'
    '<div class="choice-btn-label">Owner</div>'
    '</div>'
    '<div class="choice-btn choice-btn--vertical" aria-pressed="false" tabindex="-1" style="min-width:72px;">'
    '<div class="choice-btn-accessory">'
    '<div class="avatar avatar--medium avatar--circle" style="background:var(--color-background-subtle);color:var(--color-content-subtle);font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;">TM</div>'
    '</div>'
    '<div class="choice-btn-label">Member</div>'
    '</div>'
    '</div>'
),

# Chips: a row of chips, one selected
'chips': (
    '<div style="display:flex;flex-direction:column;gap:8px;pointer-events:none;">'
    '<div style="display:flex;gap:6px;">'
    '<button class="chip chip--selected" aria-pressed="true" tabindex="-1">Design</button>'
    '<button class="chip" tabindex="-1">Research</button>'
    '<button class="chip" tabindex="-1">Dev</button>'
    '</div>'
    '<div style="display:flex;gap:6px;">'
    '<button class="chip" tabindex="-1">Strategy</button>'
    '<button class="chip chip--selected" aria-pressed="true" tabindex="-1">Brand</button>'
    '</div>'
    '</div>'
),

# Tags: 3 tags in different semantic states
'tags': (
    '<div style="display:flex;flex-direction:column;gap:8px;align-items:flex-start;pointer-events:none;">'
    '<span class="tag tag--success">Shipped</span>'
    '<span class="tag tag--warning">In review</span>'
    '<span class="tag tag--emphasis">New</span>'
    '</div>'
),

# Link: standalone link with arrow
'link': (
    '<div style="pointer-events:none;display:flex;flex-direction:column;gap:10px;">'
    '<a class="link link--large" tabindex="-1" style="pointer-events:none;display:inline-flex;align-items:center;gap:6px;">'
    'View documentation'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none"><use href="#ico-arrow"/></svg>'
    '</a>'
    '<a class="link" tabindex="-1" style="pointer-events:none;display:inline-flex;align-items:center;gap:5px;">'
    'See all examples'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><use href="#ico-arrow"/></svg>'
    '</a>'
    '</div>'
),

# ── INPUTS ────────────────────────────────────────────────────────────────────

# Text field: focused field with label + helper
'text-fields': (
    '<div style="width:180px;pointer-events:none;">'
    '<div class="tf-wrap">'
    '<label class="tf-label" style="pointer-events:none;">Email address</label>'
    '<div class="tf-ifield tf-ifield--focused">'
    '<input class="tf-iinput" type="email" placeholder="name@studio.com" tabindex="-1" style="pointer-events:none;">'
    '</div>'
    '</div>'
    '</div>'
),

# Checkbox: 3 rows
'checkbox': (
    '<div style="display:flex;flex-direction:column;gap:10px;pointer-events:none;">'
    + ''.join(
        f'<label style="display:inline-flex;align-items:center;gap:10px;cursor:default;">'
        f'{chk_span(i==0 or i==1)}'
        f'<span style="font-size:14px;font-family:var(--font-family-sans);color:var(--color-content-{"default" if i<2 else "subtle"});">{label}</span>'
        f'</label>'
        for i, label in enumerate(['Notifications', 'Weekly digest', 'Promotions'])
    )
    + '</div>'
),

# Radio: 3 options, first selected
'radio': (
    '<div style="display:flex;flex-direction:column;gap:10px;pointer-events:none;">'
    + ''.join(
        f'<label style="display:inline-flex;align-items:center;gap:10px;cursor:default;">'
        f'{radio_span(i==0)}'
        f'<span style="font-size:14px;font-family:var(--font-family-sans);color:var(--color-content-{"default" if i==0 else "subtle"});">{label}</span>'
        f'</label>'
        for i, label in enumerate(['Light mode', 'Dark mode', 'System'])
    )
    + '</div>'
),

# Switch: two toggles with labels
'switch': (
    '<div style="display:flex;flex-direction:column;gap:12px;pointer-events:none;">'
    + ''.join(
        f'<div style="display:flex;align-items:center;justify-content:space-between;gap:40px;">'
        f'<span style="font-size:14px;font-family:var(--font-family-sans);color:var(--color-content-default);">{label}</span>'
        f'<label class="toggle-switch" style="pointer-events:none;">'
        f'<input type="checkbox"{"" if not on else " checked"} tabindex="-1" style="pointer-events:none;">'
        f'<div class="toggle-track"><div class="toggle-handle"><div class="toggle-icon">'
        f'<svg class="icon-check" viewBox="0 0 12 12" fill="none"><path d="M2 6L5 9L10 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        f'<svg class="icon-x" viewBox="0 0 12 12" fill="none"><path d="M3 3L9 9M9 3L3 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        f'</div></div></div></label></div>'
        for label, on in [('Dark mode', True), ('Notifications', False)]
    )
    + '</div>'
),

# Segmented control: 3 options
'segmented-control': (
    '<div style="pointer-events:none;">'
    '<div class="seg-control">'
    '<span class="seg-control-slider" style="transform:translateX(100%);" aria-hidden="true"></span>'
    '<button class="seg-control-btn" aria-pressed="false" tabindex="-1">Day</button>'
    '<button class="seg-control-btn" aria-pressed="true"  tabindex="-1">Week</button>'
    '<button class="seg-control-btn" aria-pressed="false" tabindex="-1">Month</button>'
    '</div>'
    '</div>'
),

# Stepper: one full stepper control
'stepper': (
    '<div style="pointer-events:none;display:flex;flex-direction:column;gap:8px;align-items:center;">'
    '<span style="font-size:12px;font-family:var(--font-family-sans);color:var(--color-content-subtle);letter-spacing:0.02em;text-transform:uppercase;">Quantity</span>'
    '<div class="stepper">'
    '<button class="stepper-btn" tabindex="-1"><div class="stepper-btn-pill btn btn-outlined" style="min-width:0;width:36px;height:36px;display:flex;align-items:center;justify-content:center;padding:0;">−</div></button>'
    '<input class="stepper-field" type="number" value="3" tabindex="-1" style="pointer-events:none;width:48px;text-align:center;">'
    '<button class="stepper-btn" tabindex="-1"><div class="stepper-btn-pill btn btn-outlined" style="min-width:0;width:36px;height:36px;display:flex;align-items:center;justify-content:center;padding:0;">+</div></button>'
    '</div>'
    '</div>'
),

# Search field: full search input, focused
'search-field': (
    '<div style="width:190px;pointer-events:none;">'
    '<div class="tf-ifield tf-ifield--focused" style="border-radius:var(--corner-radius-round);">'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-subtle);flex-shrink:0;margin-left:4px;"><use href="#ico-search"/></svg>'
    '<input class="tf-iinput" type="search" placeholder="Search components…" tabindex="-1" style="pointer-events:none;">'
    '</div>'
    '</div>'
),

# ── NAVIGATION ────────────────────────────────────────────────────────────────

# Bottom nav: 4-tab nav bar, scaled to fit
'bottom-nav': (
    '<div style="pointer-events:none;transform:scale(0.82);transform-origin:center;">'
    '<nav class="bnav" style="position:static;box-shadow:0 -1px 0 var(--color-border-subtle),0 4px 24px rgba(8,5,13,0.14);">'
    '<div class="bnav-track">'
    + ''.join(
        f'<button class="bnav-tab{"" if icon!="ico-unica" else " bnav-tab--active"}" tabindex="-1">'
        f'<span class="bnav-tab-icon"><svg width="22" height="22" viewBox="0 0 24 24" fill="none"><use href="#{icon}"/></svg></span>'
        f'<span class="bnav-tab-label">{label}</span>'
        f'</button>'
        for icon, label in [('ico-unica','Home'),('ico-search','Explore'),('ico-heart','Saved'),('ico-bell','Alerts')]
    )
    + '</div></nav></div>'
),

# Tabs: 3 tabs with active indicator
'tabs': (
    '<div style="pointer-events:none;width:200px;">'
    '<div role="tablist" style="display:flex;border-bottom:1px solid var(--color-border-subtle);">'
    + ''.join(
        f'<button class="tab-item{"" if i!=1 else " tab-item--active"}" aria-selected="{"false" if i!=1 else "true"}" tabindex="-1"'
        f' style="flex:1;{" border-bottom:2px solid var(--color-action-default);" if i==1 else ""}">'
        f'{label}</button>'
        for i, label in enumerate(['Overview','Details','Settings'])
    )
    + '</div></div>'
),

# Date tabs: a row of day selectors
'date-tabs': (
    '<div style="display:flex;gap:6px;pointer-events:none;">'
    + ''.join(
        f'<button tabindex="-1" style="display:flex;flex-direction:column;align-items:center;justify-content:center;'
        f'width:44px;height:56px;border-radius:12px;border:none;cursor:default;gap:2px;'
        f'background:{"var(--color-action-default)" if i==2 else "var(--color-background-page)"};'
        f'color:{"var(--color-content-on-action)" if i==2 else "var(--color-content-default)"};'
        f'box-shadow:{"0 2px 12px rgba(8,5,13,0.16)" if i==2 else "0 1px 4px rgba(8,5,13,0.08)"};'
        f'font-family:var(--font-family-sans);pointer-events:none;">'
        f'<span style="font-size:10px;opacity:0.7;">{day}</span>'
        f'<span style="font-size:18px;font-weight:600;">{date}</span>'
        f'</button>'
        for i, (day, date) in enumerate([('Mon','9'),('Tue','10'),('Wed','11'),('Thu','12'),('Fri','13')])
    )
    + '</div>'
),

# Pagination: 5 buttons with one selected
'pagination': (
    '<div style="display:flex;gap:4px;align-items:center;pointer-events:none;">'
    '<button class="pag-btn" tabindex="-1" style="pointer-events:none;">'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="transform:rotate(180deg);"><use href="#ico-caret-right"/></svg>'
    '</button>'
    + ''.join(
        f'<button class="pag-btn{"" if i!=2 else " pag-btn--selected"}" tabindex="-1" style="pointer-events:none;">{i+1}</button>'
        for i in range(5)
    )
    + '<button class="pag-btn" tabindex="-1" style="pointer-events:none;">'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><use href="#ico-caret-right"/></svg>'
    '</button>'
    '</div>'
),

# Top nav app: mobile app header bar
'top-nav-app': (
    '<div style="pointer-events:none;width:210px;background:var(--color-background-page);'
    'border-radius:14px;box-shadow:0 4px 24px rgba(8,5,13,0.16);overflow:hidden;">'
    '<div style="display:flex;align-items:center;padding:12px 14px;gap:10px;">'
    '<button tabindex="-1" style="background:none;border:none;padding:0;cursor:default;color:var(--color-content-default);display:flex;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-arrow"/></svg>'
    '</button>'
    '<span style="flex:1;font-size:15px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);">Components</span>'
    '<button tabindex="-1" style="background:none;border:none;padding:0;cursor:default;color:var(--color-content-default);display:flex;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-search"/></svg>'
    '</button>'
    '<button tabindex="-1" style="background:none;border:none;padding:0;cursor:default;color:var(--color-content-default);display:flex;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-bell"/></svg>'
    '</button>'
    '</div>'
    '</div>'
),

# Top nav web: desktop nav bar
'top-nav-web': (
    '<div style="pointer-events:none;width:220px;background:var(--color-background-page);'
    'border-radius:14px;box-shadow:0 4px 24px rgba(8,5,13,0.16);overflow:hidden;">'
    '<div style="display:flex;align-items:center;padding:10px 14px;gap:10px;border-bottom:1px solid var(--color-border-subtle);">'
    '<div style="width:24px;height:24px;border-radius:50%;background:var(--color-brand-ink);flex-shrink:0;"></div>'
    '<div style="display:flex;gap:12px;flex:1;justify-content:center;">'
    + ''.join(
        f'<span style="font-size:12px;font-family:var(--font-family-sans);color:{"var(--color-action-default);font-weight:600" if i==0 else "var(--color-content-subtle)"};">{label}</span>'
        for i, label in enumerate(['Components','Foundations','About'])
    )
    + '</div>'
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;font-size:11px;padding:6px 12px;height:auto;min-width:0;">Get started</button>'
    '</div>'
    '</div>'
),

# ── FEEDBACK & OVERLAY ────────────────────────────────────────────────────────

# Toast: a real toast notification
'toast': (
    '<div style="pointer-events:none;max-width:220px;">'
    '<div class="toast" style="pointer-events:none;">'
    '<span class="toast-icon-bullet toast-icon-bullet--success" aria-hidden="true"></span>'
    '<span class="toast-message">Changes saved successfully</span>'
    '<button class="toast-dismiss" tabindex="-1" style="pointer-events:none;">'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><use href="#ico-x-sm"/></svg>'
    '</button>'
    '</div>'
    '</div>'
),

# Badge: two examples — dot and number
'badge': (
    '<div style="display:flex;gap:16px;align-items:center;pointer-events:none;">'
    '<div style="position:relative;display:inline-flex;">'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;width:44px;height:44px;padding:0;display:flex;align-items:center;justify-content:center;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-default);"><use href="#ico-bell"/></svg>'
    '</button>'
    '<span class="badge-number badge-number--alert" style="position:absolute;top:-6px;right:-6px;">9</span>'
    '</div>'
    '<div style="position:relative;display:inline-flex;">'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;width:44px;height:44px;padding:0;display:flex;align-items:center;justify-content:center;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-default);"><use href="#ico-message"/></svg>'
    '</button>'
    '<span class="badge-dot badge-dot--alert" style="position:absolute;top:-4px;right:-4px;"></span>'
    '</div>'
    '</div>'
),

# Progress: circular + linear
'progress': (
    '<div style="display:flex;flex-direction:column;gap:16px;align-items:center;pointer-events:none;">'
    '<svg class="progress-circular" width="64" height="64" viewBox="0 0 52 52" aria-hidden="true">'
    '<circle class="progress-circular-track" cx="26" cy="26" r="22" fill="none" stroke-width="4"/>'
    '<circle class="progress-circular-fill"  cx="26" cy="26" r="22" fill="none" stroke-width="4" stroke-dasharray="138.2" stroke-dashoffset="42" transform="rotate(-90 26 26)"/>'
    '</svg>'
    '<div style="width:140px;height:6px;border-radius:3px;background:var(--color-border-subtle);overflow:hidden;">'
    '<div style="width:65%;height:100%;background:var(--color-action-default);border-radius:3px;"></div>'
    '</div>'
    '</div>'
),

# Scrim: dark overlay with a dialog peeking above
'scrim': (
    '<div style="pointer-events:none;position:relative;width:180px;height:110px;border-radius:14px;overflow:hidden;">'
    '<div style="position:absolute;inset:0;background:rgba(8,5,13,0.42);border-radius:14px;"></div>'
    '<div style="position:absolute;bottom:0;left:0;right:0;height:72px;background:var(--color-background-page);'
    'border-radius:14px 14px 0 0;display:flex;flex-direction:column;align-items:center;padding:14px 16px;gap:8px;">'
    '<div style="width:32px;height:4px;border-radius:2px;background:var(--color-border-default);"></div>'
    '<div style="width:110px;height:6px;border-radius:3px;background:var(--color-border-subtle);"></div>'
    '</div>'
    '</div>'
),

# Modal: floating dialog card
'modal': (
    '<div style="pointer-events:none;width:178px;background:var(--color-background-page);'
    'border-radius:16px;box-shadow:0 8px 40px rgba(8,5,13,0.22),0 0 0 1px rgba(8,5,13,0.05);overflow:hidden;">'
    '<div style="padding:16px 16px 0;">'
    '<div style="font-size:13px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);margin-bottom:6px;">Confirm action</div>'
    '<div style="font-size:11px;font-family:var(--font-family-sans);color:var(--color-content-subtle);line-height:1.5;">This cannot be undone. Are you sure you want to continue?</div>'
    '</div>'
    '<div style="display:flex;gap:8px;padding:12px 16px;justify-content:flex-end;">'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;font-size:12px;padding:6px 12px;height:auto;min-width:0;">Cancel</button>'
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;font-size:12px;padding:6px 12px;height:auto;min-width:0;">Continue</button>'
    '</div>'
    '</div>'
),

# Bottom sheet: sheet rising with grabber + content rows
'bottom-sheet': (
    '<div style="pointer-events:none;width:190px;background:var(--color-background-page);'
    'border-radius:16px 16px 0 0;box-shadow:0 -4px 32px rgba(8,5,13,0.16);'
    'display:flex;flex-direction:column;align-items:center;padding:10px 16px 16px;">'
    '<div style="width:32px;height:4px;border-radius:2px;background:var(--color-border-default);margin-bottom:14px;"></div>'
    + ''.join(
        f'<div style="width:100%;display:flex;align-items:center;gap:10px;padding:8px 0;'
        f'{"border-top:1px solid var(--color-border-subtle);" if i else ""}pointer-events:none;">'
        f'<div style="width:32px;height:32px;border-radius:8px;background:var(--color-background-subtle);'
        f'display:flex;align-items:center;justify-content:center;flex-shrink:0;">'
        f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-subtle);"><use href="#{ico}"/></svg>'
        f'</div>'
        f'<span style="font-size:13px;font-family:var(--font-family-sans);color:var(--color-content-default);">{label}</span>'
        f'</div>'
        for i, (ico, label) in enumerate([('ico-heart','Save to collection'),('ico-message','Share link'),('ico-eye-show','Preview')])
    )
    + '</div>'
),

# ── DISPLAY ───────────────────────────────────────────────────────────────────

# Avatar: facepile of 4 + overflow count
'avatar': (
    '<div style="display:flex;align-items:center;pointer-events:none;">'
    + ''.join(
        f'<div class="avatar avatar--large avatar--circle" style="margin-left:{"-12" if i else "0"}px;'
        f'background:var(--primitive-{"violet" if i==0 else "pool" if i==1 else "berry" if i==2 else "mint"}-200);'
        f'color:var(--color-content-default);font-size:12px;font-weight:700;'
        f'display:flex;align-items:center;justify-content:center;'
        f'box-shadow:0 0 0 2px var(--color-background-page);font-family:var(--font-family-sans);">{initials}</div>'
        for i, initials in enumerate(['EJ','TM','PK','AR'])
    )
    + '<div class="avatar avatar--large avatar--circle" style="margin-left:-12px;'
    'background:var(--color-background-subtle);color:var(--color-content-subtle);font-size:11px;font-weight:600;'
    'display:flex;align-items:center;justify-content:center;font-family:var(--font-family-sans);'
    'box-shadow:0 0 0 2px var(--color-background-page);">+8</div>'
    '</div>'
),

# Card: standard card with image area + content + action
'card': (
    '<div style="pointer-events:none;width:160px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-l);box-shadow:0 4px 24px rgba(8,5,13,0.16),0 0 0 1px rgba(8,5,13,0.04);overflow:hidden;">'
    '<div style="height:72px;background:linear-gradient(135deg,var(--primitive-violet-100),var(--primitive-berry-100));'
    'display:flex;align-items:center;justify-content:center;">'
    '<svg width="28" height="28" viewBox="0 0 24 24" fill="none" style="color:var(--primitive-violet-400);"><use href="#ico-leaf"/></svg>'
    '</div>'
    '<div style="padding:12px;">'
    '<div style="font-size:13px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);margin-bottom:4px;">Card title</div>'
    '<div style="font-size:11px;font-family:var(--font-family-sans);color:var(--color-content-subtle);line-height:1.4;margin-bottom:10px;">Short supporting description text here.</div>'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;font-size:11px;padding:5px 10px;height:auto;min-width:0;">Learn more</button>'
    '</div>'
    '</div>'
),

# Card color block: accent stripe on left
'card-color-block': (
    '<div style="pointer-events:none;width:168px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-l);box-shadow:0 4px 24px rgba(8,5,13,0.16);overflow:hidden;display:flex;">'
    '<div style="width:5px;background:var(--color-action-default);flex-shrink:0;"></div>'
    '<div style="flex:1;padding:14px;">'
    '<div style="font-size:12px;font-weight:700;font-family:var(--font-family-sans);color:var(--color-content-default);margin-bottom:5px;">System update</div>'
    '<div style="font-size:11px;font-family:var(--font-family-sans);color:var(--color-content-subtle);line-height:1.5;margin-bottom:10px;">A new version of the design system is available.</div>'
    '<div style="display:flex;gap:6px;">'
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;font-size:11px;padding:5px 10px;height:auto;min-width:0;">Update</button>'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;font-size:11px;padding:5px 10px;height:auto;min-width:0;">Later</button>'
    '</div>'
    '</div>'
    '</div>'
),

# Card media: photo card
'card-media': (
    '<div style="pointer-events:none;width:160px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-l);box-shadow:0 4px 24px rgba(8,5,13,0.16);overflow:hidden;">'
    '<div style="height:90px;background:linear-gradient(160deg,var(--primitive-pool-100),var(--primitive-mint-100));'
    'position:relative;display:flex;align-items:center;justify-content:center;">'
    '<svg width="36" height="36" viewBox="0 0 24 24" fill="none" style="color:var(--primitive-pool-400);"><use href="#ico-cloud"/></svg>'
    '<div style="position:absolute;top:8px;right:8px;">'
    '<span class="tag tag--success" style="font-size:9px;padding:2px 7px;">New</span>'
    '</div>'
    '</div>'
    '<div style="padding:10px 12px;">'
    '<div style="font-size:12px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);margin-bottom:3px;">Media card</div>'
    '<div style="font-size:10px;font-family:var(--font-family-sans);color:var(--color-content-subtle);">Image, video, or illustration</div>'
    '</div>'
    '</div>'
),

# Card multi: content card with avatar + action row
'card-multi': (
    '<div style="pointer-events:none;width:168px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-l);box-shadow:0 4px 24px rgba(8,5,13,0.16);padding:14px;box-sizing:border-box;">'
    '<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;">'
    '<div class="avatar avatar--medium avatar--circle" style="background:var(--primitive-berry-200);color:var(--color-content-default);font-size:11px;font-weight:600;display:flex;align-items:center;justify-content:center;font-family:var(--font-family-sans);">PK</div>'
    '<div>'
    '<div style="font-size:12px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);">Priya Kuma…</div>'
    '<div style="font-size:10px;font-family:var(--font-family-sans);color:var(--color-content-subtle);">Design lead</div>'
    '</div>'
    '</div>'
    '<div style="font-size:11px;font-family:var(--font-family-sans);color:var(--color-content-subtle);line-height:1.5;margin-bottom:10px;">Supporting content for the multifunctional card format.</div>'
    '<div style="display:flex;gap:6px;">'
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;font-size:11px;padding:5px 10px;height:auto;min-width:0;">Follow</button>'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;font-size:11px;padding:5px 10px;height:auto;min-width:0;">View</button>'
    '</div>'
    '</div>'
),

# List: 3 list rows with avatar + label
'list': (
    '<div style="pointer-events:none;width:190px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-m);box-shadow:0 4px 24px rgba(8,5,13,0.14),0 0 0 1px rgba(8,5,13,0.04);overflow:hidden;">'
    + ''.join(
        f'<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;'
        f'{"background:var(--color-background-selection);" if i==1 else ""}'
        f'{"border-top:1px solid var(--color-border-subtle);" if i>0 else ""}pointer-events:none;">'
        f'<div class="avatar avatar--small avatar--circle" style="background:var(--primitive-{"violet" if i==0 else "pool" if i==1 else "berry"}-200);'
        f'color:var(--color-content-default);font-size:9px;font-weight:700;display:flex;align-items:center;justify-content:center;font-family:var(--font-family-sans);flex-shrink:0;">{initials}</div>'
        f'<div style="flex:1;">'
        f'<div style="font-size:12px;font-weight:{"600" if i==1 else "400"};font-family:var(--font-family-sans);color:var(--color-content-default);">{name}</div>'
        f'<div style="font-size:10px;font-family:var(--font-family-sans);color:var(--color-content-subtle);">{role}</div>'
        f'</div>'
        f'<svg width="12" height="12" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-subtle);flex-shrink:0;"><use href="#ico-caret-right"/></svg>'
        f'</div>'
        for i, (initials, name, role) in enumerate([('EJ','Elona Jaquez','Design Director'),('TM','Tomás M.','Product Lead'),('PK','Priya Kumar','Engineer')])
    )
    + '</div>'
),

# List accordion: 2 rows, first one open
'list-accordion': (
    '<div style="pointer-events:none;width:190px;background:var(--color-background-page);'
    'border-radius:var(--corner-radius-m);box-shadow:0 4px 24px rgba(8,5,13,0.14);overflow:hidden;">'

    # Open item
    '<div>'
    '<button class="list-accordion__header" aria-expanded="true" tabindex="-1" style="width:100%;display:flex;align-items:center;gap:8px;padding:10px 12px;border:none;background:none;cursor:default;">'
    '<span style="flex:1;font-size:13px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);text-align:left;">Foundations</span>'
    '<div class="list-accordion__control"><div class="list-accordion__control-inner" style="background:var(--color-action-hover-subtle);">'
    '<svg class="list-accordion__chevron" viewBox="0 0 24 24" width="14" height="14" fill="none" style="transform:rotate(180deg);"><use href="#ico-caret-dn"/></svg>'
    '</div></div>'
    '</button>'
    '<div style="padding:4px 12px 10px;border-bottom:1px solid var(--color-border-subtle);">'
    '<div style="font-size:11px;font-family:var(--font-family-sans);color:var(--color-content-subtle);line-height:1.6;">Color, typography, spacing, and grid — the primitives behind every component.</div>'
    '</div>'
    '</div>'

    # Closed item
    '<button class="list-accordion__header" aria-expanded="false" tabindex="-1" style="width:100%;display:flex;align-items:center;gap:8px;padding:10px 12px;border:none;background:none;cursor:default;">'
    '<span style="flex:1;font-size:13px;font-weight:400;font-family:var(--font-family-sans);color:var(--color-content-default);text-align:left;">Components</span>'
    '<div class="list-accordion__control"><div class="list-accordion__control-inner">'
    '<svg class="list-accordion__chevron" viewBox="0 0 24 24" width="14" height="14" fill="none"><use href="#ico-caret-dn"/></svg>'
    '</div></div>'
    '</button>'
    '</div>'
),

# Date picker: mini calendar grid
'date-picker': (
    '<div style="pointer-events:none;background:var(--color-background-page);border-radius:var(--corner-radius-l);'
    'box-shadow:0 4px 24px rgba(8,5,13,0.16);padding:12px;width:auto;display:inline-block;">'
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">'
    '<button tabindex="-1" style="background:none;border:none;cursor:default;color:var(--color-content-subtle);display:flex;">'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" style="transform:rotate(180deg);"><use href="#ico-caret-right"/></svg>'
    '</button>'
    '<span style="font-size:12px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-default);">June 2026</span>'
    '<button tabindex="-1" style="background:none;border:none;cursor:default;color:var(--color-content-subtle);display:flex;">'
    '<svg width="14" height="14" viewBox="0 0 24 24" fill="none"><use href="#ico-caret-right"/></svg>'
    '</button>'
    '</div>'
    '<div style="display:grid;grid-template-columns:repeat(7,24px);gap:3px;">'
    + ''.join(
        f'<div style="width:24px;height:24px;border-radius:50%;display:flex;align-items:center;justify-content:center;'
        f'font-size:9px;font-family:var(--font-family-sans);'
        f'{"background:var(--color-action-default);color:var(--color-content-on-action);font-weight:700;" if d==11 else "color:var(--color-content-subtle);" if d in (1,2,3,4,5) else "color:var(--color-content-default);"}'
        f'">{d}</div>'
        for d in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28]
    )
    + '</div>'
    '</div>'
),

# Divider: ruled sections with labels
'divider': (
    '<div style="pointer-events:none;width:180px;display:flex;flex-direction:column;gap:12px;">'
    '<div>'
    '<div style="font-size:10px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-subtle);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;">Section A</div>'
    '<hr class="divider" style="margin:0;">'
    '</div>'
    '<div>'
    '<div style="font-size:10px;font-weight:600;font-family:var(--font-family-sans);color:var(--color-content-subtle);letter-spacing:0.08em;text-transform:uppercase;margin-bottom:6px;">Section B</div>'
    '<hr class="divider divider--bold" style="margin:0;">'
    '</div>'
    '<div>'
    '<hr class="divider" style="margin:0;">'
    '</div>'
    '</div>'
),

# Icon bullet: 3 icon-bullet list items
'icon-bullet': (
    '<div style="pointer-events:none;display:flex;flex-direction:column;gap:10px;">'
    + ''.join(
        f'<div style="display:flex;align-items:center;gap:10px;">'
        f'<div class="icon-bullet icon-bullet--medium">'
        f'<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><use href="#{ico}"/></svg>'
        f'</div>'
        f'<span style="font-size:13px;font-family:var(--font-family-sans);color:var(--color-content-default);">{label}</span>'
        f'</div>'
        for ico, label in [('ico-fire','Enduring by design'),('ico-bulb','Precisely crafted'),('ico-leaf','Token-driven')]
    )
    + '</div>'
),

}  # end COMPS

# ─── CSS ──────────────────────────────────────────────────────────────────────
NEW_CSS = '''
  /* comp-overview: true component render (no center shape) */
  .cov-comp {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    z-index: 2;
  }
'''

# ─── Build scene line (no ctt-center-shape) ───────────────────────────────────
def make_scene(target, tile_idx):
    cat  = CATS[target]
    path = SHAPES[SHAPE_IDX.get(target, tile_idx % 6)]
    sa   = 'viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"'
    bg1  = f'<svg class="ctt-bg-shape ctt-bg-shape--1" {sa}><path d="{path}"/></svg>'
    bg2  = f'<svg class="ctt-bg-shape ctt-bg-shape--2" {sa}><path d="{path}"/></svg>'
    comp = f'<div class="cov-comp">{COMPS.get(target, "")}</div>'
    return f'<div class="ctt-scene ctt-scene--{cat}">{bg1}{bg2}{comp}'

# ─── Inject ───────────────────────────────────────────────────────────────────
with open(FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Inject CSS
for i, line in enumerate(lines):
    if line.strip() == '</style>' and i < 12000:
        lines.insert(i, NEW_CSS)
        print(f'  ✓ CSS injected before line {i+1}')
        break

target_pat = re.compile(r'data-nav-target="([^"]+)"')
modified = 0
tile_idx  = 0

for i in range(len(lines)):
    m = target_pat.search(lines[i])
    if m and m.group(1) in CATS:
        target = m.group(1)
        for j in range(i+1, min(i+6, len(lines))):
            if 'ctt-scene' in lines[j] or 'cov-snap' in lines[j] or 'cov-comp' in lines[j]:
                leading = re.match(r'^(\s*)', lines[j]).group(1)
                lines[j] = leading + make_scene(target, tile_idx) + '\n'
                print(f'  ✓ {target:22s} shape={SHAPE_IDX.get(target,0)} (line {j+1})')
                modified += 1
                tile_idx += 1
                break

print(f'\nTotal: {modified} tiles injected')
with open(FILE, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done.')
