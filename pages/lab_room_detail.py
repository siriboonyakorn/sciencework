"""
Lab Room Detail — room info + weekly reservation schedule (core feature).
"""
import streamlit as st
from components.navbar import render_navbar
from data.mock_data import LABS, PERIODS, DAYS, DAYS_SHORT, get_schedule, get_week_dates

# ── Navbar ───────────────────────────────────────────────────────────────────
render_navbar()

# ── Get selected lab ─────────────────────────────────────────────────────────
lab = st.session_state.get("selected_lab")

if not lab:
    st.markdown("""
    <div style="text-align: center; padding: 4rem 1rem;">
        <div style="font-size: 3rem; margin-bottom: 1rem;">🔬</div>
        <h2 style="color: #0F172A; font-weight: 600; margin-bottom: 0.5rem;">
            No Lab Selected</h2>
        <p style="color: #64748B; font-size: 0.9rem;">
            Please select a lab room from the Lab Rooms page.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("← Browse Labs", type="primary"):
        st.switch_page("pages/lab_rooms.py")
    st.stop()

# ── Week navigation state ───────────────────────────────────────────────────
if "week_offset" not in st.session_state:
    st.session_state.week_offset = 0

# ── Back button ──────────────────────────────────────────────────────────────
if st.button("← Back to Lab Rooms", type="secondary"):
    st.switch_page("pages/lab_rooms.py")

st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)

# ── Room Header ──────────────────────────────────────────────────────────────
equip_tags = " ".join(
    [f'<span style="background:#F1F5F9;padding:4px 10px;border-radius:8px;'
     f'font-size:0.78rem;color:#64748B;white-space:nowrap;">{e}</span>'
     for e in lab["equipment"]]
)

st.markdown(f"""
<div class="custom-card-static animate-in" style="margin-bottom: 1.5rem;">
    <div style="display: flex; gap: 1.25rem; align-items: flex-start; flex-wrap: wrap;">
        <div style="
            width: 72px; height: 72px;
            background: linear-gradient(135deg, #DBEAFE 0%, #E0E7FF 100%);
            border-radius: 16px;
            display: flex; align-items: center; justify-content: center;
            font-size: 2.2rem;
            flex-shrink: 0;
        ">{lab['icon']}</div>

        <div style="flex: 1; min-width: 200px;">
            <h1 style="
                font-size: 1.4rem; font-weight: 700; color: #0F172A;
                margin: 0 0 0.35rem 0; line-height: 1.2;
            ">{lab['name']}</h1>
            <div style="display: flex; flex-wrap: wrap; gap: 1rem;
                        font-size: 0.85rem; color: #64748B; margin-bottom: 0.75rem;">
                <span>📍 {lab['building']} · {lab['floor']}</span>
                <span>👥 {lab['capacity']} seats</span>
            </div>
            <p style="font-size: 0.85rem; color: #94A3B8; margin: 0 0 0.75rem 0;
                      line-height: 1.5;">
                {lab['description']}
            </p>
            <div style="display: flex; flex-wrap: wrap; gap: 6px;">
                {equip_tags}
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Weekly Schedule ──────────────────────────────────────────────────────────
st.markdown('<div class="section-title animate-in">📅 Weekly Reservation Schedule</div>',
            unsafe_allow_html=True)

# Week navigation
nav_c1, nav_c2, nav_c3 = st.columns([1, 2, 1])
with nav_c1:
    if st.button("◀ Previous", use_container_width=True, type="secondary"):
        st.session_state.week_offset -= 1
        st.rerun()
with nav_c3:
    if st.button("Next ▶", use_container_width=True, type="secondary"):
        st.session_state.week_offset += 1
        st.rerun()

week_info = get_week_dates(st.session_state.week_offset)
with nav_c2:
    st.markdown(f"""
    <div style="text-align: center; padding: 0.5rem 0;">
        <div style="font-weight: 600; color: #0F172A; font-size: 0.95rem;">
            Week {week_info['week_number']}</div>
        <div style="font-size: 0.78rem; color: #64748B;">
            {week_info['start']} — {week_info['end']}</div>
    </div>
    """, unsafe_allow_html=True)

if st.session_state.week_offset != 0:
    _, reset_col, _ = st.columns([2, 1, 2])
    with reset_col:
        if st.button("↻ Current Week", use_container_width=True, type="secondary"):
            st.session_state.week_offset = 0
            st.rerun()

st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)

# Generate schedule
schedule = get_schedule(lab["id"], st.session_state.week_offset)

# ── Build the schedule HTML table ────────────────────────────────────────────
cell_styles = {
    "available": (
        "background:#FFFFFF;color:#64748B;cursor:pointer;"
        "border:1px solid #E2E8F0;"
    ),
    "reserved": (
        "background:linear-gradient(135deg,#2563EB,#1D4ED8);color:white;"
        "border:1px solid #1E40AF;"
    ),
    "my_reservation": (
        "background:linear-gradient(135deg,#22C55E,#16A34A);color:white;"
        "border:1px solid #15803D;"
    ),
    "pending": (
        "background:linear-gradient(135deg,#F59E0B,#D97706);color:white;"
        "border:1px solid #B45309;"
    ),
}

cell_labels = {
    "available": "Available",
    "reserved": "🔒 Reserved",
    "my_reservation": "✓ Mine",
    "pending": "⏳ Pending",
}

# Build header
header_cells = '<th style="padding:12px 8px;background:#F8FAFC;color:#64748B;font-weight:600;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;border-bottom:2px solid #E2E8F0;min-width:55px;text-align:center;">Period</th>'
for j, day in enumerate(DAYS):
    date_str = week_info["dates"][day]
    header_cells += f'''<th style="padding:12px 8px;background:#F8FAFC;color:#64748B;font-weight:600;font-size:0.72rem;text-transform:uppercase;letter-spacing:0.06em;border-bottom:2px solid #E2E8F0;min-width:90px;text-align:center;">
        <div>{DAYS_SHORT[j]}</div>
        <div style="font-weight:400;font-size:0.68rem;color:#94A3B8;margin-top:2px;">{date_str}</div>
    </th>'''

# Build rows
body_rows = ""
for period in PERIODS:
    row = f'''<td style="padding:10px 8px;background:#FAFBFC;border-bottom:1px solid #F1F5F9;text-align:center;white-space:nowrap;">
        <div style="font-weight:600;color:#0F172A;font-size:0.85rem;">{period['short']}</div>
        <div style="font-size:0.68rem;color:#94A3B8;">{period['start']}-{period['end']}</div>
    </td>'''

    for day in DAYS:
        cell = schedule[day][period["id"]]
        status = cell["status"]
        style = cell_styles[status]
        label = cell_labels[status]

        tooltip = ""
        if status == "reserved":
            tooltip = f'title="Reserved by {cell.get("reserved_by", "—")} — {cell.get("course", "")}"'
        elif status in ("my_reservation", "pending"):
            tooltip = f'title="{cell.get("course", "")}"'

        row += f'''<td {tooltip} style="
            {style}
            padding:10px 6px;
            text-align:center;
            border-radius:8px;
            font-size:0.75rem;
            font-weight:500;
            transition:all 0.2s ease;
            vertical-align:middle;
        ">{label}</td>'''

    body_rows += f"<tr>{row}</tr>"

# Full table
st.markdown(f"""
<div class="custom-card-static" style="padding:0;overflow-x:auto;">
    <table style="width:100%;border-collapse:separate;border-spacing:4px;padding:8px;">
        <thead><tr>{header_cells}</tr></thead>
        <tbody>{body_rows}</tbody>
    </table>
</div>
""", unsafe_allow_html=True)

# ── Legend ───────────────────────────────────────────────────────────────────
st.markdown("""
<div style="
    display: flex; flex-wrap: wrap; gap: 1rem;
    margin-top: 1rem; padding: 0.75rem 1rem;
    background: #FAFBFC; border-radius: 10px; border: 1px solid #F1F5F9;
    font-size: 0.78rem;
">
    <div style="display:flex;align-items:center;gap:6px;">
        <div style="width:14px;height:14px;background:white;border:1px solid #E2E8F0;border-radius:4px;"></div>
        <span style="color:#64748B;">Available</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;">
        <div style="width:14px;height:14px;background:linear-gradient(135deg,#2563EB,#1D4ED8);border-radius:4px;"></div>
        <span style="color:#64748B;">Reserved</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;">
        <div style="width:14px;height:14px;background:linear-gradient(135deg,#22C55E,#16A34A);border-radius:4px;"></div>
        <span style="color:#64748B;">My Reservation</span>
    </div>
    <div style="display:flex;align-items:center;gap:6px;">
        <div style="width:14px;height:14px;background:linear-gradient(135deg,#F59E0B,#D97706);border-radius:4px;"></div>
        <span style="color:#64748B;">Pending</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ── Quick Reserve Form ───────────────────────────────────────────────────────
st.markdown('<div class="section-title">📝 Make a Reservation</div>', unsafe_allow_html=True)

with st.form("quick_reserve_form"):
    qr1, qr2 = st.columns(2)
    with qr1:
        selected_day = st.selectbox("Day", DAYS)
    with qr2:
        period_options = [f"{p['short']} ({p['start']} - {p['end']})" for p in PERIODS]
        selected_period_str = st.selectbox("Period", period_options)

    purpose = st.text_area(
        "Purpose",
        placeholder="e.g. CS201 Lab session on linked lists",
        height=80,
    )

    qr3, qr4 = st.columns(2)
    with qr3:
        from data.mock_data import COURSES
        course = st.selectbox("Course", ["Select a course..."] + COURSES)
    with qr4:
        from data.mock_data import INSTRUCTORS
        instructor = st.selectbox("Instructor", ["Select an instructor..."] + INSTRUCTORS)

    student_count = st.number_input("Number of Students", min_value=1,
                                    max_value=lab["capacity"], value=20)

    reserve_submitted = st.form_submit_button("Submit Reservation", use_container_width=True)

if reserve_submitted:
    # Validate
    selected_period_id = period_options.index(selected_period_str) + 1
    cell_status = schedule[selected_day][selected_period_id]["status"]

    if cell_status == "reserved":
        st.error("❌ This slot is already reserved by another user.")
    elif cell_status == "my_reservation":
        st.warning("⚠️ You already have a reservation for this slot.")
    elif cell_status == "pending":
        st.warning("⚠️ You already have a pending reservation for this slot.")
    elif not purpose.strip():
        st.error("⚠️ Please enter a purpose for the reservation.")
    elif course == "Select a course...":
        st.error("⚠️ Please select a course.")
    elif instructor == "Select an instructor...":
        st.error("⚠️ Please select an instructor.")
    else:
        st.success(
            f"✅ Reservation submitted for **{lab['name']}** — "
            f"**{selected_day}**, **{selected_period_str}**\n\n"
            f"Status: *Pending approval*"
        )
        st.balloons()
