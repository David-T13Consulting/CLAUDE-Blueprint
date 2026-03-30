# Design System

> **This is the single source of truth for every visual decision.**
> Every component Claude builds must reference this file. No improvising colors, spacing, or typography.
> If it's not in this file, it doesn't get used.
>
> **Implementation**: Wire these tokens into your project's styling configuration (e.g., `tailwind.config.js`, CSS variables, theme file).
> Use your framework's token classes — never hardcode hex values or pixel sizes in components.

---

## Colors

### Core Palette

| Token | Hex | Usage |
|-------|-----|-------|
| `background` | `#FAFAFA` | App background, screen base |
| `surface` | `#FFFFFF` | Cards, sheets, elevated containers |
| `surface-secondary` | `#F5F5F5` | Subtle backgrounds, input fields, secondary surfaces |
| `text-primary` | `#1A1A1A` | Headings, body text, primary content |
| `text-secondary` | `#6B7280` | Captions, timestamps, supporting text |
| `text-tertiary` | `#9CA3AF` | Placeholders, disabled text |
| `border` | `#F3F4F6` | Subtle dividers, card borders (use sparingly) |

### Accent

| Token | Hex | Usage |
|-------|-----|-------|
| `accent` | `#6366F1` | Primary actions, links, active states |
| `accent-light` | `#EEF2FF` | Accent tint backgrounds, selected states |
| `accent-dark` | `#4F46E5` | Pressed states on accent elements |

### Semantic

| Token | Hex | Usage |
|-------|-----|-------|
| `error` | `#EF4444` | Error messages, destructive actions |
| `error-light` | `#FEF2F2` | Error background tint |
| `success` | `#10B981` | Success confirmations |
| `success-light` | `#ECFDF5` | Success background tint |
| `warning` | `#F59E0B` | Warnings, caution states |
| `warning-light` | `#FFFBEB` | Warning background tint |

### Rules
- **Never introduce a new color** without adding it here first
- **No opacity hacks** for creating lighter shades — use the defined `-light` tokens
- **Dark mode**: invert `background`→`#0F0F0F`, `surface`→`#1A1A1A`, `text-primary`→`#F5F5F5`. Full dark mode tokens TBD when dark mode is built

---

## Spacing

**Base unit: 4px.** All spacing must be a multiple of 4.

| Token | Value | Usage |
|-------|-------|-------|
| `space-1` | `4px` | Tight inline gaps (icon-to-text) |
| `space-2` | `8px` | Between related elements (label and input) |
| `space-3` | `12px` | Inner padding for compact components (pills, tags) |
| `space-4` | `16px` | Standard inner padding (cards, list items) |
| `space-5` | `20px` | Card inner padding (comfortable) |
| `space-6` | `24px` | Section padding, gap between cards |
| `space-8` | `32px` | Section separation within a screen |
| `space-10` | `40px` | Major section breaks |
| `space-12` | `48px` | Screen top/bottom padding |

### Example Mapping (Tailwind / NativeWind)

```
space-1  → p-1  / gap-1  / m-1
space-2  → p-2  / gap-2  / m-2
space-3  → p-3  / gap-3  / m-3
space-4  → p-4  / gap-4  / m-4
space-5  → p-5  / gap-5  / m-5
space-6  → p-6  / gap-6  / m-6
space-8  → p-8  / gap-8  / m-8
space-10 → p-10 / gap-10 / m-10
space-12 → p-12 / gap-12 / m-12
```

### Rules
- **No magic numbers.** Every spacing value comes from this scale
- **Consistent axis.** Vertical rhythm uses `space-6` as the default gap between elements in a list/feed
- **Screen padding.** Horizontal screen padding is always `space-4` (16px) on standard screens, `space-5` (20px) on detail/settings screens

---

## Typography

**Font: System default** (San Francisco on iOS). No custom fonts unless explicitly decided.

| Token | Size | Weight | Line Height | Usage |
|-------|------|--------|-------------|-------|
| `display` | `34px` | `700` (bold) | `40px` | Large screen titles (iOS large title style) |
| `heading-lg` | `28px` | `700` (bold) | `34px` | Section headers, screen titles |
| `heading` | `22px` | `600` (semibold) | `28px` | Card titles, modal titles |
| `heading-sm` | `18px` | `600` (semibold) | `24px` | Subsection headers |
| `body` | `16px` | `400` (regular) | `24px` | Primary body text, chat messages |
| `body-medium` | `16px` | `500` (medium) | `24px` | Emphasized body text, labels |
| `caption` | `13px` | `400` (regular) | `18px` | Timestamps, metadata, helper text |
| `caption-medium` | `13px` | `500` (medium) | `18px` | Badge labels, small emphasis |
| `tiny` | `11px` | `500` (medium) | `14px` | Legal text, version numbers (rare) |

