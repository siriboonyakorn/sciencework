import streamlit as st
import time

# Set page configuration
st.set_page_config(
    page_title="Lab Room Pre-Order - Login",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Inject custom CSS to match the SaaS design aesthetic as closely as possible in Streamlit
custom_css = """
<style>
    /* Global background gradient */
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 100%);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }

    /* Hide Streamlit header and footer for a cleaner look */
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* Center the main container and make it look like a card */
    .block-container {
        padding-top: 4rem;
        padding-bottom: 4rem;
        max-width: 480px;
    }

    /* Card styling container */
    div[data-testid="stVerticalBlock"] > div {
        background-color: white;
        padding: 2rem;
        border-radius: 16px;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
        border: 1px solid #E2E8F0;
    }

    /* Override input fields to look modern */
    .stTextInput input {
        border-radius: 8px !important;
        border: 1px solid #E2E8F0 !important;
        padding: 0.75rem 1rem !important;
        color: #0F172A !important;
        transition: all 0.2s ease;
    }
    .stTextInput input:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.2) !important;
    }

    /* Primary Button styling */
    .stButton button {
        background-color: #2563EB !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        width: 100% !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
    }
    .stButton button:hover {
        background-color: #1D4ED8 !important;
        transform: scale(1.02);
    }
    .stButton button:active {
        transform: scale(1.0);
    }

    /* Checkbox styling */
    .stCheckbox label {
        color: #64748B !important;
    }

    /* Text styling */
    h1 {
        color: #0F172A !important;
        font-size: 1.875rem !important;
        font-weight: 700 !important;
        margin-bottom: 0.5rem !important;
    }
    .subtitle {
        color: #64748B;
        font-size: 0.875rem;
        margin-bottom: 2rem;
    }
    .logo-text {
        color: #2563EB;
        font-weight: 600;
        font-size: 1.125rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
        margin-bottom: 2rem;
    }
    
    /* Links */
    a {
        color: #2563EB !important;
        text-decoration: none !important;
        font-size: 0.875rem;
        font-weight: 500;
    }
    a:hover {
        text-decoration: underline !important;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# UI Layout
st.markdown('<div class="logo-text">🧪 LabRoom</div>', unsafe_allow_html=True)
st.markdown('<h1>Welcome back</h1>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter your details to access the pre-order system.</div>', unsafe_allow_html=True)

# Form
with st.form("login_form", clear_on_submit=False):
    student_id = st.text_input("Student ID", placeholder="e.g. 64010000")
    password = st.text_input("Password", type="password", placeholder="••••••••")
    
    # Streamlit layout for Remember Me and Forgot Password
    col1, col2 = st.columns([1, 1])
    with col1:
        remember_me = st.checkbox("Remember me")
    with col2:
        # Using markdown for right-aligned forgot password link
        st.markdown('<div style="text-align: right; padding-top: 0.5rem;"><a href="#">Forgot password?</a></div>', unsafe_allow_html=True)

    st.write("") # spacing
    submitted = st.form_submit_button("Sign in", use_container_width=True)

# Handle Login Logic
if submitted:
    if not student_id.strip():
        st.error("Please enter your Student ID.")
    elif not password:
        st.error("Please enter your password.")
    else:
        # Show a loading spinner
        with st.spinner('Signing in...'):
            time.sleep(1.5) # Simulate API call
            
            # Mock authentication
            if student_id == "admin" and password == "admin":
                st.success("Login successful! Redirecting...")
                # Here you would typically set session state and rerun
                # st.session_state['logged_in'] = True
                # st.rerun()
            else:
                st.error("Invalid Student ID or password. Please try again.")

st.markdown('<div style="text-align: center; margin-top: 2rem; font-size: 0.875rem; color: #64748B;">Don\'t have an account? <a href="#">Request access</a></div>', unsafe_allow_html=True)
