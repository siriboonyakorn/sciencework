import streamlit as st
from src.config import setup_page
from src.state import initialize_state
from src.views.dashboard import render_dashboard
from src.views.browse import render_browse
from src.views.schedule import render_schedule
from src.views.orders import render_orders
from src.views.admin import render_admin

# 1. Page Setup & Custom CSS
setup_page()

# 2. State Initialization
initialize_state()

# 3. Clean Ultra-Minimal Sidebar Navigation
with st.sidebar:
    st.markdown("""
    <div style="padding: 0.5rem 0 1.2rem 0; border-bottom: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
        <div style="display: flex; align-items: center; gap: 0.6rem;">
            <div style="background-color: #004ac6; color: white; width: 34px; height: 34px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; font-family: 'Geist', sans-serif; font-size: 1rem;">
                R
            </div>
            <div>
                <div style="font-family: 'Geist', sans-serif; font-size: 1.15rem; font-weight: 700; color: #0f172a; line-height: 1.1;">
                    LabReserve
                </div>
                <div style="font-size: 0.72rem; color: #64748b; font-weight: 500;">
                    Precision Lab Systems
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation Menu",
        [
            "Dashboard",
            "Browse & Pre-Order",
            "Schedule Matrix",
            "My Reservations",
            "Admin Settings"
        ],
        index=1,
        label_visibility="collapsed"
    )

    st.markdown("<br/><br/>", unsafe_allow_html=True)
    st.markdown("---")

    total_labs = len(st.session_state.labs)
    avail_labs = len([l for l in st.session_state.labs if l["status"] == "Available"])

    st.markdown(f"""
    <div style="background-color: #f8fafc; padding: 0.9rem; border-radius: 10px; border: 1px solid #e2e8f0;">
        <div style="font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase; letter-spacing: 0.05em;">
            FACILITY AVAILABILITY
        </div>
        <div style="font-family: 'Geist', sans-serif; font-size: 1.3rem; font-weight: 800; color: #15803d; margin-top: 0.2rem;">
            {avail_labs} of {total_labs} Free Suites
        </div>
        <div style="font-size: 0.75rem; color: #004ac6; font-weight: 600; margin-top: 0.3rem;">
            ✓ 100% Complimentary Access
        </div>
    </div>
    """, unsafe_allow_html=True)

# 4. View Router
if page == "Dashboard":
    render_dashboard()
elif page == "Browse & Pre-Order":
    render_browse()
elif page == "Schedule Matrix":
    render_schedule()
elif page == "My Reservations":
    render_orders()
elif page == "Admin Settings":
    render_admin()
