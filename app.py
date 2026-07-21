"""
LabRoom — Lab Room Pre-Order Application
Main entry point. Handles page config, session state, and navigation.
"""
# pyrefly: ignore [missing-import]
import streamlit as st
from components.styles import inject_global_styles

# ── Page Configuration (must be first Streamlit command) ─────────────────────
st.set_page_config(
    page_title="LabRoom — Lab Room Pre-Order",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="auto",
)

# ── Initialize Session State ─────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user" not in st.session_state:
    st.session_state.user = None
if "selected_lab" not in st.session_state:
    st.session_state.selected_lab = None
if "week_offset" not in st.session_state:
    st.session_state.week_offset = 0


# ── Logout handler ───────────────────────────────────────────────────────────
def _logout():
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.selected_lab = None
    st.session_state.week_offset = 0
    st.rerun()


# ── Define Pages ─────────────────────────────────────────────────────────────
login_page = st.Page("pages/login.py", title="Login", icon="🔑")
dashboard_page = st.Page("pages/dashboard.py", title="Dashboard", icon="🏠")
lab_rooms_page = st.Page("pages/lab_rooms.py", title="Lab Rooms", icon="🔬")
lab_detail_page = st.Page("pages/lab_room_detail.py", title="Room Detail", icon="📋")
preorder_page = st.Page("pages/preorder.py", title="New Reservation", icon="📝")
reservations_page = st.Page("pages/my_reservations.py", title="My Reservations", icon="📅")
logout_page = st.Page(_logout, title="Log out", icon="🚪")

# ── Navigation ───────────────────────────────────────────────────────────────
if not st.session_state.logged_in:
    # Not authenticated — only show login
    pg = st.navigation([login_page], position="hidden")
else:
    # Authenticated — show full navigation
    pg = st.navigation(
        {
            "Main": [dashboard_page, lab_rooms_page, lab_detail_page],
            "Reservations": [preorder_page, reservations_page],
            "Account": [logout_page],
        }
    )

# ── Apply Global Styles ─────────────────────────────────────────────────────
inject_global_styles()

# ── Run Selected Page ────────────────────────────────────────────────────────
pg.run()
