"""
Lab Room List — search, filter, and browse available lab rooms.
"""
import streamlit as st
from components.navbar import render_navbar
from data.mock_data import LABS

# ── Navbar ───────────────────────────────────────────────────────────────────
render_navbar()

# ── Page Header ──────────────────────────────────────────────────────────────
st.markdown("""
<div class="animate-in" style="margin-bottom: 1.5rem;">
    <h1 style="
        font-size: 1.5rem; font-weight: 700; color: #0F172A;
        margin: 0 0 0.35rem 0; letter-spacing: -0.02em;
    ">🔬 Lab Rooms</h1>
    <p style="font-size: 0.875rem; color: #64748B; margin: 0;">
        Browse and reserve laboratory rooms across campus.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Search & Filters ────────────────────────────────────────────────────────
filter_col1, filter_col2, filter_col3 = st.columns([2, 1, 1])

with filter_col1:
    search = st.text_input(
        "Search",
        placeholder="🔍 Search labs by name...",
        label_visibility="collapsed",
    )
with filter_col2:
    buildings = sorted(set(lab["building"] for lab in LABS))
    building_filter = st.selectbox(
        "Building",
        ["All Buildings"] + buildings,
        label_visibility="collapsed",
    )
with filter_col3:
    sort_option = st.selectbox(
        "Sort",
        ["Name (A–Z)", "Capacity (High)", "Capacity (Low)", "Availability"],
        label_visibility="collapsed",
    )

st.markdown('<div style="height: 0.5rem;"></div>', unsafe_allow_html=True)

# ── Filter logic ─────────────────────────────────────────────────────────────
filtered_labs = LABS.copy()

if search:
    q = search.lower()
    filtered_labs = [l for l in filtered_labs
                     if q in l["name"].lower() or q in l["building"].lower()
                     or q in l["id"].lower()]

if building_filter != "All Buildings":
    filtered_labs = [l for l in filtered_labs if l["building"] == building_filter]

if sort_option == "Name (A–Z)":
    filtered_labs.sort(key=lambda l: l["name"])
elif sort_option == "Capacity (High)":
    filtered_labs.sort(key=lambda l: l["capacity"], reverse=True)
elif sort_option == "Capacity (Low)":
    filtered_labs.sort(key=lambda l: l["capacity"])
elif sort_option == "Availability":
    filtered_labs.sort(key=lambda l: l["available_count"], reverse=True)

# ── Results count ────────────────────────────────────────────────────────────
st.markdown(f"""
<div style="font-size: 0.8rem; color: #94A3B8; margin-bottom: 1rem;">
    Showing {len(filtered_labs)} of {len(LABS)} labs
</div>
""", unsafe_allow_html=True)

# ── Lab Cards Grid ───────────────────────────────────────────────────────────
if not filtered_labs:
    st.markdown("""
    <div style="text-align: center; padding: 3rem 1rem; color: #94A3B8;">
        <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🔍</div>
        <div style="font-weight: 500;">No labs found</div>
        <div style="font-size: 0.85rem; margin-top: 0.25rem;">
            Try adjusting your search or filters.</div>
    </div>
    """, unsafe_allow_html=True)
else:
    # Display in rows of 3
    for row_start in range(0, len(filtered_labs), 3):
        row_labs = filtered_labs[row_start:row_start + 3]
        cols = st.columns(3)

        for i, lab in enumerate(row_labs):
            with cols[i]:
                # Equipment tags
                equip_html = " ".join(
                    [f'<span style="background:#F1F5F9;padding:3px 8px;'
                     f'border-radius:6px;font-size:0.72rem;color:#64748B;'
                     f'white-space:nowrap;">{e}</span>'
                     for e in lab["equipment"][:3]]
                )

                # Availability badge
                if lab["available_count"] > 20:
                    avail_class = "badge-success"
                elif lab["available_count"] > 10:
                    avail_class = "badge-warning"
                else:
                    avail_class = "badge-danger"

                st.markdown(f"""
                <div class="custom-card" style="height: 100%;">
                    <div style="display: flex; justify-content: space-between;
                                align-items: flex-start; margin-bottom: 0.75rem;">
                        <div style="
                            width: 48px; height: 48px;
                            background: linear-gradient(135deg, #DBEAFE 0%, #E0E7FF 100%);
                            border-radius: 12px;
                            display: flex; align-items: center; justify-content: center;
                            font-size: 1.5rem;
                        ">{lab['icon']}</div>
                        <span class="badge {avail_class}">
                            {lab['available_count']} available
                        </span>
                    </div>

                    <div style="font-weight: 600; color: #0F172A; font-size: 1rem;
                                margin-bottom: 0.25rem; line-height: 1.3;">
                        {lab['name']}
                    </div>
                    <div style="font-size: 0.8rem; color: #64748B;
                                margin-bottom: 0.5rem;">
                        📍 {lab['building']} · {lab['floor']}
                    </div>
                    <div style="font-size: 0.8rem; color: #64748B;
                                margin-bottom: 0.85rem;">
                        👥 Capacity: {lab['capacity']} seats
                    </div>

                    <div style="display: flex; flex-wrap: wrap; gap: 4px;
                                margin-bottom: 1rem;">
                        {equip_html}
                    </div>

                    <div style="font-size: 0.8rem; color: #94A3B8;
                                line-height: 1.4; margin-bottom: 0;">
                        {lab['description'][:80]}...
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    f"View Details",
                    key=f"view_{lab['id']}",
                    use_container_width=True,
                    type="primary",
                ):
                    st.session_state.selected_lab = lab
                    st.switch_page("pages/lab_room_detail.py")
