import streamlit as st

def render_admin():
    st.markdown("""
    <div class="main-header">
        <h1>Laboratory System Administration</h1>
        <p>Manage facility inventory, room availability statuses, and system policies.</p>
    </div>
    """, unsafe_allow_html=True)

    tab_inv, tab_add, tab_cfg = st.tabs(["Inventory Management", "Register New Suite", "Policy Controls"])

    with tab_inv:
        st.subheader("Current Laboratory Suites")
        labs = st.session_state.labs
        
        for idx, lab in enumerate(labs):
            with st.container():
                c1, c2, c3 = st.columns([2.5, 1.5, 1.2])
                with c1:
                    st.markdown(f"**{lab['name']}** (`{lab['id']}`) - {lab['building']}")
                    st.caption(f"Cap: {lab['capacity']} | BSL: {lab['bsl_level']} | Free Academic Access")
                
                with c2:
                    current_status = lab["status"]
                    new_status = st.selectbox(
                        "Status", 
                        ["Available", "Occupied", "Maintenance"], 
                        index=["Available", "Occupied", "Maintenance"].index(current_status),
                        key=f"adm_stat_{lab['id']}"
                    )
                    if new_status != current_status:
                        lab["status"] = new_status
                        st.toast(f"Updated {lab['id']} status to {new_status}", icon="🔄")
                        st.rerun()

                with c3:
                    st.markdown("<br/>", unsafe_allow_html=True)
                    if st.button("Decommission", key=f"del_{lab['id']}"):
                        st.session_state.labs = [l for l in st.session_state.labs if l["id"] != lab["id"]]
                        st.toast(f"Decommissioned facility {lab['id']}", icon="🗑️")
                        st.rerun()
                st.markdown("---")

    with tab_add:
        with st.form("add_lab_form"):
            st.subheader("Register New Laboratory Suite")
            a_col1, a_col2 = st.columns(2)
            with a_col1:
                new_id = st.text_input("Lab ID (e.g. LAB-G101)", value=f"LAB-G{len(st.session_state.labs)+101}")
                new_name = st.text_input("Facility Name", placeholder="e.g. Nanotechnology Cleanroom Suite")
                new_bldg = st.selectbox("Building Wing", ["BioTech Wing A", "Quantum Physics Lab B", "Chemistry Complex C", "Micro-Nano Fabrication D", "AI & Autonomous Systems F"])
                new_floor = st.text_input("Floor Level", value="Floor 1")
            with a_col2:
                new_cap = st.number_input("Max Capacity (Persons)", min_value=1, max_value=50, value=8)
                new_bsl = st.selectbox("Biosafety Level", ["BSL-1", "BSL-2", "BSL-3"])
                new_status = st.selectbox("Initial Status", ["Available", "Maintenance", "Occupied"])

            new_desc = st.text_area("Lab Description & Capabilities", placeholder="Enter room capabilities...")
            new_equip = st.text_input("Equipment Specs (Comma separated)", value="Biosafety Cabinet Class II, High-Speed Centrifuge, Autoclave")

            if st.form_submit_button("Add Suite to Inventory", type="primary"):
                if not new_name.strip():
                    st.error("Please enter a facility name.")
                else:
                    equip_list = [e.strip() for e in new_equip.split(",") if e.strip()]
                    new_lab_obj = {
                        "id": new_id.strip(),
                        "name": new_name.strip(),
                        "building": new_bldg,
                        "floor": new_floor,
                        "capacity": int(new_cap),
                        "bsl_level": new_bsl,
                        "rate": 0.00,
                        "status": new_status,
                        "description": new_desc.strip() if new_desc.strip() else "Newly registered laboratory facility.",
                        "equipment": equip_list
                    }
                    st.session_state.labs.append(new_lab_obj)
                    st.toast(f"✅ Registered suite {new_id} in system inventory!", icon="🚀")
                    st.success(f"Facility {new_name} ({new_id}) successfully created!")
                    st.rerun()

    with tab_cfg:
        st.subheader("Policy Controls")
        st.checkbox("Require Admin Approval for BSL-2 and BSL-3 Suites", value=True)
        st.checkbox("Enable Automatic Cancellation for Unconfirmed 48-hour Pending Orders", value=True)
        st.checkbox("Enforce Operator Safety Certification prior to room entry", value=True)
        st.slider("Maximum Advance Booking Window (Days)", min_value=7, max_value=90, value=30)
