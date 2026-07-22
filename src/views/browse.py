import streamlit as st
from datetime import date, timedelta

def render_browse():
    st.markdown("""
    <div class="main-header">
        <h1>Pre-Order Laboratory Rooms</h1>
        <p>Explore specialized research spaces, verify biosafety levels, and instantly lock in time slots.</p>
    </div>
    """, unsafe_allow_html=True)

    # Filter Bar
    f_col1, f_col2, f_col3, f_col4 = st.columns([1.5, 1, 1, 1])

    with f_col1:
        search_query = st.text_input("🔍 Search Lab Name, Equipment, or ID", placeholder="e.g. Mass Spec, Cleanroom, BSL-2...")

    with f_col2:
        buildings = ["All Buildings"] + sorted(list(set(l["building"] for l in st.session_state.labs)))
        selected_bldg = st.selectbox("🏢 Building Wing", buildings)

    with f_col3:
        status_filter = st.selectbox("🟢 Availability Status", ["All Statuses", "Available Only", "Occupied", "Maintenance"])

    with f_col4:
        bsl_filter = st.selectbox("🛡️ Biosafety Level", ["All BSL Levels", "BSL-1", "BSL-2", "BSL-3"])

    st.markdown("<br/>", unsafe_allow_html=True)

    # Filter Logic
    filtered_labs = st.session_state.labs
    if search_query:
        q = search_query.lower().strip()
        filtered_labs = [
            l for l in filtered_labs 
            if q in l["name"].lower() or q in l["id"].lower() or any(q in eq.lower() for eq in l["equipment"]) or q in l["description"].lower()
        ]
    if selected_bldg != "All Buildings":
        filtered_labs = [l for l in filtered_labs if l["building"] == selected_bldg]
    if status_filter == "Available Only":
        filtered_labs = [l for l in filtered_labs if l["status"] == "Available"]
    elif status_filter != "All Statuses":
        filtered_labs = [l for l in filtered_labs if l["status"] == status_filter]
    if bsl_filter != "All BSL Levels":
        filtered_labs = [l for l in filtered_labs if l["bsl_level"] == bsl_filter]

    st.caption(f"Showing **{len(filtered_labs)}** matching laboratory suites")

    if not filtered_labs:
        st.warning("No laboratory suites matched your filter criteria. Try adjusting your search query or filters.")
        return

    # Display Labs Grid (2 Columns)
    for i in range(0, len(filtered_labs), 2):
        cols = st.columns(2)
        for idx, col in enumerate(cols):
            if i + idx < len(filtered_labs):
                lab = filtered_labs[i + idx]
                with col:
                    status_cls = {
                        "Available": "status-available",
                        "Occupied": "status-occupied",
                        "Maintenance": "status-maintenance",
                        "Pending": "status-pending"
                    }.get(lab["status"], "status-available")

                    st.markdown(f"""
                    <div class="lab-card">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <div>
                                <span class="lab-id">{lab['id']}</span>
                                <span style="font-size: 0.8rem; color: #434655; margin-left: 0.5rem; font-weight: 500;">{lab['building']} ({lab['floor']})</span>
                            </div>
                            <span class="status-pill {status_cls}">{lab['status']}</span>
                        </div>
                        <div class="lab-title" style="margin-top: 0.6rem;">{lab['name']}</div>
                        <p style="font-size: 0.85rem; color: #434655; line-height: 1.45; margin-bottom: 0.8rem;">
                            {lab['description']}
                        </p>
                        <div style="margin-bottom: 0.8rem;">
                            {"".join([f'<span class="equipment-tag">{eq}</span>' for eq in lab['equipment']])}
                        </div>
                        <div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #ededf9; padding-top: 0.8rem; margin-top: 0.5rem;">
                            <div>
                                <span style="font-size: 1.15rem; font-weight: 800; color: #004ac6;">${lab['rate']:.2f}</span>
                                <span style="font-size: 0.78rem; color: #737686;"> / hour</span>
                            </div>
                            <div style="font-size: 0.78rem; color: #434655; font-weight: 600;">
                                👥 Cap: {lab['capacity']} | 🛡️ {lab['bsl_level']}
                            </div>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    # Interactive Pre-Order Form
                    with st.expander(f"📅 Pre-Order / Reserve {lab['id']}", expanded=False):
                        if lab["status"] == "Maintenance":
                            st.warning(f"⚠️ **{lab['id']}** is currently under scheduled maintenance. Pre-orders will require manual administrator clearance.")
                        elif lab["status"] == "Occupied":
                            st.info(f"ℹ️ **{lab['id']}** is currently occupied. You can schedule future dates below.")

                        st.markdown(f"**Pre-Ordering {lab['name']}**")
                        
                        form_col1, form_col2 = st.columns(2)
                        with form_col1:
                            res_name = st.text_input("Lead Researcher Name", value="Dr. Alex Mercer", key=f"name_{lab['id']}")
                            res_dept = st.selectbox(
                                "Department", 
                                ["Biomedical Engineering", "Molecular Genetics", "Applied Physics", "Synthetic Chemistry", "Robotics & AI Lab", "Neuroscience Core"], 
                                key=f"dept_{lab['id']}"
                            )
                            res_date = st.date_input(
                                "Reservation Date", 
                                value=date.today() + timedelta(days=1), 
                                min_value=date.today(),
                                max_value=date.today() + timedelta(days=60),
                                key=f"date_{lab['id']}"
                            )
                        
                        with form_col2:
                            res_proj = st.text_input("Grant / Project Code", value="PRJ-GEN-2026", key=f"proj_{lab['id']}")
                            res_slot = st.selectbox(
                                "Time Slot Window",
                                [
                                    "08:00 AM - 10:00 AM (2 hrs)",
                                    "10:00 AM - 12:00 PM (2 hrs)",
                                    "12:00 PM - 02:00 PM (2 hrs)",
                                    "02:00 PM - 04:00 PM (2 hrs)",
                                    "04:00 PM - 06:00 PM (2 hrs)",
                                    "06:00 PM - 08:00 PM (2 hrs)",
                                    "08:00 AM - 05:00 PM (Full Day - 9 hrs)"
                                ],
                                key=f"slot_{lab['id']}"
                            )
                            
                            hours_num = 9.0 if "Full Day" in res_slot else 2.0
                            est_cost = lab['rate'] * hours_num
                            st.markdown(
                                f"<div style='background-color:#eef0ff; padding:0.6rem; border-radius:8px; border:1px solid #b4c5ff; font-size:0.88rem; color:#003ea8; font-weight:700; margin-top:0.5rem;'>Total Estimated Fee: <strong>${est_cost:.2f}</strong></div>", 
                                unsafe_allow_html=True
                            )

                        special_req = st.text_area("Special Equipment / Gas Setup Requests", placeholder="e.g. Liquid nitrogen access required, gas purge...", key=f"req_{lab['id']}")

                        if st.button(f"Confirm Pre-Order ({lab['id']})", type="primary", key=f"btn_{lab['id']}"):
                            if not res_name.strip() or not res_proj.strip():
                                st.error("Please fill in researcher name and project code before submitting.")
                            else:
                                new_id = f"RES-{len(st.session_state.reservations)+8924}"
                                initial_status = "Pending Approval" if (lab["bsl_level"] == "BSL-2" or lab["status"] == "Maintenance") else "Confirmed"
                                
                                new_res = {
                                    "res_id": new_id,
                                    "lab_id": lab["id"],
                                    "lab_name": lab["name"],
                                    "researcher": res_name.strip(),
                                    "department": res_dept,
                                    "project": res_proj.strip(),
                                    "date": res_date.strftime("%Y-%m-%d"),
                                    "time_slot": res_slot,
                                    "status": initial_status,
                                    "cost": est_cost
                                }
                                st.session_state.reservations.insert(0, new_res)
                                st.toast(f"✅ Pre-Order {new_id} created for {lab['name']}!", icon="🎉")
                                st.success(f"Reservation Submitted! Order Ref: **{new_id}** (Status: **{initial_status}**)")
                                st.rerun()