### Example Mapping (Tailwind / NativeWind)

```
display       → text-[34px] font-bold leading-[40px]
heading-lg    → text-[28px] font-bold leading-[34px]
heading       → text-[22px] font-semibold leading-[28px]
heading-sm    → text-lg font-semibold leading-[24px]
body          → text-base font-normal leading-6
body-medium   → text-base font-medium leading-6
caption       → text-[13px] font-normal leading-[18px]
caption-medium→ text-[13px] font-medium leading-[18px]
tiny          → text-[11px] font-medium leading-[14px]
```

### Rules
- **Max 2 weights per screen.** Regular + semibold, or regular + bold. Never 3+.
- **No underlines** for emphasis — use weight or color instead
- **Body text is always 16px minimum.** Anything smaller is caption or metadata

---

## Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | `8px` | Small elements: inputs, tags, tooltips |
| `radius-md` | `12px` | Buttons, input fields |
| `radius-lg` | `16px` | Cards, sheets, modals |
| `radius-xl` | `20px` | Chat bubbles, large cards |
| `radius-full` | `9999px` | Pills, avatars, circular buttons |

### Example Mapping (Tailwind / NativeWind)

```
radius-sm   → rounded-lg
radius-md   → rounded-xl
radius-lg   → rounded-2xl
radius-xl   → rounded-[20px]
radius-full → rounded-full
```

### Rules
- **Cards are always `radius-lg` (16px)** minimum
- **Chat bubbles use `radius-xl` (20px)** with `radius-sm` (8px) on the tail-side corner
- **Buttons use `radius-md` (12px)** for rectangular, `radius-full` for pill-shaped
- **Never use sharp corners** (`rounded-none`) on interactive elements

---

