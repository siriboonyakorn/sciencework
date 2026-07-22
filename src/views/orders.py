import streamlit as st
import json

def render_orders():
    st.markdown("""
    <div class="main-header">
        <h1>My Pre-Orders & Reservation Management</h1>
        <p>Track order statuses, download lab access credentials, or cancel scheduled lab sessions.</p>
    </div>
    """, unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["📌 Active & Pending Pre-Orders", "✅ Completed & Past Orders"])

    with tab1:
        active_list = [r for r in st.session_state.reservations if r["status"] in ["Confirmed", "Pending Approval"]]
        
        if not active_list:
            st.info("No active pre-orders found. Head over to **Browse & Pre-Order Labs** to schedule a room.")
        else:
            for res in active_list:
                with st.container():
                    status_cls = "status-available" if res['status'] == "Confirmed" else "status-pending"
                    
                    st.markdown(f"""
                    <div class="lab-card">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span class="lab-id">{res['res_id']}</span>
                                <span style="font-size: 1.15rem; font-weight: 700; margin-left: 0.6rem; color: #191b23;">{res['lab_name']} ({res['lab_id']})</span>
                            </div>
                            <span class="status-pill {status_cls}">{res['status']}</span>
                        </div>
                        <div style="margin-top: 1rem; display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; font-size: 0.88rem; color: #434655;">
                            <div>👤 <strong>Researcher:</strong><br/>{res['researcher']}</div>
                            <div>🏢 <strong>Department:</strong><br/>{res['department']}</div>
                            <div>📅 <strong>Scheduled Date:</strong><br/>{res['date']}</div>
                            <div>⏰ <strong>Time Window:</strong><br/>{res['time_slot']}</div>
                        </div>
                        <div style="margin-top: 1rem; border-top: 1px solid #ededf9; padding-top: 0.8rem; display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-family: 'Geist', sans-serif; font-size: 1.05rem; font-weight: 800; color: #004ac6;">
                                Total Estimated Fee: ${res['cost']:.2f}
                            </span>
                            <span style="font-size: 0.8rem; color: #737686;">Project Code: <code>{res.get('project', 'N/A')}</code></span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                    c_act1, c_act2, c_act3, c_act4 = st.columns([1.2, 1.2, 1.2, 2])
                    
                    with c_act1:
                        pass_data = json.dumps(res, indent=2)
                        st.download_button(
                            label="📄 Download Pass",
                            data=pass_data,
                            file_name=f"{res['res_id']}_LabPass.json",
                            mime="application/json",
                            key=f"dl_{res['res_id']}"
                        )

                    with c_act2:
                        if res["status"] == "Pending Approval":
                            if st.button("✅ Approve Order", key=f"app_{res['res_id']}"):
                                res["status"] = "Confirmed"
                                st.toast(f"Approved reservation {res['res_id']}", icon="✅")
                                st.rerun()

                    with c_act3:
                        if st.button("❌ Cancel Order", key=f"cancel_{res['res_id']}"):
                            st.session_state.reservations = [r for r in st.session_state.reservations if r["res_id"] != res["res_id"]]
                            st.toast(f"Cancelled reservation {res['res_id']}", icon="🗑️")
                            st.rerun()

                    with c_act4:
                        with st.popover("🔑 Digital Access Key"):
                            st.markdown(f"**Lab Keycard Authorization**")
                            st.caption(f"Ref: {res['res_id']} | Facility: {res['lab_id']}")
                            st.markdown(f"""
                            <div class="digital-pass">
                                <div style="font-family:'JetBrains Mono'; font-weight:700; font-size:1.1rem; color:#6063ee;">
                                    ACC-KEY-{res['res_id'][-4:]}
                                </div>
                                <div style="font-size:0.8rem; color:#cbd5e1; margin-top:0.4rem;">
                                    Holder: {res['researcher']}<br/>
                                    Valid: {res['date']} ({res['time_slot']})
                                </div>
                                <div style="margin-top:0.8rem; font-size:0.75rem; color:#94a3b8;">
                                    Scan code at Lab Keypad door reader
                                </div>
                            </div>
                            """, unsafe_allow_html=True)

    with tab2:
        st.markdown("### Past Completed Sessions")
        completed_list = [r for r in st.session_state.reservations if r["status"] == "Completed"]
        if not completed_list:
            st.info("No historical completed sessions recorded yet.")
        else:
            for c_res in completed_list:
                st.write(c_res)
