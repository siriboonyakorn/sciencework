"""
My Reservations — view, filter, and manage all reservations.
"""
import streamlit as st
from components.navbar import render_navbar
from data.mock_data import get_user_reservations

# ── Navbar ───────────────────────────────────────────────────────────────────
render_navbar()

# ── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="animate-in" style="margin-bottom: 1.5rem;">
    <h1 style="
        font-size: 1.5rem; font-weight: 700; color: #0F172A;
        margin: 0 0 0.35rem 0; letter-spacing: -0.02em;
    ">📋 My Reservations</h1>
    <p style="font-size: 0.875rem; color: #64748B; margin: 0;">
        Track and manage all your lab room reservations.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Get reservations ─────────────────────────────────────────────────────────
reservations = get_user_reservations()

# ── Status tabs ──────────────────────────────────────────────────────────────
tab_all, tab_active, tab_pending, tab_past = st.tabs(
    ["All", "Active", "Pending", "Past"]
)

def _filter_by(statuses):
    return [r for r in reservations if r["status"] in statuses]

tab_data = {
    "All": reservations,
    "Active": _filter_by(["approved"]),
    "Pending": _filter_by(["pending"]),
    "Past": _filter_by(["completed", "rejected", "cancelled"]),
}

tabs = [tab_all, tab_active, tab_pending, tab_past]
tab_names = list(tab_data.keys())

# ── Status badge helper ──────────────────────────────────────────────────────
STATUS_BADGES = {
    "approved":  '<span class="badge badge-success">✓ Approved</span>',
    "pending":   '<span class="badge badge-warning">⏳ Pending</span>',
    "rejected":  '<span class="badge badge-danger">✗ Rejected</span>',
    "completed": '<span class="badge badge-neutral">✓ Completed</span>',
    "cancelled": '<span class="badge badge-neutral">— Cancelled</span>',
}

# ── Render table for each tab ────────────────────────────────────────────────
for tab, name in zip(tabs, tab_names):
    with tab:
        items = tab_data[name]

        if not items:
            st.markdown(f"""
            <div style="text-align: center; padding: 3rem 1rem; color: #94A3B8;">
                <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">📭</div>
                <div style="font-weight: 500;">No {name.lower()} reservations</div>
            </div>
            """, unsafe_allow_html=True)
            continue

        # Search / filter within tab
        search = st.text_input(
            "Search",
            placeholder="🔍 Search by lab name, course, or purpose...",
            key=f"search_{name}",
            label_visibility="collapsed",
        )

        if search:
            q = search.lower()
            items = [r for r in items
                     if q in r["lab_name"].lower()
                     or q in r.get("course", "").lower()
                     or q in r.get("purpose", "").lower()]

        st.markdown(f"""
        <div style="font-size: 0.8rem; color: #94A3B8; margin-bottom: 0.75rem;">
            {len(items)} reservation{'s' if len(items) != 1 else ''}
        </div>
        """, unsafe_allow_html=True)

        # Build table
        rows_html = ""
        for r in items:
            badge = STATUS_BADGES.get(r["status"], "")
            rows_html += f"""
            <tr>
                <td>
                    <div style="font-weight:500;color:#0F172A;">{r['lab_name']}</div>
                    <div style="font-size:0.75rem;color:#94A3B8;margin-top:2px;">
                        {r.get('course', '—')}</div>
                </td>
                <td>
                    <div style="color:#0F172A;">{r['date']}</div>
                    <div style="font-size:0.75rem;color:#94A3B8;margin-top:2px;">
                        {r['day']}</div>
                </td>
                <td>
                    <div style="color:#0F172A;">P{r['period']}</div>
                    <div style="font-size:0.75rem;color:#94A3B8;margin-top:2px;">
                        {r['period_time']}</div>
                </td>
                <td>{badge}</td>
                <td style="font-size:0.82rem;color:#64748B;">
                    {r['purpose'][:40]}{'...' if len(r['purpose']) > 40 else ''}
                </td>
                <td style="font-size:0.75rem;color:#94A3B8;">{r['created_at']}</td>
            </tr>
            """

        st.markdown(f"""
        <div class="custom-card-static" style="padding:0;overflow-x:auto;">
            <table class="reservation-table">
                <thead>
                    <tr>
                        <th style="min-width:160px;">Lab Room</th>
                        <th style="min-width:100px;">Date</th>
                        <th style="min-width:80px;">Period</th>
                        <th style="min-width:100px;">Status</th>
                        <th style="min-width:150px;">Purpose</th>
                        <th style="min-width:90px;">Created</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
            </table>
        </div>
        """, unsafe_allow_html=True)

        # ── Action buttons for active / pending reservations ─────────────
        if name in ("Active", "Pending", "All"):
            cancellable = [r for r in items if r["status"] in ("approved", "pending")]
            if cancellable:
                st.markdown('<div style="height:1rem;"></div>', unsafe_allow_html=True)
                st.markdown(
                    '<div style="font-size:0.85rem;font-weight:600;color:#0F172A;'
                    'margin-bottom:0.5rem;">Actions</div>',
                    unsafe_allow_html=True,
                )

                for r in cancellable:
                    ac1, ac2, ac3 = st.columns([3, 1, 1])
                    with ac1:
                        st.markdown(
                            f'<div style="font-size:0.85rem;padding-top:6px;">'
                            f'{r["lab_name"]} — {r["date"]} P{r["period"]}</div>',
                            unsafe_allow_html=True,
                        )
                    with ac2:
                        if st.button("👁 View", key=f"view_{name}_{r['id']}",
                                     use_container_width=True, type="secondary"):
                            # Navigate to lab detail
                            from data.mock_data import LABS
                            lab_match = next(
                                (l for l in LABS if l["id"] == r["lab_id"]), None
                            )
                            if lab_match:
                                st.session_state.selected_lab = lab_match
                                st.switch_page("pages/lab_room_detail.py")
                    with ac3:
                        if st.button("✗ Cancel", key=f"cancel_{name}_{r['id']}",
                                     use_container_width=True, type="secondary"):
                            st.warning(
                                f"⚠️ Reservation #{r['id']} for **{r['lab_name']}** "
                                f"on {r['date']} would be cancelled. "
                                f"*(Demo mode — no actual changes)*"
                            )

# ── Bottom action ────────────────────────────────────────────────────────────
st.markdown('<div class="custom-divider"></div>', unsafe_allow_html=True)
if st.button("📝 New Reservation", type="primary", use_container_width=False):
    st.switch_page("pages/preorder.py")