## Shadows & Elevation

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.04)` | Subtle lift: input fields, inline elements |
| `shadow-md` | `0 2px 8px rgba(0,0,0,0.08)` | Standard cards, list items |
| `shadow-lg` | `0 4px 16px rgba(0,0,0,0.12)` | Elevated elements: floating input bar, FABs |
| `shadow-xl` | `0 8px 32px rgba(0,0,0,0.16)` | Modals, bottom sheets |

### Rules
- **Shadows over borders.** Use elevation to create depth, not outlines
- **If you add a border**, it's `1px border-[#F3F4F6]` — barely visible, never dark
- **No drop shadows on text**
- **Blur headers** use `backdrop-blur-xl` with `bg-white/80` instead of solid backgrounds

---

## Component Specifications

### Chat Bubbles

```
User message:
  background:     accent (#6366F1)
  text:           #FFFFFF
  alignment:      right
  max-width:      80%
  padding:        12px 16px
  border-radius:  20px (top-left, top-right, bottom-left), 8px (bottom-right)
  shadow:         none

Agent message:
  background:     surface-secondary (#F5F5F5)
  text:           text-primary (#1A1A1A)
  alignment:      left
  max-width:      80%
  padding:        12px 16px
  border-radius:  20px (top-left, top-right, bottom-right), 8px (bottom-left)
  shadow:         none
  icon:           Small agent avatar (20px), left of bubble, bottom-aligned
```

### Input Bar

```
container:
  position:       floating above keyboard
  margin:         0 16px 8px 16px
  background:     surface (#FFFFFF)
  border:         1px border (#F3F4F6)
  border-radius:  radius-full (pill when single-line), radius-lg (when multiline)
  padding:        8px 8px 8px 16px
  shadow:         shadow-lg

text input:
  font:           body (16px/400)
  placeholder:    text-tertiary (#9CA3AF)
  color:          text-primary (#1A1A1A)

send button:
  size:           36px circle
  background:     accent (#6366F1) when active, surface-secondary (#F5F5F5) when disabled
  icon:           arrow-up, #FFFFFF when active, text-tertiary when disabled
  border-radius:  radius-full
  animation:      scale(0.9) → scale(1) spring on tap, 150ms
```

### Cards (Tool Results, Settings)

```
container:
  background:     surface (#FFFFFF)
  border:         1px border (#F3F4F6)
  border-radius:  radius-lg (16px)
  padding:        space-5 (20px)
  shadow:         shadow-md
  margin:         0 (full-bleed within chat) or space-4 horizontal on settings screens

title:
  font:           heading-sm (18px/600)
  color:          text-primary
  margin-bottom:  space-2 (8px)

body:
  font:           body (16px/400)
  color:          text-secondary
```

### Buttons

```
Primary:
  background:     accent (#6366F1)
  text:           #FFFFFF, body-medium (16px/500)
  padding:        12px 24px
  border-radius:  radius-md (12px)
  shadow:         shadow-sm
  pressed:        accent-dark (#4F46E5), scale(0.97)

Secondary:
  background:     surface-secondary (#F5F5F5)
  text:           text-primary (#1A1A1A), body-medium (16px/500)
  padding:        12px 24px
  border-radius:  radius-md (12px)
  pressed:        border (#F3F4F6) bg, scale(0.97)

Destructive:
  background:     error-light (#FEF2F2)
  text:           error (#EF4444), body-medium (16px/500)
  padding:        12px 24px
  border-radius:  radius-md (12px)
  pressed:        error (#EF4444) bg, #FFFFFF text

All buttons:
  min-height:     44px (Apple HIG touch target)
  min-width:      44px
```

### Header / Navigation Bar

```
background:     bg-white/80 + backdrop-blur-xl (frosted glass)
border-bottom:  none (no visible border — blur handles separation)
title:          heading-sm (18px/600), centered
height:         44px (content) + safe area inset top
```

### Thinking Indicator

```
container:
  alignment:      left, same position as agent message
  padding:        12px 16px

animation:
  3 dots, 6px each, rounded-full
  color:          text-tertiary (#9CA3AF)
  animation:      sequential opacity pulse 0.3 → 1.0 → 0.3
  duration:       1200ms per cycle
  stagger:        200ms between dots
  easing:         ease-in-out
```

### Empty State / Greeting

```
container:
  centered vertically (offset slightly above true center — 40% from top)
  padding:        space-6 (24px) horizontal

greeting:
  text:           "What can I help you with?"
  font:           heading-lg (28px/700)
  color:          text-primary (#1A1A1A)

suggested prompts:
  layout:         vertical stack, gap space-2 (8px)
  count:          2-3 prompts
  style:          pill — surface-secondary bg, text-secondary text
  padding:        12px 16px
  border-radius:  radius-full
  font:           body (16px/400)
  pressed:        accent-light bg, accent text
```

---

## Animation Tokens

Use your framework's recommended animation library (e.g., `react-native-reanimated`, `framer-motion`, CSS transitions).

| Token | Duration | Easing | Usage |
|-------|----------|--------|-------|
| `anim-fast` | `150ms` | `spring(damping: 15, stiffness: 150)` | Button presses, micro-interactions |
| `anim-normal` | `300ms` | `ease-out` | Message appear, fade in |
| `anim-slow` | `500ms` | `ease-in-out` | Screen transitions, large reveals |
| `anim-loop` | `1200ms` | `ease-in-out` | Thinking indicator, pulsing states |

### Message Entrance

```
initial:    opacity: 0, translateY: 8px
final:      opacity: 1, translateY: 0
duration:   anim-normal (300ms)
easing:     ease-out
stagger:    50ms between consecutive messages (on initial load only)
```

### Tool Result Card Entrance

```
initial:    opacity: 0, height: 0
final:      opacity: 1, height: auto
duration:   250ms
easing:     spring(damping: 20, stiffness: 200)
```

---

## Iconography

| Rule | Specification |
|------|--------------|
| **Library** | `lucide-react-native` (consistent stroke weight) |
| **Default size** | `20px` |
| **Stroke width** | `1.5px` |
| **Color** | Inherits from text color of context — never independently colored unless semantic (error, success) |
| **Touch target** | Icon buttons always have 44x44px minimum hit area, even if icon is 20px |

### Rules
- **Max 3 icons visible** on any single screen (excluding nav)
- **No decorative icons.** Every icon must communicate a function
- **Pair with text** when the icon's meaning isn't universally obvious

---

## Accessibility Minimums

| Rule | Value |
|------|-------|
| Text contrast ratio | ≥ 4.5:1 against background |
| Large text contrast | ≥ 3:1 (heading-lg and above) |
| Touch target | 44 × 44px minimum |
| Focus indicator | 2px accent ring |
| Dynamic Type | All text tokens scale with system font size preference |
| Motion | Respect `prefers-reduced-motion` — disable non-essential animations |

---

## Quick Reference — The "Never Do" List

1. Never use a color not defined in this file
2. Never use spacing that isn't a multiple of 4px
3. Never go below 16px for readable body text
4. Never use borders when a shadow would work
5. Never use more than 2 font weights on one screen
6. Never use sharp corners on interactive elements
7. Never animate without purpose
8. Never put more than 2 primary action buttons on one screen
9. Never use a centered modal when a bottom sheet would work
10. Never make a touch target smaller than 44×44px
