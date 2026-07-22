import streamlit as st
from src.config import setup_page
from src.state import initialize_state
from src.views.dashboard import render_dashboard
from src.views.browse import render_browse
from src.views.schedule import render_schedule
from src.views.orders import render_orders
from src.views.admin import render_admin

# 1. Page Configuration & Custom CSS Injection
setup_page()

# 2. State Data Initialization
initialize_state()

# 3. Sidebar Navigation & Global Branding
with st.sidebar:
    st.markdown("""
    <div style="text-align: center; padding: 0.8rem 0; border-bottom: 1px solid #c3c6d7; margin-bottom: 1.5rem;">
        <span style="font-size: 2.2rem;">🔬</span>
        <div style="font-family: 'Geist', sans-serif; font-size: 1.25rem; font-weight: 700; color: #004ac6; margin-top: 0.2rem;">
            LabReserve
        </div>
        <div style="font-size: 0.75rem; color: #434655; font-weight: 500;">
            Precision Lab Systems v2.4
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["📊 Dashboard", "🔬 Browse & Pre-Order Labs", "📅 Schedule Matrix", "📋 My Pre-Orders", "⚙️ Admin Settings"],
        index=1
    )

    st.markdown("---")
    st.markdown("<div class='label-sm' style='color:#737686; font-size:0.75rem; font-weight:700; margin-bottom:0.5rem;'>SYSTEM METRICS</div>", unsafe_allow_html=True)
    
    total_labs = len(st.session_state.labs)
    avail_labs = len([l for l in st.session_state.labs if l["status"] == "Available"])
    active_res = len(st.session_state.reservations)

    st.caption(f"🟢 **Available Labs:** {avail_labs} / {total_labs}")
    st.caption(f"📌 **Active Bookings:** {active_res}")
    st.caption(f"⚡ **System Status:** All Systems Operational")

    st.markdown("---")
    st.markdown("""
    <div style='background-color: #eef0ff; padding: 0.8rem; border-radius: 8px; border: 1px solid #b4c5ff;'>
        <span style='font-size: 0.8rem; color: #003ea8; font-weight: 600;'>💡 Researcher Support</span><br/>
        <span style='font-size: 0.75rem; color: #434655;'>Need specialized equipment calibration? Contact Lab Ops at ext. 4402.</span>
    </div>
    """, unsafe_allow_html=True)

# 4. View Router
if page == "📊 Dashboard":
    render_dashboard()
elif page == "🔬 Browse & Pre-Order Labs":
    render_browse()
elif page == "📅 Schedule Matrix":
    render_schedule()
elif page == "📋 My Pre-Orders":
    render_orders()
elif page == "⚙️ Admin Settings":
    render_admin()
