"""
Login page — fixed styling, proper session state management.
"""
import streamlit as st
import time
from components.styles import inject_login_styles


def _do_login(student_id: str, password: str):
    """Handle the login logic."""
    if not student_id.strip():
        st.error("⚠️ Please enter your Student ID.")
        return False
    if not password:
        st.error("⚠️ Please enter your password.")
        return False

    with st.spinner("Signing in..."):
        time.sleep(1.2)  # Simulate API call

    # Mock authentication
    if student_id == "admin" and password == "admin":
        st.session_state.logged_in = True
        st.session_state.user = {
            "id": student_id,
            "name": "John Doe",
            "email": "john.doe@university.edu",
            "role": "student",
            "department": "Computer Science",
        }
        st.rerun()
    else:
        st.error("❌ Invalid Student ID or password. Please try again.")
        return False


# ── Inject login-specific CSS ────────────────────────────────────────────────
inject_login_styles()

# ── Layout: center the login card ────────────────────────────────────────────
st.markdown('<div style="height: 6vh;"></div>', unsafe_allow_html=True)
_spacer_l, _center, _spacer_r = st.columns([1.2, 1.6, 1.2])

with _center:
    # ── Logo ─────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="
        display: flex; align-items: center; gap: 0.6rem;
        margin-bottom: 2rem; margin-top: 2rem;
    ">
        <div style="
            width: 44px; height: 44px;
            background: linear-gradient(135deg, #DBEAFE 0%, #C7D2FE 100%);
            border-radius: 12px;
            display: flex; align-items: center; justify-content: center;
            font-size: 1.3rem;
        ">🧪</div>
        <span style="
            font-weight: 700; font-size: 1.25rem; color: #0F172A;
            letter-spacing: -0.01em;
        ">LabRoom</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Title & Subtitle ────────────────────────────────────────────────────
    st.markdown("""
    <div style="margin-bottom: 1.75rem;">
        <h1 style="
            font-size: 1.85rem; font-weight: 700; color: #0F172A;
            margin: 0 0 0.4rem 0; line-height: 1.2; letter-spacing: -0.02em;
        ">Welcome back</h1>
        <p style="
            font-size: 0.9rem; color: #64748B; margin: 0;
            line-height: 1.5;
        ">Enter your details to access the lab pre-order system.</p>
    </div>
    """, unsafe_allow_html=True)

    # ── Login Form ──────────────────────────────────────────────────────────
    with st.form("login_form", clear_on_submit=False):
        student_id = st.text_input(
            "Student ID",
            placeholder="e.g. 64010000",
            help="Enter your university student ID",
        )
        password = st.text_input(
            "Password",
            type="password",
            placeholder="••••••••",
        )

        # Remember me + Forgot password row
        col_rem, col_forgot = st.columns([1, 1])
        with col_rem:
            remember_me = st.checkbox("Remember me")
        with col_forgot:
            st.markdown(
                '<div style="text-align: right; padding-top: 0.45rem;">'
                '<a href="#" style="color: #2563EB; font-size: 0.85rem; '
                'font-weight: 500; text-decoration: none;">'
                'Forgot password?</a></div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div style="height: 0.25rem;"></div>', unsafe_allow_html=True)
        submitted = st.form_submit_button("Sign in", use_container_width=True)

    if submitted:
        _do_login(student_id, password)

    # ── Footer ──────────────────────────────────────────────────────────────
    st.markdown("""
    <div style="
        text-align: center; margin-top: 1.75rem;
        font-size: 0.85rem; color: #64748B;
    ">
        Don't have an account?
        <a href="#" style="color: #2563EB; font-weight: 600;
                          text-decoration: none;">Request access</a>
    </div>
    """, unsafe_allow_html=True)

    # ── Mock credentials hint ────────────────────────────────────────────────
    st.markdown("""
    <div style="
        text-align: center; margin-top: 2.5rem; padding: 0.75rem 1rem;
        background: #F0F9FF; border-radius: 10px; border: 1px solid #BAE6FD;
    ">
        <span style="font-size: 0.78rem; color: #0369A1;">
            💡 Demo credentials: <b>admin</b> / <b>admin</b>
        </span>
    </div>
    """, unsafe_allow_html=True)
