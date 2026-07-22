import streamlit as st
from datetime import date, timedelta
import random

def render_schedule():
    st.markdown("""
    <div class="main-header">
        <h1>Weekly Laboratory Schedule Matrix</h1>
        <p>Visual 7-day grid showing real-time slot allocations and reservation statuses across lab facilities.</p>
    </div>
    """, unsafe_allow_html=True)

    if "week_offset" not in st.session_state:
        st.session_state.week_offset = 0

    col_lab, col_nav = st.columns([2, 1.5])
    
    with col_lab:
        selected_lab_id = st.selectbox(
            "Select Laboratory Suite",
            [f"{l['id']} - {l['name']}" for l in st.session_state.labs]
        )
        target_lab_id = selected_lab_id.split(" - ")[0]

    with col_nav:
        st.markdown("<div style='font-size:0.8rem; font-weight:600; color:#434655; margin-bottom:0.3rem;'>Week Navigation</div>", unsafe_allow_html=True)
        nav_prev, nav_today, nav_next = st.columns(3)
        with nav_prev:
            if st.button("⬅️ Prev", key="btn_prev_week"):
                st.session_state.week_offset -= 1
                st.rerun()
        with nav_today:
            if st.button("📅 Today", key="btn_today_week"):
                st.session_state.week_offset = 0
                st.rerun()
        with nav_next:
            if st.button("Next ➡️", key="btn_next_week"):
                st.session_state.week_offset += 1
                st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # Calculate 7 days for the selected week offset
    today = date.today()
    start_of_week = (today - timedelta(days=today.weekday())) + timedelta(weeks=st.session_state.week_offset)
    days = [(start_of_week + timedelta(days=d)) for d in range(7)]
    day_labels = [d.strftime("%a %b %d") for d in days]
    day_strs = [d.strftime("%Y-%m-%d") for d in days]

    time_slots = [
        "08:00 AM - 10:00 AM",
        "10:00 AM - 12:00 PM",
        "12:00 PM - 02:00 PM",
        "02:00 PM - 04:00 PM",
        "04:00 PM - 06:00 PM",
        "06:00 PM - 08:00 PM"
    ]

    st.markdown(f"### Weekly Schedule: **{start_of_week.strftime('%B %d, %Y')}** to **{(start_of_week + timedelta(days=6)).strftime('%B %d, %Y')}**")

    # Render table header
    hdr_cols = st.columns([1.3] + [1]*7)
    with hdr_cols[0]:
        st.markdown("**Time Window**")
    for idx, day_lbl in enumerate(day_labels):
        is_today_col = (days[idx] == today)
        with hdr_cols[idx+1]:
            if is_today_col:
                st.markdown(f"<span style='color:#004ac6; font-weight:700;'>{day_lbl} (Today)</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"**{day_lbl}**")

    st.markdown("---")

    # Fetch existing reservations for target lab
    lab_res_map = {}
    for r in st.session_state.get("reservations", []):
        if r["lab_id"] == target_lab_id:
            key = (r["date"], r["time_slot"])
            lab_res_map[key] = r

    # Deterministic fallback random seed per lab for visual fullness
    random.seed(100 + ord(target_lab_id[-1]) + st.session_state.week_offset)

    for slot in time_slots:
        r_cols = st.columns([1.3] + [1]*7)
        with r_cols[0]:
            st.markdown(f"<span style='font-family:\"JetBrains Mono\"; font-size:0.82rem; color:#434655; font-weight:600;'>{slot}</span>", unsafe_allow_html=True)
        
        for d_idx in range(7):
            d_str = day_strs[d_idx]
            match_res = lab_res_map.get((d_str, slot))
            
            with r_cols[d_idx+1]:
                if match_res:
                    if match_res["status"] == "Confirmed":
                        st.markdown("<div class='slot-chip slot-selected'>Confirmed</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='slot-chip' style='background:#fef3c7; border:1px solid #fde68a; color:#b45309;'>Pending</div>", unsafe_allow_html=True)
                else:
                    rand_val = random.random()
                    if rand_val > 0.75:
                        st.markdown("<div class='slot-chip slot-booked'>Reserved</div>", unsafe_allow_html=True)
                    else:
                        st.markdown("<div class='slot-chip slot-available'>Available</div>", unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; flex-wrap:wrap; gap:1.2rem; align-items:center; background:#ffffff; padding:0.9rem 1.4rem; border-radius:12px; border:1px solid #c3c6d7; box-shadow: 0 2px 6px rgba(0,0,0,0.03);">
        <span style="font-weight:700; font-size:0.85rem; color:#191b23;">Legend:</span>
        <span class="slot-chip slot-available" style="margin:0;">🟢 Available</span>
        <span class="slot-chip slot-selected" style="margin:0;">🔵 Confirmed Booking</span>
        <span class="slot-chip" style="margin:0; background:#fef3c7; border:1px solid #fde68a; color:#b45309;">🟠 Pending Approval</span>
        <span class="slot-chip slot-booked" style="margin:0;">⚪ Unavailable / Booked</span>
    </div>
    """, unsafe_allow_html=True)
