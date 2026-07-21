"""
Pre-order / New Reservation page — full reservation form.
"""
import streamlit as st
from datetime import datetime, timedelta
from components.navbar import render_navbar
from data.mock_data import LABS, PERIODS, COURSES, INSTRUCTORS

# ── Navbar ───────────────────────────────────────────────────────────────────
render_navbar()

# ── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="animate-in" style="margin-bottom: 1.5rem;">
    <h1 style="
        font-size: 1.5rem; font-weight: 700; color: #0F172A;
        margin: 0 0 0.35rem 0; letter-spacing: -0.02em;
    ">📝 New Reservation</h1>
    <p style="font-size: 0.875rem; color: #64748B; margin: 0;">
        Fill in the details below to reserve a lab room.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Reservation Form ────────────────────────────────────────────────────────
with st.form("preorder_form"):
    # ── Room Selection ───────────────────────────────────────────────────
    st.markdown("""
    <div style="font-weight:600;color:#0F172A;font-size:0.9rem;margin-bottom:0.25rem;">
        🔬 Room Details
    </div>
    """, unsafe_allow_html=True)

    lab_options = {f"{l['icon']} {l['name']} ({l['building']})": l for l in LABS}
    selected_lab_name = st.selectbox(
        "Lab Room",
        list(lab_options.keys()),
        help="Select the lab room you want to reserve.",
    )
    selected_lab = lab_options[selected_lab_name]

    # Show selected lab info
    st.markdown(f"""
    <div style="
        background: #F0F9FF; border-radius: 10px; padding: 0.75rem 1rem;
        border: 1px solid #BAE6FD; margin-bottom: 0.5rem;
        font-size: 0.82rem; color: #0369A1;
    ">
        📍 {selected_lab['building']} · {selected_lab['floor']} &nbsp;|&nbsp;
        👥 Capacity: {selected_lab['capacity']} &nbsp;|&nbsp;
        {' · '.join(selected_lab['equipment'][:3])}
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="custom-divider" style="margin:1rem 0;"></div>',
                unsafe_allow_html=True)

    # ── Date & Period ────────────────────────────────────────────────────
    st.markdown("""
    <div style="font-weight:600;color:#0F172A;font-size:0.9rem;margin-bottom:0.25rem;">
        📅 Date & Time
    </div>
    """, unsafe_allow_html=True)

    d_col1, d_col2 = st.columns(2)
    with d_col1:
        reservation_date = st.date_input(
            "Date",
            min_value=datetime.now().date(),
            max_value=datetime.now().date() + timedelta(days=60),
            value=datetime.now().date() + timedelta(days=1),
        )
    with d_col2:
        period_options = [f"{p['short']} — {p['start']} to {p['end']}" for p in PERIODS]
        selected_period = st.selectbox("Period", period_options)

    st.markdown('<div class="custom-divider" style="margin:1rem 0;"></div>',
                unsafe_allow_html=True)

    # ── Course Details ───────────────────────────────────────────────────
    st.markdown("""
    <div style="font-weight:600;color:#0F172A;font-size:0.9rem;margin-bottom:0.25rem;">
        📚 Course Details
    </div>
    """, unsafe_allow_html=True)

    c_col1, c_col2 = st.columns(2)
    with c_col1:
        course = st.selectbox("Course", ["Select a course..."] + COURSES)
    with c_col2:
        instructor = st.selectbox("Instructor", ["Select an instructor..."] + INSTRUCTORS)

    student_count = st.number_input(
        "Number of Students",
        min_value=1,
        max_value=selected_lab["capacity"],
        value=min(20, selected_lab["capacity"]),
        help=f"Maximum capacity for this room: {selected_lab['capacity']}",
    )

    st.markdown('<div class="custom-divider" style="margin:1rem 0;"></div>',
                unsafe_allow_html=True)

    # ── Purpose & Notes ──────────────────────────────────────────────────
    st.markdown("""
    <div style="font-weight:600;color:#0F172A;font-size:0.9rem;margin-bottom:0.25rem;">
        💬 Additional Info
    </div>
    """, unsafe_allow_html=True)

    purpose = st.text_area(
        "Purpose of Reservation",
        placeholder="e.g. CS201 Lab Session — Data Structures practicum on linked lists and trees",
        height=100,
    )
    notes = st.text_area(
        "Additional Notes (optional)",
        placeholder="e.g. Need extra whiteboard markers, will use room for 2 consecutive periods",
        height=68,
    )

    st.markdown('<div style="height:0.75rem;"></div>', unsafe_allow_html=True)

    # ── Summary before submit ────────────────────────────────────────────
    day_name = reservation_date.strftime("%A")
    st.markdown(f"""
    <div style="
        background: #FFFBEB; border-radius: 10px; padding: 0.85rem 1rem;
        border: 1px solid #FDE68A; margin-bottom: 0.75rem;
    ">
        <div style="font-size: 0.82rem; font-weight: 600; color: #92400E;
                    margin-bottom: 0.35rem;">📋 Reservation Summary</div>
        <div style="font-size: 0.8rem; color: #78350F; line-height: 1.7;">
            <b>Room:</b> {selected_lab['name']}<br>
            <b>Date:</b> {reservation_date.strftime('%B %d, %Y')} ({day_name})<br>
            <b>Period:</b> {selected_period}<br>
            <b>Students:</b> {student_count}
        </div>
    </div>
    """, unsafe_allow_html=True)

    submitted = st.form_submit_button("📨 Submit Reservation", use_container_width=True)

# ── Handle submission ────────────────────────────────────────────────────────
if submitted:
    errors = []
    if course == "Select a course...":
        errors.append("Please select a course.")
    if instructor == "Select an instructor...":
        errors.append("Please select an instructor.")
    if not purpose.strip():
        errors.append("Please enter a purpose for the reservation.")
    if reservation_date < datetime.now().date():
        errors.append("Cannot reserve for a past date.")

    if errors:
        for err in errors:
            st.error(f"⚠️ {err}")
    else:
        st.success(
            f"✅ **Reservation submitted successfully!**\n\n"
            f"**{selected_lab['name']}** — {reservation_date.strftime('%B %d, %Y')} "
            f"({day_name}), {selected_period}\n\n"
            f"Your reservation is now **pending approval**. "
            f"You'll be notified once it's reviewed."
        )
        st.balloons()
