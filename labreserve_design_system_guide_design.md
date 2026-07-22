---
name: Precision Lab Systems (LabReserve)
description: A modern, minimal, and professional SaaS-inspired design system for laboratory room management.
---

# Precision Lab Systems (LabReserve)

LabReserve is built on a foundation of clarity, precision, and efficiency. The visual language is inspired by high-performance SaaS platforms like Notion, Linear, and Stripe, focusing on high-contrast typography, generous whitespace, and a refined functional aesthetic.

## 1. Brand Identity
The LabReserve brand conveys reliability and technological sophistication. The logo is a minimalist geometric lab flask with a nested 'R', symbolizing the intersection of science and scheduling.

## 2. Color Palette

### Primary & Functional
- **Primary Blue (#2563EB):** Action-oriented, used for primary buttons, active states, and focus indicators.
- **Secondary Indigo (#6366F1):** Supporting brand color for secondary actions and accents.
- **Success Green (#22C55E):** Used for 'Available' states, 'My Reservation' highlights, and success confirmations.
- **Warning Orange (#F59E0B):** Used for 'Pending Approval' states and cautionary alerts.
- **Danger Red (#EF4444):** Reserved for destructive actions (Delete, Cancel) and error states.

### Neutral & Surfaces
- **Background (#F8FAFC):** The foundational page background color for a clean, light feel.
- **Surface/Cards (#FFFFFF):** Elevated surfaces with soft shadows for content organization.
- **Text (Primary: #0F172A):** High-contrast dark navy for maximum readability.
- **Text (Secondary: #64748B):** Muted slate for metadata, captions, and placeholders.
- **Border (#E2E8F0):** Subtle strokes for defining component boundaries without visual clutter.

## 3. Typography
The system uses **Geist** (or Inter as a fallback), a modern sans-serif optimized for technical interfaces and legibility.

- **Headlines:** Semi-bold or Bold, tight letter-spacing, Slate-900.
- **Body:** Regular weight, Slate-700/800 for high readability.
- **Labels:** Medium weight, uppercase or small-caps for utility navigation.
- **Monospace:** Used for Lab IDs (e.g., A101) to convey a technical, precise feel.

## 4. Layout & Spacing
- **Grid System:** 12-column responsive grid for desktop.
- **Corner Radius:** Standardized at **12-16px** for a modern, approachable feel.
- **Shadows:** Soft, multi-layered shadows to provide depth without heavy borders.
- **Whitespace:** Prioritize "breathe" around content to reduce cognitive load during scheduling.

## 5. Component Patterns

### Navigation
- **Side Navigation:** Fixed left-hand bar. Features the brand logo, primary "New Reservation" CTA, and categorized links (Dashboard, Browse, My Reservations, Settings).
- **Top Navigation:** Contains breadcrumbs, global search, notifications, and user profile avatar.

### Cards
- **Stat Cards:** Simple, high-impact cards for dashboard metrics.
- **Lab Cards:** Image-centric cards with metadata (Capacity, Building) and clear "View Details" actions.

### Data Inputs
- **Form Fields:** Rounded corners, subtle borders, and a Primary Blue focus ring.
- **Status Badges:** Rounded "pill" style badges with semi-transparent backgrounds matching the functional color logic (e.g., Green for 'Completed').

### Timetable (Core Feature)
- **Grid-based:** 8-period vertical axis, 7-day horizontal axis.
- **States:**
  - *White/Clear:* Available
  - *Solid Blue:* Reserved (Occupied)
  - *Solid Green:* My Reservation
  - *Solid Orange:* Pending Approval

## 6. Motion & Interaction
- **Scale Hover:** 1.02x scale transition for buttons and interactive cards.
- **Fade Transitions:** Smooth 200ms opacity shifts between page views.
- **Focus States:** High-visibility blue outlines for keyboard accessibility.

## 7. Accessibility
- All text meets WCAG AA contrast standards.
- Interactive elements have a minimum touch target of 44x44px for mobile users.
- Meaningful use of icons (lock for reserved, clock for pending) to supplement color-based information.