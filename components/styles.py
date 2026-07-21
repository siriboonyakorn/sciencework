"""
Shared CSS styles and color constants for the LabRoom app.
"""
import streamlit as st

# ── Color Palette ────────────────────────────────────────────────────────────
PRIMARY = "#2563EB"
PRIMARY_DARK = "#1D4ED8"
PRIMARY_LIGHT = "#DBEAFE"
SECONDARY = "#6366F1"
SUCCESS = "#22C55E"
SUCCESS_LIGHT = "#DCFCE7"
WARNING = "#F59E0B"
WARNING_LIGHT = "#FEF3C7"
DANGER = "#EF4444"
DANGER_LIGHT = "#FEE2E2"
BG = "#F8FAFC"
CARD = "#FFFFFF"
TEXT = "#0F172A"
TEXT_SECONDARY = "#64748B"
TEXT_MUTED = "#94A3B8"
BORDER = "#E2E8F0"
BORDER_LIGHT = "#F1F5F9"


def inject_global_styles():
    """Inject base CSS used across all pages."""
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
    /* ── CSS Variables ───────────────────────────────────── */
    :root {
        --primary: #2563EB;
        --primary-dark: #1D4ED8;
        --primary-light: #DBEAFE;
        --secondary: #6366F1;
        --success: #22C55E;
        --success-light: #DCFCE7;
        --warning: #F59E0B;
        --warning-light: #FEF3C7;
        --danger: #EF4444;
        --danger-light: #FEE2E2;
        --bg: #F8FAFC;
        --card: #FFFFFF;
        --text: #0F172A;
        --text-secondary: #64748B;
        --text-muted: #94A3B8;
        --border: #E2E8F0;
        --border-light: #F1F5F9;
    }

    /* ── Global Font ────────────────────────────────────── */
    html, body, [class*="css"], .stMarkdown, .stText,
    .stTextInput label, .stSelectbox label, .stTextArea label,
    .stCheckbox label, .stRadio label, .stButton button,
    p, span, div, h1, h2, h3, h4, h5, h6, a, li, td, th, input, select, textarea, button {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
                     Helvetica, Arial, sans-serif !important;
    }

    /* ── Hide Streamlit Chrome ──────────────────────────── */
    #MainMenu {visibility: hidden !important;}
    header[data-testid="stHeader"] {display: none !important;}
    footer {visibility: hidden !important;}
    .stDeployButton {display: none !important;}
    div[data-testid="stDecoration"] {display: none !important;}

    /* ── Background ─────────────────────────────────────── */
    .stApp {
        background: var(--bg);
    }

    /* ── Block Container ────────────────────────────────── */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* ── Custom Scrollbar ───────────────────────────────── */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: #CBD5E1; border-radius: 3px; }
    ::-webkit-scrollbar-thumb:hover { background: #94A3B8; }

    /* ── Card Component ─────────────────────────────────── */
    .custom-card {
        background: var(--card);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid var(--border);
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: all 0.25s ease;
    }
    .custom-card:hover {
        box-shadow: 0 8px 24px rgba(0,0,0,0.08);
        transform: translateY(-2px);
    }
    .custom-card-static {
        background: var(--card);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid var(--border);
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }

    /* ── Stat Card ──────────────────────────────────────── */
    .stat-card {
        background: var(--card);
        border-radius: 14px;
        padding: 1.25rem 1.5rem;
        border: 1px solid var(--border);
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        transition: all 0.2s ease;
    }
    .stat-card:hover {
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
    }
    .stat-icon {
        width: 42px; height: 42px;
        border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.2rem;
        margin-bottom: 0.75rem;
    }
    .stat-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--text);
        line-height: 1.1;
        margin-bottom: 0.25rem;
    }
    .stat-label {
        font-size: 0.8rem;
        font-weight: 500;
        color: var(--text-secondary);
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* ── Badge ──────────────────────────────────────────── */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.2rem 0.65rem;
        border-radius: 99px;
        font-size: 0.72rem;
        font-weight: 600;
        line-height: 1.5;
        white-space: nowrap;
    }
    .badge-success { background: var(--success-light); color: #15803D; }
    .badge-warning { background: var(--warning-light); color: #B45309; }
    .badge-danger  { background: var(--danger-light);  color: #DC2626; }
    .badge-primary { background: var(--primary-light); color: #1D4ED8; }
    .badge-neutral { background: var(--border-light);  color: var(--text-secondary); }

    /* ── Section Title ──────────────────────────────────── */
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: var(--text);
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* ── Custom Divider ─────────────────────────────────── */
    .custom-divider {
        height: 1px;
        background: var(--border);
        margin: 1.5rem 0;
        border: none;
    }

    /* ── Animations ─────────────────────────────────────── */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes shimmer {
        0%   { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.6; }
    }
    .animate-in {
        animation: fadeInUp 0.4s ease forwards;
    }
    .animate-fade {
        animation: fadeIn 0.3s ease forwards;
    }

    /* ── Streamlit Button Override ───────────────────────── */
    .stButton > button,
    .stFormSubmitButton > button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        padding: 0.55rem 1.25rem !important;
        transition: all 0.2s ease !important;
        font-size: 0.875rem !important;
        letter-spacing: 0.01em !important;
    }
    .stFormSubmitButton > button,
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--primary) 0%, var(--primary-dark) 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 2px 8px rgba(37, 99, 235, 0.25) !important;
    }
    .stFormSubmitButton > button:hover,
    .stButton > button[kind="primary"]:hover {
        box-shadow: 0 4px 16px rgba(37, 99, 235, 0.4) !important;
        transform: translateY(-1px);
    }
    .stButton > button[kind="secondary"] {
        background: white !important;
        color: var(--text) !important;
        border: 1.5px solid var(--border) !important;
    }
    .stButton > button[kind="secondary"]:hover {
        background: var(--border-light) !important;
        border-color: #CBD5E1 !important;
    }

    /* ── Streamlit Input Override ────────────────────────── */
    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stTextArea textarea {
        border-radius: 10px !important;
        border: 1.5px solid var(--border) !important;
        padding: 0.6rem 0.85rem !important;
        font-size: 0.9rem !important;
        color: var(--text) !important;
        transition: all 0.2s ease !important;
    }
    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    .stTextArea textarea:focus {
        border-color: var(--primary) !important;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
    }

    /* ── Streamlit Selectbox Override ────────────────────── */
    .stSelectbox > div > div {
        border-radius: 10px !important;
    }

    /* ── Streamlit Checkbox Override ─────────────────────── */
    .stCheckbox label span {
        color: var(--text-secondary) !important;
        font-size: 0.875rem !important;
    }

    /* ── Streamlit Tabs Override ─────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0.25rem;
        background: transparent;
        border-bottom: 2px solid var(--border-light);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 0.6rem 1.25rem;
        font-weight: 500;
        font-size: 0.875rem;
    }
    .stTabs [aria-selected="true"] {
        background: transparent !important;
        border-bottom: 2px solid var(--primary) !important;
        color: var(--primary) !important;
        font-weight: 600 !important;
    }

    /* ── Data Table ──────────────────────────────────────── */
    .reservation-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        font-size: 0.85rem;
    }
    .reservation-table th {
        background: var(--border-light);
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        font-size: 0.72rem;
        letter-spacing: 0.06em;
        padding: 0.75rem 1rem;
        text-align: left;
        border-bottom: 1px solid var(--border);
    }
    .reservation-table th:first-child { border-radius: 10px 0 0 0; }
    .reservation-table th:last-child  { border-radius: 0 10px 0 0; }
    .reservation-table td {
        padding: 0.85rem 1rem;
        border-bottom: 1px solid var(--border-light);
        color: var(--text);
        vertical-align: middle;
    }
    .reservation-table tr:hover td {
        background: #F8FAFC;
    }
    .reservation-table tr:last-child td {
        border-bottom: none;
    }

    /* ── Sidebar Styling ────────────────────────────────── */
    [data-testid="stSidebar"] {
        background: white !important;
        border-right: 1px solid var(--border) !important;
    }
    [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
        padding-top: 1rem;
    }

    /* ── Expander ───────────────────────────────────────── */
    .streamlit-expanderHeader {
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        color: var(--text) !important;
    }

    /* ── Metric override ────────────────────────────────── */
    [data-testid="stMetricValue"] {
        font-weight: 700 !important;
        color: var(--text) !important;
    }
    [data-testid="stMetricLabel"] {
        font-weight: 500 !important;
        color: var(--text-secondary) !important;
    }

    </style>
    """, unsafe_allow_html=True)


def inject_login_styles():
    """Inject CSS specific to the login page."""
    st.markdown("""
    <style>
    /* ── Login Background ───────────────────────────────── */
    .stApp {
        background: linear-gradient(135deg, #F8FAFC 0%, #EFF6FF 50%, #F0F9FF 100%) !important;
    }
    .block-container {
        padding-top: 0 !important;
        display: flex;
        align-items: center;
        min-height: 100vh;
    }

    /* ── Login Form Card ────────────────────────────────── */
    [data-testid="stForm"] {
        background: white !important;
        border-radius: 16px !important;
        padding: 2rem !important;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06) !important;
        border: 1px solid var(--border) !important;
    }

    /* ── Login Button ───────────────────────────────────── */
    .stFormSubmitButton > button {
        height: 44px !important;
        font-size: 0.95rem !important;
        margin-top: 0.5rem !important;
    }

    /* ── Hide sidebar on login ──────────────────────────── */
    [data-testid="stSidebar"] { display: none !important; }
    [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)
