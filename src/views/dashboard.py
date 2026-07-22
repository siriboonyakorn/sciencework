import streamlit as st
import pandas as pd
import plotly.express as px

def render_dashboard():
    st.markdown("""
    <div class="main-header">
        <h1>Precision Lab Systems Dashboard</h1>
        <p>Real-time laboratory room utilization, schedule tracking, and reservation analytics.</p>
    </div>
    """, unsafe_allow_html=True)

    labs = st.session_state.labs
    reservations = st.session_state.reservations

    total_labs = len(labs)
    avail_labs = len([l for l in labs if l["status"] == "Available"])
    active_res = len([r for r in reservations if r["status"] in ["Confirmed", "Pending Approval"]])

    # Top KPI Metrics Row
    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">TOTAL LAB SUITES</div>
            <div class="metric-value">{total_labs}</div>
            <div class="metric-sub">Across 6 Facility Wings</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">FREE & AVAILABLE NOW</div>
            <div class="metric-value" style="color: #16a34a;">{avail_labs}</div>
            <div class="metric-sub">Ready for Pre-Order</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-box">
            <div class="metric-label">ACTIVE BOOKINGS</div>
            <div class="metric-value" style="color: #2563eb;">{active_res}</div>
            <div class="metric-sub">Confirmed & Pending</div>
        </div>
        """, unsafe_allow_html=True)

    with m4:
        st.markdown("""
        <div class="metric-box">
            <div class="metric-label">RESEARCH ACCESS COST</div>
            <div class="metric-value" style="color: #16a34a;">$0.00</div>
            <div class="metric-sub">100% Free Academic Grant</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # Visual Charts
    col_chart1, col_chart2 = st.columns([1.2, 1])

    with col_chart1:
        st.subheader("📈 Hourly Lab Occupancy & Peak Usage")
        hours = ["08:00 AM", "10:00 AM", "12:00 PM", "02:00 PM", "04:00 PM", "06:00 PM", "08:00 PM"]
        util_data = pd.DataFrame({
            "Hour": hours,
            "BioTech Wing A": [40, 85, 90, 95, 70, 45, 20],
            "Quantum Physics B": [30, 60, 80, 85, 90, 65, 30],
            "Chemistry C": [50, 90, 95, 100, 80, 50, 25],
            "Micro-Nano D": [20, 70, 75, 80, 75, 40, 10]
        })
        fig = px.line(
            util_data, 
            x="Hour", 
            y=["BioTech Wing A", "Quantum Physics B", "Chemistry C", "Micro-Nano D"],
            markers=True,
            color_discrete_sequence=["#004ac6", "#4648d4", "#2563eb", "#656d84"]
        )
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="white",
            margin=dict(l=20, r=20, t=30, b=20),
            legend_title_text="Facility Wing",
            height=330
        )
        st.plotly_chart(fig, use_container_width=True)

    with col_chart2:
        st.subheader("📊 Lab Operational Status Breakdown")
        status_counts = pd.DataFrame(labs)["status"].value_counts().reset_index()
        status_counts.columns = ["Status", "Count"]
        
        fig_pie = px.pie(
            status_counts, 
            names="Status", 
            values="Count",
            color="Status",
            color_discrete_map={
                "Available": "#22c55e",
                "Occupied": "#ef4444",
                "Maintenance": "#94a3b8"
            },
            hole=0.55
        )
        fig_pie.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=30, b=20),
            height=330
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # Recent Pre-Orders Table
    st.subheader("📋 Recent Lab Pre-Orders & System Log")
    df_res = pd.DataFrame(reservations)
    if not df_res.empty:
        st.dataframe(
            df_res[["res_id", "lab_id", "lab_name", "researcher", "department", "date", "time_slot", "status"]],
            use_container_width=True,
            column_config={
                "res_id": "Order Ref",
                "lab_id": "Lab ID",
                "lab_name": "Facility Suite",
                "researcher": "Lead Researcher",
                "department": "Department",
                "date": "Date",
                "time_slot": "Scheduled Window",
                "status": "Status"
            }
        )
