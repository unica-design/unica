#!/usr/bin/env python3
"""
Hybrid v2: shape art + floating component overlay.
Key fix: use actual component CSS classes (like radio/checkbox did) so the
real component color shows through. Keep elements SMALL so shapes stay visible.
No large opaque white backgrounds blocking the shape art.
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

# Checkbox SVG path (reusable)
CHK_PATH = 'M9.44038 0.240068C9.72214 -0.0635401 10.1963 -0.0817123 10.5 0.200029C10.8034 0.481649 10.8213 0.955964 10.54 1.2596L4.5146 7.75179L3.97456 8.33382L3.42378 7.76155L0.208937 4.41585C-0.0778684 4.11718 -0.0681694 3.64225 0.230422 3.3553C0.529095 3.0685 1.00403 3.0782 1.29097 3.37679L3.95503 6.14925L6.42769 3.48616L9.44038 0.240068Z'

def checkbox_html(scale=1.5):
    return (
        f'<span class="checkbox" style="pointer-events:none;transform:scale({scale});">'
        '<input type="checkbox" checked tabindex="-1">'
        '<span class="checkbox-box">'
        f'<svg class="checkbox-check" viewBox="0 0 10.7398 8.33382" fill="none"><path d="{CHK_PATH}" fill="currentColor"/></svg>'
        '<span class="checkbox-dash"></span>'
        '</span></span>'
    )

def radio_html(scale=1.8):
    return (
        f'<span class="radio" style="pointer-events:none;transform:scale({scale});">'
        '<input type="radio" checked tabindex="-1">'
        '<span class="radio-circle"><span class="radio-dot"></span></span>'
        '</span>'
    )

def toggle_html():
    return (
        '<div class="toggle-switch" style="pointer-events:none;transform:scale(1.4);">'
        '<input type="checkbox" checked tabindex="-1">'
        '<div class="toggle-track"><div class="toggle-handle"><div class="toggle-icon">'
        '<svg class="icon-check" viewBox="0 0 12 12" fill="none"><path d="M2 6L5 9L10 3" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        '<svg class="icon-x" viewBox="0 0 12 12" fill="none"><path d="M3 3L9 9M9 3L3 9" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
        '</div></div></div></div>'
    )

# ─── Floats: real CSS classes + keep small so shapes show through ─────────────
FLOATS = {

# ACTIONS ─────────────────────────────────────────────────────────────────────

# Empty filled button pill — real btn CSS, violet accent, no text
'button':
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;width:72px;height:0;padding-top:18px;padding-bottom:18px;overflow:hidden;font-size:0;"></button>',

# One selected choice button, accessory only visible (no text div)
'choice-button': (
    '<div class="choice-btn choice-btn--vertical" aria-pressed="true" tabindex="-1" style="pointer-events:none;transform:scale(1.1);">'
    '<div class="choice-btn-accessory">'
    '<div class="avatar avatar--medium avatar--circle" style="background:var(--primitive-violet-200);color:var(--color-content-default);font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;">EJ</div>'
    '</div>'
    '</div>'
),

# Three chips in a row — real chip CSS, selected state = violet
'chips': (
    '<div style="display:flex;gap:6px;">'
    '<button class="chip chip--selected" aria-pressed="true" tabindex="-1" style="pointer-events:none;font-size:0;width:28px;height:28px;padding:0;"></button>'
    '<button class="chip" tabindex="-1" style="pointer-events:none;font-size:0;width:28px;height:28px;padding:0;"></button>'
    '<button class="chip chip--selected" aria-pressed="true" tabindex="-1" style="pointer-events:none;font-size:0;width:28px;height:28px;padding:0;"></button>'
    '</div>'
),

# Two tags — real tag CSS colors (success=mint, emphasis=dark)
'tags': (
    '<div style="display:flex;flex-direction:column;gap:6px;align-items:center;">'
    '<span class="tag tag--success" style="font-size:0;width:48px;height:18px;display:block;border-radius:999px;"></span>'
    '<span class="tag tag--emphasis" style="font-size:0;width:36px;height:18px;display:block;border-radius:999px;"></span>'
    '</div>'
),

# Link: just the arrow icon
'link':
    '<svg width="36" height="36" viewBox="0 0 24 24" aria-hidden="true" style="color:var(--color-action-default);filter:drop-shadow(0 1px 6px rgba(8,5,13,0.18));"><use href="#ico-arrow"/></svg>',

# INPUTS ──────────────────────────────────────────────────────────────────────

# Text field — real tf-ifield CSS, focused state
'text-fields': (
    '<div class="tf-ifield tf-ifield--focused" style="width:100px;pointer-events:none;">'
    '<input class="tf-iinput" type="text" placeholder="" tabindex="-1" style="pointer-events:none;width:100%;caret-color:transparent;">'
    '</div>'
),

# Checked checkbox — real CSS, violet
'checkbox': checkbox_html(1.6),

# Selected radio — real CSS, violet
'radio': radio_html(2.0),

# Toggle switch — real CSS, on state
'switch': toggle_html(),

# Segmented control — 3 segments, middle selected
'segmented-control': (
    '<div class="seg-control" style="pointer-events:none;transform:scale(0.95);">'
    '<span class="seg-control-slider" style="transform:translateX(100%);" aria-hidden="true"></span>'
    '<button class="seg-control-btn" aria-pressed="false" tabindex="-1" style="font-size:0;width:32px;height:28px;padding:0;"></button>'
    '<button class="seg-control-btn" aria-pressed="true"  tabindex="-1" style="font-size:0;width:32px;height:28px;padding:0;"></button>'
    '<button class="seg-control-btn" aria-pressed="false" tabindex="-1" style="font-size:0;width:32px;height:28px;padding:0;"></button>'
    '</div>'
),

# Stepper — real CSS, minimal
'stepper': (
    '<div class="stepper stepper--sm" style="pointer-events:none;transform:scale(1.1);">'
    '<div class="stepper-btn"><div class="stepper-btn-pill btn btn-outlined" style="padding:0 12px;min-width:0;">−</div></div>'
    '<input class="stepper-field" type="number" value="3" tabindex="-1" style="pointer-events:none;width:36px;">'
    '<div class="stepper-btn"><div class="stepper-btn-pill btn btn-outlined" style="padding:0 12px;min-width:0;">+</div></div>'
    '</div>'
),

# Search — magnifying glass icon in real search-field CSS
'search-field':
    '<svg width="40" height="40" viewBox="0 0 24 24" aria-hidden="true" style="color:var(--color-content-subtle);filter:drop-shadow(0 1px 8px rgba(8,5,13,0.15));"><use href="#ico-search"/></svg>',

# NAVIGATION ──────────────────────────────────────────────────────────────────

# Bottom nav — real bnav CSS, one active tab with icon (no label text)
'bottom-nav': (
    '<nav class="bnav" style="pointer-events:none;transform:scale(0.85);position:static;box-shadow:none;">'
    '<div class="bnav-track" style="background:rgba(255,255,255,0.88);border-radius:var(--corner-radius-round);box-shadow:0 2px 14px rgba(8,5,13,0.14);">'
    '<button class="bnav-tab bnav-tab--active" tabindex="-1"><span class="bnav-tab-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-unica"/></svg></span></button>'
    '<button class="bnav-tab" tabindex="-1"><span class="bnav-tab-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-search"/></svg></span></button>'
    '<button class="bnav-tab" tabindex="-1"><span class="bnav-tab-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-heart"/></svg></span></button>'
    '<button class="bnav-tab" tabindex="-1"><span class="bnav-tab-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none"><use href="#ico-bell"/></svg></span></button>'
    '</div></nav>'
),

# Tabs — real tab-item CSS, one selected, no labels (font-size:0)
'tabs': (
    '<div role="tablist" style="display:flex;gap:2px;background:rgba(255,255,255,0.88);border-radius:var(--corner-radius-round);padding:3px;box-shadow:0 2px 14px rgba(8,5,13,0.12);">'
    '<button class="tab-item" aria-selected="true"  tabindex="-1" style="font-size:0;width:36px;height:30px;padding:0;border-radius:var(--corner-radius-round);"></button>'
    '<button class="tab-item" aria-selected="false" tabindex="-1" style="font-size:0;width:36px;height:30px;padding:0;"></button>'
    '<button class="tab-item" aria-selected="false" tabindex="-1" style="font-size:0;width:36px;height:30px;padding:0;"></button>'
    '</div>'
),

# Date tabs — 3 day squares, first selected (pure CSS, real shape)
'date-tabs': (
    '<div style="display:flex;gap:6px;">'
    + ''.join(
        f'<div style="width:36px;height:46px;border-radius:10px;'
        f'background:{"var(--color-action-default)" if i==0 else "rgba(255,255,255,0.78)"};'
        f'box-shadow:0 2px 10px rgba(8,5,13,{"0.16" if i==0 else "0.10"});'
        f'border:{"none" if i==0 else "1px solid rgba(255,255,255,0.5)"};"></div>'
        for i in range(3)
    )
    + '</div>'
),

# Pagination — real pag-btn CSS, 3rd selected
'pagination': (
    '<div style="display:flex;gap:3px;">'
    + ''.join(
        f'<button class="pag-btn{"" if i!=2 else " pag-btn--selected"}" tabindex="-1" style="pointer-events:none;font-size:0;width:28px;height:28px;padding:0;"></button>'
        for i in range(5)
    )
    + '</div>'
),

# Top nav app — 3 icon buttons in a pill bar
'top-nav-app': (
    '<div style="display:flex;align-items:center;gap:6px;background:rgba(255,255,255,0.88);border-radius:var(--corner-radius-round);padding:6px 10px;box-shadow:0 2px 14px rgba(8,5,13,0.12);">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-default);"><use href="#ico-arrow"/></svg>'
    '<div style="width:40px;height:6px;border-radius:999px;background:var(--color-border-subtle);margin:0 6px;"></div>'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-default);"><use href="#ico-search"/></svg>'
    '</div>'
),

# Top nav web — logo + nav dots + CTA pill
'top-nav-web': (
    '<div style="display:flex;align-items:center;gap:8px;background:rgba(255,255,255,0.88);border-radius:var(--corner-radius-round);padding:6px 10px;box-shadow:0 2px 14px rgba(8,5,13,0.12);">'
    '<div style="width:24px;height:24px;border-radius:50%;background:var(--color-brand-ink);opacity:0.85;flex-shrink:0;"></div>'
    '<div style="display:flex;gap:5px;flex:1;justify-content:center;">'
    + ''.join('<div style="width:18px;height:5px;border-radius:999px;background:var(--color-border-default);"></div>' for _ in range(3))
    + '</div>'
    '<button class="btn btn-filled" tabindex="-1" style="pointer-events:none;font-size:0;width:32px;height:24px;padding:0;border-radius:999px;"></button>'
    '</div>'
),

# FEEDBACK ────────────────────────────────────────────────────────────────────

# Toast — real toast CSS, just an icon bullet (no message text)
'toast': (
    '<div class="toast" style="pointer-events:none;transform:scale(1.1);">'
    '<span class="toast-icon-bullet toast-icon-bullet--success" aria-hidden="true"></span>'
    '<span class="toast-message" style="width:56px;height:6px;background:var(--color-border-subtle);border-radius:999px;display:block;"></span>'
    '</div>'
),

# Badge — bell icon with real badge-number--alert
'badge': (
    '<div style="position:relative;display:inline-flex;">'
    '<button class="btn btn-outlined" tabindex="-1" style="pointer-events:none;width:44px;height:44px;padding:0;display:flex;align-items:center;justify-content:center;">'
    '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" style="color:var(--color-content-default);"><use href="#ico-bell"/></svg>'
    '</button>'
    '<span class="badge-number badge-number--alert" style="position:absolute;top:-6px;right:-6px;">3</span>'
    '</div>'
),

# Progress — real progress-circular SVG
'progress': (
    '<svg class="progress-circular" width="60" height="60" viewBox="0 0 52 52" aria-hidden="true" style="pointer-events:none;">'
    '<circle class="progress-circular-track" cx="26" cy="26" r="22" fill="none" stroke-width="4"/>'
    '<circle class="progress-circular-fill" cx="26" cy="26" r="22" fill="none" stroke-width="4" stroke-dasharray="138.2" stroke-dashoffset="38" transform="rotate(-90 26 26)"/>'
    '</svg>'
),

# Scrim — translucent dark layer with tiny card emerging
'scrim': (
    '<div style="position:relative;width:80px;height:64px;border-radius:10px;overflow:hidden;">'
    '<div style="position:absolute;inset:0;background:rgba(8,5,13,0.38);border-radius:10px;"></div>'
    '<div style="position:absolute;bottom:0;left:50%;transform:translateX(-50%);width:60px;height:32px;border-radius:8px 8px 0 0;background:var(--color-background-page);box-shadow:0 -2px 12px rgba(8,5,13,0.2);"></div>'
    '</div>'
),

# Modal — small floating dialog card, no content blocking shapes
'modal': (
    '<div style="width:72px;height:80px;border-radius:14px;background:var(--color-background-page);'
    'box-shadow:0 4px 24px rgba(8,5,13,0.22),0 0 0 1px rgba(8,5,13,0.05);overflow:hidden;">'
    '<div style="height:24px;background:var(--primitive-violet-100);"></div>'
    '<div style="padding:8px 8px;display:flex;flex-direction:column;gap:4px;">'
    '<div style="width:40px;height:5px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:30px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:44px;height:16px;border-radius:999px;background:var(--color-action-default);margin-top:4px;"></div>'
    '</div></div>'
),

# Bottom sheet — grabber + minimal sheet shape
'bottom-sheet': (
    '<div style="width:96px;height:60px;border-radius:14px 14px 0 0;background:var(--color-background-page);'
    'box-shadow:0 -2px 18px rgba(8,5,13,0.18);display:flex;flex-direction:column;align-items:center;padding-top:10px;gap:10px;">'
    '<div style="width:32px;height:3px;border-radius:2px;background:var(--color-border-default);"></div>'
    '<div style="display:flex;gap:10px;">'
    + ''.join(f'<div style="width:22px;height:22px;border-radius:7px;background:var(--color-background-subtle);"></div>' for _ in range(3))
    + '</div></div>'
),

# DISPLAY ─────────────────────────────────────────────────────────────────────

# Avatar — real avatar CSS, overlapping facepile
'avatar': (
    '<div style="display:flex;">'
    + ''.join(
        f'<div class="avatar avatar--large avatar--circle" style="margin-left:{"-10" if i else "0"}px;'
        f'background:var(--primitive-{"violet" if i==0 else "citron" if i==1 else "berry"}-200);'
        f'color:var(--color-content-default);font-size:11px;font-weight:700;display:flex;align-items:center;justify-content:center;'
        f'box-shadow:0 0 0 2px var(--color-background-page);"></div>'
        for i in range(3)
    )
    + '</div>'
),

# Card — small card, real corner radius tokens, no blocking shapes
'card': (
    '<div style="width:80px;height:76px;border-radius:var(--corner-radius-l);background:var(--color-background-page);'
    'box-shadow:0 3px 18px rgba(8,5,13,0.16),0 0 0 1px rgba(8,5,13,0.04);overflow:hidden;">'
    '<div style="height:28px;background:var(--primitive-citron-100);"></div>'
    '<div style="padding:8px;display:flex;flex-direction:column;gap:4px;">'
    '<div style="width:44px;height:5px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:34px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '</div></div>'
),

# Card color block — card with accent left stripe
'card-color-block': (
    '<div style="width:80px;height:76px;border-radius:var(--corner-radius-l);background:var(--color-background-page);'
    'box-shadow:0 3px 18px rgba(8,5,13,0.16);overflow:hidden;display:flex;">'
    '<div style="width:6px;background:var(--color-action-default);flex-shrink:0;"></div>'
    '<div style="flex:1;padding:10px 8px;display:flex;flex-direction:column;gap:4px;">'
    '<div style="width:40px;height:5px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:30px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '</div></div>'
),

# Card media — card with image area on top
'card-media': (
    '<div style="width:80px;height:80px;border-radius:var(--corner-radius-l);background:var(--color-background-page);'
    'box-shadow:0 3px 18px rgba(8,5,13,0.16);overflow:hidden;">'
    '<div style="height:38px;background:var(--primitive-pool-100);display:flex;align-items:center;justify-content:center;">'
    '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" style="color:var(--primitive-pool-400);"><use href="#ico-cloud"/></svg>'
    '</div>'
    '<div style="padding:6px 8px;display:flex;flex-direction:column;gap:4px;">'
    '<div style="width:42px;height:5px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:30px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '</div></div>'
),

# Card multi — card with avatar + content
'card-multi': (
    '<div style="width:80px;height:80px;border-radius:var(--corner-radius-l);background:var(--color-background-page);'
    'box-shadow:0 3px 18px rgba(8,5,13,0.16);padding:8px;box-sizing:border-box;display:flex;flex-direction:column;gap:6px;">'
    '<div style="display:flex;align-items:center;gap:5px;">'
    '<div class="avatar avatar--small avatar--circle" style="width:18px;height:18px;background:var(--primitive-berry-200);"></div>'
    '<div style="width:32px;height:5px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '</div>'
    '<div style="width:52px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:42px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '<div style="width:48px;height:16px;border-radius:999px;background:var(--color-action-default);margin-top:auto;"></div>'
    '</div>'
),

# List — 3 rows (circle + line), real divider between
'list': (
    '<div style="display:flex;flex-direction:column;gap:0;background:var(--color-background-page);border-radius:var(--corner-radius-m);box-shadow:0 2px 14px rgba(8,5,13,0.12);overflow:hidden;width:110px;">'
    + ''.join(
        f'<div style="display:flex;align-items:center;gap:8px;padding:8px 10px;{"border-top:1px solid var(--color-border-subtle);" if i else ""}'
        f'{"background:var(--color-background-selection);" if i==1 else ""}">'
        f'<div class="avatar avatar--small avatar--circle" style="width:18px;height:18px;background:var(--primitive-{"violet" if i==0 else "pool" if i==1 else "berry"}-200);flex-shrink:0;"></div>'
        f'<div style="width:{28+i*4}px;height:5px;border-radius:999px;background:var(--color-border-{"default" if i==1 else "subtle"});"></div>'
        f'</div>'
        for i in range(3)
    )
    + '</div>'
),

# List accordion — real list-accordion CSS, one open
'list-accordion': (
    '<div style="background:var(--color-background-page);border-radius:var(--corner-radius-m);box-shadow:0 2px 14px rgba(8,5,13,0.12);overflow:hidden;width:110px;">'
    '<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-bottom:1px solid var(--color-border-subtle);">'
    '<div style="width:48px;height:6px;border-radius:999px;background:var(--color-content-default);opacity:0.5;"></div>'
    '<div class="list-accordion__control"><div class="list-accordion__control-inner" style="background:var(--color-action-hover-subtle);">'
    '<svg class="list-accordion__chevron" viewBox="0 0 24 24" width="14" height="14" fill="none" style="transform:rotate(180deg);"><use href="#ico-caret-dn"/></svg>'
    '</div></div>'
    '</div>'
    '<div style="padding:6px 10px;">'
    '<div style="width:40px;height:4px;border-radius:999px;background:var(--color-border-subtle);margin-bottom:4px;"></div>'
    '<div style="width:54px;height:4px;border-radius:999px;background:var(--color-border-subtle);"></div>'
    '</div>'
    '<div style="display:flex;align-items:center;justify-content:space-between;padding:8px 10px;border-top:1px solid var(--color-border-subtle);">'
    '<div style="width:40px;height:6px;border-radius:999px;background:var(--color-content-default);opacity:0.35;"></div>'
    '<div class="list-accordion__control"><div class="list-accordion__control-inner">'
    '<svg class="list-accordion__chevron" viewBox="0 0 24 24" width="14" height="14" fill="none"><use href="#ico-caret-dn"/></svg>'
    '</div></div>'
    '</div>'
    '</div>'
),

# Date picker — tiny calendar grid using pag-btn dots
'date-picker': (
    '<div style="display:grid;grid-template-columns:repeat(7,18px);gap:2px;">'
    + ''.join(
        f'<button class="pag-btn{"" if i!=16 else " pag-btn--selected"}" tabindex="-1" '
        f'style="pointer-events:none;width:18px;height:18px;padding:0;font-size:8px;min-width:0;border-radius:50%;">'
        f'{i+1 if i < 28 else ""}</button>'
        for i in range(28)
    )
    + '</div>'
),

# Divider — real divider CSS, 4 lines
'divider': (
    '<div style="display:flex;flex-direction:column;gap:10px;width:90px;">'
    '<hr class="divider" style="margin:0;">'
    '<hr class="divider" style="margin:0;">'
    '<hr class="divider divider--bold" style="margin:0;">'
    '<hr class="divider" style="margin:0;opacity:0.5;">'
    '</div>'
),

# Icon bullet — real icon-bullet CSS
'icon-bullet':
    '<div class="icon-bullet icon-bullet--xlarge" style="pointer-events:none;transform:scale(1.1);">'
    '<svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" style="color:currentColor;"><use href="#ico-fire"/></svg>'
    '</div>',

}

# ─── CSS ──────────────────────────────────────────────────────────────────────
NEW_CSS = '''
  /* comp-overview: floating component silhouette overlay */
  .cov-float {
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    pointer-events: none;
    z-index: 2;
    animation: cov-waft 6s ease-in-out infinite;
  }
  @keyframes cov-waft {
    0%   { transform: translateY(0px);  opacity: 0.92; }
    35%  { transform: translateY(-8px); opacity: 0.5;  }
    70%  { transform: translateY(-3px); opacity: 0.74; }
    100% { transform: translateY(0px);  opacity: 0.92; }
  }
'''

# ─── Build scene line ─────────────────────────────────────────────────────────
def make_scene(target, tile_idx):
    cat  = CATS[target]
    path = SHAPES[SHAPE_IDX.get(target, tile_idx % 6)]
    delay = -round((tile_idx * 1.37) % 6, 2)
    sa = 'viewBox="0 0 240 240" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"'
    bg1 = f'<svg class="ctt-bg-shape ctt-bg-shape--1" {sa}><path d="{path}"/></svg>'
    bg2 = f'<svg class="ctt-bg-shape ctt-bg-shape--2" {sa}><path d="{path}"/></svg>'
    ctr = f'<svg class="ctt-center-shape" {sa}><path d="{path}"/></svg>'
    flt = f'<div class="cov-float" style="animation-delay:{delay}s;">{FLOATS.get(target, "")}</div>'
    return f'<div class="ctt-scene ctt-scene--{cat}">{bg1}{bg2}{ctr}{flt}'

# ─── Inject ───────────────────────────────────────────────────────────────────
with open(FILE, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# CSS before </style>
for i, line in enumerate(lines):
    if line.strip() == '</style>' and i < 12000:
        lines.insert(i, NEW_CSS)
        print(f'  ✓ CSS injected at line {i+1}')
        break

target_pat = re.compile(r'data-nav-target="([^"]+)"')
modified = 0
tile_idx = 0

for i in range(len(lines)):
    m = target_pat.search(lines[i])
    if m and m.group(1) in CATS:
        target = m.group(1)
        for j in range(i+1, min(i+6, len(lines))):
            if 'ctt-scene' in lines[j] or 'cov-snap' in lines[j]:
                leading = re.match(r'^(\s*)', lines[j]).group(1)
                lines[j] = leading + make_scene(target, tile_idx) + '\n'
                print(f'  ✓ {target:22s} shape={SHAPE_IDX.get(target,0)} (line {j+1})')
                modified += 1
                tile_idx += 1
                break

print(f'\nTotal: {modified} tiles')
with open(FILE, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Done.')
