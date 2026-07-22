import streamlit as st
from datetime import date, timedelta

def initialize_state():
    """Initializes session state data for labs and reservations if not already set."""
    if "labs" not in st.session_state:
        st.session_state.labs = [
            {
                "id": "LAB-A101",
                "name": "Molecular & Cell Biology Core",
                "building": "BioTech Wing A",
                "floor": "Floor 1",
                "capacity": 12,
                "bsl_level": "BSL-2",
                "rate": 0.00,
                "status": "Available",
                "image": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=600&q=80",
                "description": "High-throughput cell culture workstation equipped with sterile hoods and real-time qPCR systems.",
                "equipment": ["Biosafety Cabinet Class II", "Real-Time PCR System", "CO2 Incubators", "Fluorescence Microscope"]
            },
            {
                "id": "LAB-B204",
                "name": "Advanced Spectroscopy & Laser Suite",
                "building": "Quantum Physics Lab B",
                "floor": "Floor 2",
                "capacity": 6,
                "bsl_level": "BSL-1",
                "rate": 0.00,
                "status": "Available",
                "image": "https://images.unsplash.com/photo-1581093588401-fbb62a02f120?auto=format&fit=crop&w=600&q=80",
                "description": "Vibration-isolated optical suite for ultrafast laser experiments and Raman spectroscopy.",
                "equipment": ["Ti:Sapphire Laser", "Raman Spectrometer", "Optical Table (Vibration Isolated)", "Streak Camera"]
            },
            {
                "id": "LAB-C302",
                "name": "Organic Synthesis & Mass Spec",
                "building": "Chemistry Complex C",
                "floor": "Floor 3",
                "capacity": 8,
                "bsl_level": "BSL-2",
                "rate": 0.00,
                "status": "Occupied",
                "image": "https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80",
                "description": "Full chemical synthesis facility with high-vacuum lines and high-resolution LC-MS instrumentation.",
                "equipment": ["LC-MS System", "Fume Hoods (High Velocity)", "Rotary Evaporator", "NMR 400MHz Access"]
            },
            {
                "id": "LAB-D105",
                "name": "Cleanroom ISO Class 5 Suite",
                "building": "Micro-Nano Fabrication D",
                "floor": "Floor 1",
                "capacity": 4,
                "bsl_level": "BSL-1",
                "rate": 0.00,
                "status": "Available",
                "image": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?auto=format&fit=crop&w=600&q=80",
                "description": "Ultra-clean environment designed for semiconductor microfabrication, photolithography, and MEMS.",
                "equipment": ["Cleanroom ISO 5", "Photolithography Mask Aligner", "E-beam Evaporator", "Stylus Profilometer"]
            },
            {
                "id": "LAB-E401",
                "name": "Cryo-EM Analytical Facility",
                "building": "Structural Biology Wing E",
                "floor": "Floor 4",
                "capacity": 5,
                "bsl_level": "BSL-2",
                "rate": 0.00,
                "status": "Maintenance",
                "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80",
                "description": "Cryogenic electron microscope suite with automated sample preparation for atomic-resolution macromolecular structures.",
                "equipment": ["Titan Krios Cryo-TEM", "Vitrobot Mark IV", "Gatan Energy Filter", "GPU Processing Cluster"]
            },
            {
                "id": "LAB-F202",
                "name": "AI & Robotics Testing Arena",
                "building": "AI & Autonomous Systems F",
                "floor": "Floor 2",
                "capacity": 15,
                "bsl_level": "BSL-1",
                "rate": 0.00,
                "status": "Available",
                "image": "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?auto=format&fit=crop&w=600&q=80",
                "description": "Reconfigurable modular testbed equipped with Vicon motion capture tracking and high-power computing racks.",
                "equipment": ["Vicon Motion Capture (16 Cam)", "NVIDIA HGX H100 Cluster", "Cobot Arms (UR5e)", "LIDAR Test Bench"]
            }
        ]

    if "reservations" not in st.session_state:
        today = date.today().strftime("%Y-%m-%d")
        st.session_state.reservations = [
            {
                "res_id": "RES-8921",
                "lab_id": "LAB-C302",
                "lab_name": "Organic Synthesis & Mass Spec",
                "researcher": "Dr. Elena Rostova",
                "department": "Medicinal Chemistry",
                "project": "PRJ-CANCER-DRUG-X",
                "date": today,
                "time_slot": "08:00 AM - 12:00 PM",
                "status": "Confirmed",
                "cost": 0.00
            },
            {
                "res_id": "RES-8922",
                "lab_id": "LAB-A101",
                "lab_name": "Molecular & Cell Biology Core",
                "researcher": "Prof. Marcus Vance",
                "department": "Biomedical Engineering",
                "project": "PRJ-GENE-EDIT-04",
                "date": (date.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
                "time_slot": "01:00 PM - 05:00 PM",
                "status": "Pending Approval",
                "cost": 0.00
            },
            {
                "res_id": "RES-8923",
                "lab_id": "LAB-B204",
                "lab_name": "Advanced Spectroscopy & Laser Suite",
                "researcher": "Dr. Sarah Chen",
                "department": "Applied Physics",
                "project": "PRJ-QUANTUM-OPTICS",
                "date": (date.today() + timedelta(days=2)).strftime("%Y-%m-%d"),
                "time_slot": "09:00 AM - 01:00 PM",
                "status": "Confirmed",
                "cost": 0.00
            }
        ]

def get_lab_by_id(lab_id: str):
    """Utility to retrieve lab object by ID."""
    for lab in st.session_state.get("labs", []):
        if lab["id"] == lab_id:
            return lab
    return None

def update_lab_status(lab_id: str, new_status: str):
    """Utility to update a lab's operational status."""
    for lab in st.session_state.get("labs", []):
        if lab["id"] == lab_id:
            lab["status"] = new_status
            return True
    return False

def cancel_reservation(res_id: str):
    """Utility to cancel a reservation by ID."""
    st.session_state.reservations = [
        r for r in st.session_state.get("reservations", []) if r["res_id"] != res_id
    ]

def approve_reservation(res_id: str):
    """Utility to approve a pending reservation."""
    for r in st.session_state.get("reservations", []):
        if r["res_id"] == res_id:
            r["status"] = "Confirmed"
            return True
    return False
