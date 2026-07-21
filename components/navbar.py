"""
Top navigation bar component shared across authenticated pages.
"""
import streamlit as st
from data.mock_data import MOCK_USER


def render_navbar():
    """Render the top navigation bar with logo and user info."""
    user = st.session_state.get("user", MOCK_USER)
    name = user.get("name", "User")
    initials = "".join([w[0] for w in name.split()[:2]]).upper()

    st.markdown(f"""
    <div style="
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.6rem 0;
        margin-bottom: 1.25rem;
        border-bottom: 1px solid #E2E8F0;
    ">
        <div style="display: flex; align-items: center; gap: 0.6rem;">
            <div style="
                width: 38px; height: 38px;
                background: linear-gradient(135deg, #DBEAFE 0%, #C7D2FE 100%);
                border-radius: 10px;
                display: flex; align-items: center; justify-content: center;
                font-size: 1.1rem;
            ">🧪</div>
            <span style="font-weight: 700; font-size: 1.15rem; color: #0F172A;
                         letter-spacing: -0.01em;">LabRoom</span>
        </div>
        <div style="display: flex; align-items: center; gap: 0.85rem;">
            <div style="text-align: right;">
                <div style="font-size: 0.85rem; font-weight: 600; color: #0F172A;
                            line-height: 1.3;">{name}</div>
                <div style="font-size: 0.72rem; color: #94A3B8;
                            line-height: 1.2;">{user.get('role', 'Student').capitalize()}</div>
            </div>
            <div style="
                width: 36px; height: 36px;
                background: linear-gradient(135deg, #2563EB 0%, #6366F1 100%);
                border-radius: 50%;
                display: flex; align-items: center; justify-content: center;
                color: white; font-weight: 600; font-size: 0.8rem;
                letter-spacing: 0.02em;
                box-shadow: 0 2px 8px rgba(37, 99, 235, 0.3);
            ">{initials}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
