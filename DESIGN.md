---
name: Precision Lab Systems
colors:
  surface: '#faf8ff'
  surface-dim: '#d9d9e5'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3fe'
  surface-container: '#ededf9'
  surface-container-high: '#e7e7f3'
  surface-container-highest: '#e1e2ed'
  on-surface: '#191b23'
  on-surface-variant: '#434655'
  inverse-surface: '#2e3039'
  inverse-on-surface: '#f0f0fb'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#4648d4'
  on-secondary: '#ffffff'
  secondary-container: '#6063ee'
  on-secondary-container: '#fffbff'
  tertiary: '#4d556b'
  on-tertiary: '#ffffff'
  tertiary-container: '#656d84'
  on-tertiary-container: '#eef0ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c0c1ff'
  on-secondary-fixed: '#07006c'
  on-secondary-fixed-variant: '#2f2ebe'
  tertiary-fixed: '#dae2fd'
  tertiary-fixed-dim: '#bec6e0'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465c'
  background: '#faf8ff'
  on-background: '#191b23'
  surface-variant: '#e1e2ed'
typography:
  headline-xl:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  headline-md:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base_unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  container_max_width: 1280px
  gutter: 24px
  margin_mobile: 16px
---

## Brand & Style

The design system is engineered for a Lab Room Pre-Order application, where the primary users are researchers, lab managers, and administrators who prioritize efficiency, clarity, and reliability. The brand personality is **Precise, Calm, and Highly Functional**, drawing inspiration from modern high-performance tools like Linear and Stripe.

The visual style follows a **Modern Minimalist** approach with a focus on "Functional Elegance." It utilizes heavy whitespace to reduce cognitive load in complex scheduling environments, high-quality typography for legibility of technical data, and subtle depth through soft shadows rather than heavy borders. The UI should evoke a sense of professional calm—making the act of securing a lab space feel seamless and error-free.

## Colors

The palette is rooted in a professional "Lab Blue" to establish trust and technical authority. 

- **Primary & Secondary:** A combination of Blue and Indigo is used for primary actions and active states, creating a vibrant but controlled focal point.
- **Neutrals:** The background uses a very cool Slate-50 (#F8FAFC) to differentiate from pure white surface cards. Text is set in a deep Slate-900 (#0F172A) to ensure maximum contrast and readability.
- **Status:** Standardized semantic colors for Success (available), Warning (pending), and Danger (occupied/canceled) follow rigorous accessibility standards.
- **Borders:** A subtle Slate-200 (#E2E8F0) is used for structural separation, keeping the interface feeling open and light.

## Typography

This design system utilizes a dual-font strategy to balance technical precision with readability. 

**Geist** is used for headlines and labels. Its technical, monospaced-influenced proportions provide a "developer-tool" feel that suits laboratory environments and data-rich headers. 

**Inter** is used for all body copy and long-form information. It provides a neutral, highly legible foundation that remains clear even at small sizes in dense scheduling tables.

- Use **Negative Letter Spacing** on large headlines to create a tight, premium feel.
- Use **Uppercase Labels** with slight tracking for category markers and metadata tags.

## Layout & Spacing

The layout follows a **Fluid Grid** model with strict adherence to an 8px spatial system (with a 4px half-step for tight components). 

- **Desktop:** 12-column grid with a 1280px max-width container. 24px gutters.
- **Tablet:** 8-column grid with 20px gutters.
- **Mobile:** 4-column grid with 16px gutters and side margins.

Spacing should be generous to maintain a high-end SaaS feel. Layouts should prioritize vertical stacking for lab details and horizontal "strip" layouts for time-slot selection. Use `xl` (32px) and `xxl` (48px) spacing for section transitions to maintain the minimal, airy aesthetic.

## Elevation & Depth

Visual hierarchy is established using **Tonal Layers** and **Ambient Shadows**. 

1. **Background (#F8FAFC):** The lowest layer.
2. **Surface Cards (#FFFFFF):** Raised via a subtle 1px border (#E2E8F0) and a soft, low-opacity shadow (e.g., `0 4px 6px -1px rgb(0 0 0 / 0.1)`).
3. **Floating Elements (Modals/Popovers):** Higher elevation with more diffused shadows and a backdrop blur of 8px to maintain focus.

Avoid heavy dark shadows. Instead, use "Indigo-tinted" shadows (adding a tiny amount of primary color to the shadow hex) to make the UI feel cohesive and modern.

## Shapes

The design system uses a **Rounded** shape language to soften the clinical nature of lab software.

- **Standard Elements (Inputs, Buttons):** 0.5rem (8px) radius.
- **Cards & Containers:** 1rem (16px) radius to create a distinct framing effect for lab sections.
- **Inner Elements:** When an element sits inside a container, its radius should be 4px smaller than the parent to maintain visual nesting harmony.

## Components

### Buttons
- **Primary:** Solid #2563EB with white text. Hover state: Scale 1.02 + slightly darker blue.
- **Secondary:** White background with #E2E8F0 border. Hover: Background becomes #F8FAFC.
- **Tertiary/Ghost:** No border or background. Highlighting on hover.

### Inputs & Forms
- **Fields:** 12px vertical padding. Focus state: 2px solid ring of #2563EB with an additional 2px transparent offset.
- **Labels:** Always Geist Medium, 14px, positioned above the input.

### Cards (Lab Rooms)
- White background, 16px corner radius, 1px border.
- Hover effect: Transition to a slightly deeper shadow and 1.02 scale for interactivity.

### Status Chips
- Small, rounded-pill shapes. Use light background tints of the semantic colors (e.g., Light Green background for "Available") with dark text of the same hue for maximum contrast and style.

### Navigation
- **Top-bar:** Fixed, #FFFFFF background with a subtle bottom border.
- **Active Links:** 2px bottom border in Primary Blue or a subtle background highlight.

### Scheduler / Time Slots
- Use a "slot" system. Available slots use a dashed #E2E8F0 border; selected slots use a solid #2563EB border with a light blue wash fill.