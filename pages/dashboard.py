"""
Home Dashboard — greeting, stats, quick actions, recent reservations.
"""
import streamlit as st
from datetime import datetime
from components.navbar import render_navbar
from data.mock_data import get_dashboard_stats, get_user_reservations, LABS

# ── Navbar ───────────────────────────────────────────────────────────────────
render_navbar()

# ── Greeting ─────────────────────────────────────────────────────────────────
hour = datetime.now().hour
if hour < 12:
    greeting = "Good Morning"
    emoji = "☀️"
elif hour < 17:
    greeting = "Good Afternoon"
    emoji = "🌤️"
else:
    greeting = "Good Evening"
    emoji = "🌙"

user = st.session_state.get("user", {})
name = user.get("name", "User").split()[0]

st.markdown(f"""
<div class="animate-in" style="margin-bottom: 1.75rem;">
    <div style="font-size: 0.85rem; color: #64748B; margin-bottom: 0.25rem;">
        {emoji} {greeting}
    </div>
    <h1 style="
        font-size: 1.65rem; font-weight: 700; color: #0F172A;
        margin: 0; line-height: 1.25; letter-spacing: -0.02em;
    ">{name}, welcome to LabRoom</h1>
</div>
""", unsafe_allow_html=True)

# ── Stats Cards ──────────────────────────────────────────────────────────────
stats = get_dashboard_stats()

col1, col2, col3, col4 = st.columns(4)

stat_data = [
    (col1, stats["available_labs"], "Available Labs", "🔬", "#DBEAFE", "#2563EB"),
    (col2, stats["my_reservations"], "My Reservations", "📋", "#DCFCE7", "#22C55E"),
    (col3, stats["today_reservations"], "Today", "📅", "#FEF3C7", "#F59E0B"),
    (col4, stats["upcoming"], "Upcoming", "⏰", "#E0E7FF", "#6366F1"),
]

for col, value, label, icon, bg_color, accent in stat_data:
    with col:
        st.markdown(f"""
        <div class="stat-card animate-in">
            <div class="stat-icon" style="background: {bg_color};">{icon}</div>
            <div class="stat-value" style="color: {accent};">{value}</div>
            <div class="stat-label">{label}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('<div style="height: 1rem;"></div>', unsafe_allow_html=True)

# ── Quick Actions ────────────────────────────────────────────────────────────
st.markdown('<div class="section-title">⚡ Quick Actions</div>', unsafe_allow_html=True)

qa1, qa2, qa3 = st.columns(3)
with qa1:
    if st.button("🔬 Browse Labs", use_container_width=True, type="secondary"):
        st.switch_page("pages/lab_rooms.py")
with qa2:
    if st.button("📝 New Reservation", use_container_width=True, type="secondary"):
        st.switch_page("pages/preorder.py")
with qa3:
    if st.button("📋 My Reservations", use_container_width=True, type="secondary"):
        st.switch_page("pages/my_reservations.py")

st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)

# ── Recent Reservations ─────────────────────────────────────────────────────
st.markdown('<div class="section-title">📋 Recent Reservations</div>', unsafe_allow_html=True)

reservations = get_user_reservations()

if not reservations:
    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem; color: #94A3B8;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📭</div>
        <div style="font-weight: 500;">No reservations yet</div>
        <div style="font-size: 0.85rem; margin-top: 0.25rem;">
            Browse labs and make your first reservation!</div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Build table rows
    status_badges = {
        "approved": '<span class="badge badge-success">✓ Approved</span>',
        "pending": '<span class="badge badge-warning">⏳ Pending</span>',
        "rejected": '<span class="badge badge-danger">✗ Rejected</span>',
        "completed": '<span class="badge badge-neutral">✓ Completed</span>',
        "cancelled": '<span class="badge badge-neutral">— Cancelled</span>',
    }

    rows_html = ""
    for r in reservations[:5]:  # Show last 5
        badge = status_badges.get(r["status"], "")
        rows_html += f"""
        <tr>
            <td style="font-weight: 500;">{r['lab_name']}</td>
            <td>{r['date']}</td>
            <td>P{r['period']} · {r['period_time']}</td>
            <td>{badge}</td>
            <td style="color: #64748B; font-size: 0.8rem;">{r['purpose'][:30]}...</td>
        </tr>
        """

    st.markdown(f"""
    <div class="custom-card-static" style="padding: 0; overflow: hidden;">
        <table class="reservation-table">
            <thead>
                <tr>
                    <th>Lab Room</th>
                    <th>Date</th>
                    <th>Period</th>
                    <th>Status</th>
                    <th>Purpose</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)
    if st.button("View all reservations →", type="secondary"):
        st.switch_page("pages/my_reservations.py")

# ── Available Labs Preview ───────────────────────────────────────────────────
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">🔬 Available Labs</div>', unsafe_allow_html=True)

lab_cols = st.columns(3)
for i, lab in enumerate(LABS[:3]):
    with lab_cols[i]:
        equip_tags = " ".join(
            [f'<span style="background:#F1F5F9;padding:2px 8px;border-radius:6px;'
             f'font-size:0.7rem;color:#64748B;white-space:nowrap;">{e}</span>'
             for e in lab["equipment"][:3]]
        )
        st.markdown(f"""
        <div class="custom-card" style="cursor: pointer;">
            <div style="font-size: 2rem; margin-bottom: 0.75rem;">{lab['icon']}</div>
            <div style="font-weight: 600; color: #0F172A; font-size: 0.95rem;
                        margin-bottom: 0.25rem;">{lab['name']}</div>
            <div style="font-size: 0.8rem; color: #64748B;
                        margin-bottom: 0.75rem;">{lab['building']} · {lab['capacity']} seats</div>
            <div style="display: flex; flex-wrap: wrap; gap: 4px; margin-bottom: 0.75rem;">
                {equip_tags}
            </div>
            <div>
                <span class="badge badge-success">
                    {lab['available_count']} slots available
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)
