# Lab Room Pre-Order App
## Project Specification
## Need to use python i going to public it on a streamlit
# Overview

Build a modern, clean, responsive Lab Room Pre-Order application for students and lecturers to reserve laboratory rooms.

The design should be minimal, professional, and inspired by modern SaaS dashboards (Notion, Linear, Stripe, Vercel, Apple). Avoid outdated UI components.

---

# Design Style

## Theme

- Modern
- Clean
- Minimal
- Soft shadows
- Rounded corners (12-16px)
- Plenty of whitespace
- Smooth animations
- Glassmorphism only where appropriate
- Light mode first
- Dark mode support (optional)

## Color Palette

Primary
- Blue (#2563EB)

Secondary
- Indigo (#6366F1)

Success
- Green (#22C55E)

Warning
- Orange (#F59E0B)

Danger
- Red (#EF4444)

Background
- #F8FAFC

Cards
- White

Text
- #0F172A

Secondary Text
- #64748B

Border
- #E2E8F0

---

# Pages

1. Login
2. Home Dashboard
3. Lab Room List
4. Lab Room Detail
5. Pre-order Form
6. My Reservations
7. Profile (Optional)

---

# 1. Login Page

Simple centered login card.

Include:

- App logo
- App name
- Student ID field
- Password field
- Login button
- Remember me checkbox
- Forgot password
- Clean illustration on desktop

Style:

Rounded card

Soft shadow

Gradient background

Animated button hover

---

# 2. Home Dashboard

Top App Bar

Contains

- Logo
- User name
- Notification icon
- Profile avatar

Below

Greeting

Example

Good Morning,
John Doe

Quick Stats

Card 1

Available Labs

Card 2

My Reservations

Card 3

Today's Reservations

Card 4

Upcoming Reservations

Below

Quick Actions

- Browse Labs
- New Reservation
- My Reservations

Then

Recent Reservations

Card List

---

# 3. Lab Room List

Search bar

Filter

- Building
- Capacity
- Equipment

Sort

- Name
- Capacity
- Availability

Display labs as beautiful cards.

Each card contains

Room Name

Example

Lab A101

Image

Capacity

Building

Equipment icons

Current availability

Reserve button

Hover animation

---

# 4. Lab Room Detail (MOST IMPORTANT)

This is the most important page.

Top Section

Large room image

Room Name

Example

Computer Lab A101

Information

Building

Capacity

Computers

Projector

Air Conditioner

Whiteboard

Description

Reserve Button

---

## Weekly Reservation Schedule

Display a full weekly timetable.

Columns

Time | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday

Rows

Period 1

Period 2

Period 3

Period 4

Period 5

Period 6

Period 7

Period 8

Like this

| Period | Mon | Tue | Wed | Thu | Fri | Sat | Sun |
|---------|-----|-----|-----|-----|-----|-----|-----|
| P1 | Available | Reserved | Available | Available | Reserved | Available | Available |
| P2 | Reserved | Reserved | Available | Available | Available | Available | Reserved |
| P3 | Available | Available | Available | Reserved | Reserved | Available | Available |
| P4 | ... |

Each cell is interactive.

---

## Cell States

### Available

White background

Green border on hover

Cursor pointer

Click to reserve

---

### Reserved

Blue background

White text

Lock icon

Cannot click

Tooltip

Reserved by another user

---

### My Reservation

Green background

White text

Check icon

Can cancel

---

### Pending Approval

Orange background

Clock icon

---

### Current Time

Current period should have a subtle outline animation.

---

## Navigation

Previous Week

Current Week

Next Week

Display

Week 14

May 12 - May 18

---

## Legend

Green

My Reservation

Blue

Reserved

White

Available

Orange

Pending

---

## Clicking Available Cell

Open reservation modal.

---

# Reservation Modal

Room Name

Selected Date

Selected Period

Purpose

Textarea

Course

Dropdown

Lecturer

Dropdown

Number of Students

Submit button

Cancel button

---

# Reservation Validation

Cannot reserve

Already reserved periods

Past dates

Past periods

Maximum reservation limit

Show clear error messages.

---

# 5. Pre-order Page

Reservation Form

Fields

Room

Date

Start Period

End Period

Purpose

Course

Instructor

Student Count

Additional Notes

Submit

Confirmation dialog before submitting.

---

# 6. My Reservations

Table

Columns

Room

Date

Period

Status

Action

Status

Pending

Approved

Rejected

Completed

Cancelled

Action

View

Edit

Cancel

Search

Filter

Sort

---

# Components

Buttons

Primary

Secondary

Outlined

Danger

Cards

Rounded corners

Hover animation

Soft shadow

Inputs

Rounded

Modern

Focus ring

Dropdown

Searchable

Modal

Blur background

Fade animation

Toast Notification

Success

Error

Warning

Info

Loading Skeleton

For every page.

---

# Animations

Page transitions

200ms

Card hover

Scale 1.02

Buttons

Ripple effect

Modal

Fade + Scale

Table cells

Smooth color transition

Loading

Skeleton shimmer

---

# Responsive Design

Desktop

Tablet

Mobile

Weekly timetable should remain usable.

Desktop

Full table

Tablet

Horizontal scroll

Mobile

Horizontal scroll with sticky first column

---

# UX Requirements

Users should immediately understand:

Which slots are available

Which slots are occupied

Which reservations belong to them

How to reserve

How to cancel

Avoid unnecessary clicks.

---

# Suggested Tech Stack

Frontend

Flutter

State Management

Riverpod or Bloc

Backend

Firebase or Supabase

Database

Firestore or PostgreSQL

Authentication

Firebase Auth

---

# UI Inspiration

Use modern dashboard aesthetics similar to:

- Notion
- Linear
- Stripe Dashboard
- Vercel Dashboard
- Apple Human Interface Guidelines
- Material Design 3

Do NOT make the UI look like an old school management system.

---

# Extra Features (Nice to Have)

- Dark mode
- Room image gallery
- Equipment availability
- Reservation history
- Calendar view
- QR code for reservation confirmation
- Push notifications
- Favorite rooms
- Export reservation as PDF
- Real-time updates when another user books a slot
- Animated loading states
- Pull-to-refresh
- Empty state illustrations

---

# Important Requirement

The Weekly Reservation Schedule is the core feature of the application.

It should be:
- Highly readable
- Color-coded
- Interactive
- Fast
- Responsive
- Easy to understand at a glance

Users should instantly know:
- Which periods are available
- Which periods are reserved
- Which reservations belong to them
- Which periods are pending

This timetable should feel similar to a university scheduling system, with a polished, modern dashboard aesthetic rather than a basic HTML table.