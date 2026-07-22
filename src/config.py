import streamlit as st

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --primary: #004ac6;
    --primary-hover: #003ea8;
    --primary-container: #2563eb;
    --on-primary: #ffffff;
    --secondary: #4648d4;
    --background: #faf8ff;
    --surface: #ffffff;
    --surface-container-low: #f3f3fe;
    --surface-container: #ededf9;
    --surface-container-high: #e7e7f3;
    --on-surface: #191b23;
    --on-surface-variant: #434655;
    --outline: #737686;
    --outline-variant: #c3c6d7;
    --radius-sm: 6px;
    --radius-md: 10px;
    --radius-lg: 16px;
    --shadow-sm: 0 2px 8px rgba(0, 74, 198, 0.04);
    --shadow-md: 0 8px 24px rgba(0, 74, 198, 0.08);
}

/* Base Body Styling */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    color: var(--on-surface);
    background-color: var(--background);
}

h1, h2, h3, h4, h5, h6, .geist-font {
    font-family: 'Geist', sans-serif;
    letter-spacing: -0.02em;
    font-weight: 700;
}

/* Clean Custom Scrollbar */
::-webkit-scrollbar {
    width: 6px;
    height: 6px;
}
::-webkit-scrollbar-track {
    background: var(--background);
}
::-webkit-scrollbar-thumb {
    background: var(--outline-variant);
    border-radius: 9999px;
}

/* Premium Main Header Banner */
.main-header {
    background: linear-gradient(135deg, #003ea8 0%, #0053db 45%, #2563eb 100%);
    padding: 2.2rem 2.5rem;
    border-radius: var(--radius-lg);
    color: white;
    box-shadow: 0 12px 28px -6px rgba(0, 74, 198, 0.28);
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
}

.main-header h1 {
    color: #ffffff;
    font-weight: 800;
    margin: 0;
    font-size: 2.2rem;
    line-height: 1.2;
}

.main-header p {
    color: #dbe1ff;
    margin: 0.4rem 0 0 0;
    font-size: 1rem;
    font-weight: 400;
}

/* Metric KPI Cards */
.metric-box {
    background: var(--surface);
    border: 1px solid var(--outline-variant);
    border-radius: var(--radius-lg);
    padding: 1.3rem 1.4rem;
    text-align: left;
    box-shadow: var(--shadow-sm);
    transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
    height: 100%;
}

.metric-box:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
    border-color: var(--primary-container);
}

.metric-label {
    font-family: 'Geist', sans-serif;
    font-size: 0.78rem;
    color: var(--on-surface-variant);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 700;
}

.metric-value {
    font-family: 'Geist', sans-serif;
    font-size: 2.1rem;
    font-weight: 800;
    color: var(--primary);
    margin-top: 0.2rem;
    line-height: 1.1;
}

.metric-sub {
    font-size: 0.82rem;
    color: #16a34a;
    font-weight: 600;
    margin-top: 0.4rem;
}

/* Lab Room Card Container */
.lab-card {
    background-color: var(--surface);
    border: 1px solid var(--outline-variant);
    border-radius: var(--radius-lg);
    padding: 1.5rem;
    box-shadow: var(--shadow-sm);
    transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
    margin-bottom: 1.2rem;
}

.lab-card:hover {
    box-shadow: var(--shadow-md);
    border-color: var(--primary-container);
    transform: translateY(-3px);
}

.lab-title {
    font-family: 'Geist', sans-serif;
    font-size: 1.3rem;
    font-weight: 700;
    color: var(--on-surface);
    margin-bottom: 0.35rem;
}

.lab-id {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    background-color: var(--surface-container-low);
    color: var(--primary);
    padding: 0.25rem 0.65rem;
    border-radius: var(--radius-sm);
    font-weight: 700;
    border: 1px solid #dbe1ff;
}

/* Status Badges */
.status-pill {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.3rem 0.85rem;
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 700;
    font-family: 'Geist', sans-serif;
    letter-spacing: 0.01em;
}

.status-available {
    background-color: #dcfce7;
    color: #15803d;
    border: 1px solid #bbf7d0;
}

.status-occupied {
    background-color: #fee2e2;
    color: #b91c1c;
    border: 1px solid #fecaca;
}

.status-pending {
    background-color: #fef3c7;
    color: #b45309;
    border: 1px solid #fde68a;
}

.status-maintenance {
    background-color: #f1f5f9;
    color: #475569;
    border: 1px solid #cbd5e1;
}

/* Equipment Badge */
.equipment-tag {
    display: inline-block;
    background-color: var(--surface-container-low);
    color: var(--on-surface-variant);
    font-size: 0.78rem;
    padding: 0.25rem 0.6rem;
    border-radius: var(--radius-sm);
    margin-right: 0.35rem;
    margin-bottom: 0.35rem;
    font-weight: 500;
    border: 1px solid var(--outline-variant);
}

/* Free Badge */
.free-badge {
    display: inline-block;
    background-color: #dcfce7;
    color: #15803d;
    font-size: 0.85rem;
    font-weight: 800;
    padding: 0.25rem 0.75rem;
    border-radius: var(--radius-sm);
    border: 1px solid #bbf7d0;
    font-family: 'Geist', sans-serif;
}

/* ULTRACLEAN SIDEBAR STYLING */
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1px solid #e2e8f0 !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h2, 
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] h3 {
    font-family: 'Geist', sans-serif;
}

/* Clean Radio Navigation */
[data-testid="stSidebar"] div[role="radiogroup"] {
    gap: 0.3rem;
}

[data-testid="stSidebar"] div[role="radiogroup"] label {
    background-color: transparent;
    padding: 0.65rem 0.9rem !important;
    border-radius: var(--radius-md) !important;
    border: 1px solid transparent !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    color: #334155 !important;
    transition: all 0.15s ease-in-out !important;
    margin-bottom: 0.15rem;
}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
    background-color: #f1f5f9 !important;
    color: #0f172a !important;
}

[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
    background-color: #eff6ff !important;
    color: #004ac6 !important;
    border-color: #bfdbfe !important;
    font-weight: 700 !important;
}

/* Hide radio circle radio indicators for ultra-clean list feel */
[data-testid="stSidebar"] div[role="radiogroup"] label div[first-child] {
    display: none !important;
}

div.stButton > button {
    border-radius: var(--radius-md);
    font-family: 'Geist', sans-serif;
    font-weight: 600;
    transition: all 0.18s ease-in-out;
}

div.stButton > button[kind="primary"] {
    background-color: var(--primary);
    color: white;
    border: none;
    box-shadow: 0 4px 14px rgba(0, 74, 198, 0.22);
}

div.stButton > button[kind="primary"]:hover {
    background-color: var(--primary-hover);
    box-shadow: 0 6px 18px rgba(0, 74, 198, 0.32);
    transform: scale(1.015);
}
</style>
"""

def setup_page():
    st.set_page_config(
        page_title="Precision Lab Systems | LabReserve",
        page_icon="🔬",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
