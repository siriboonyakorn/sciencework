"""
Mock data for the LabRoom app.
Provides lab rooms, periods, courses, instructors, and reservation data.
"""
import random
from datetime import datetime, timedelta

# ── Period Definitions ───────────────────────────────────────────────────────
PERIODS = [
    {"id": 1, "name": "Period 1", "short": "P1", "start": "08:30", "end": "09:30"},
    {"id": 2, "name": "Period 2", "short": "P2", "start": "09:30", "end": "10:30"},
    {"id": 3, "name": "Period 3", "short": "P3", "start": "10:30", "end": "11:30"},
    {"id": 4, "name": "Period 4", "short": "P4", "start": "11:30", "end": "12:30"},
    {"id": 5, "name": "Period 5", "short": "P5", "start": "13:00", "end": "14:00"},
    {"id": 6, "name": "Period 6", "short": "P6", "start": "14:00", "end": "15:00"},
    {"id": 7, "name": "Period 7", "short": "P7", "start": "15:00", "end": "16:00"},
    {"id": 8, "name": "Period 8", "short": "P8", "start": "16:00", "end": "17:00"},
]

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
DAYS_SHORT = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# ── Lab Rooms ────────────────────────────────────────────────────────────────
LABS = [
    {
        "id": "A101",
        "name": "Computer Lab A101",
        "building": "Building A",
        "floor": "1st Floor",
        "capacity": 40,
        "equipment": ["💻 Computers", "📽️ Projector", "❄️ AC", "📋 Whiteboard"],
        "description": "A modern computer lab with 40 workstations running the latest "
                       "software for programming, data analysis, and design courses.",
        "icon": "🖥️",
        "available_count": 32,
    },
    {
        "id": "B201",
        "name": "Physics Lab B201",
        "building": "Building B",
        "floor": "2nd Floor",
        "capacity": 30,
        "equipment": ["🔬 Lab Equipment", "📽️ Projector", "❄️ AC", "📋 Whiteboard"],
        "description": "Equipped for physics experiments including optics, mechanics, "
                       "and electromagnetic theory labs.",
        "icon": "⚛️",
        "available_count": 18,
    },
    {
        "id": "B202",
        "name": "Chemistry Lab B202",
        "building": "Building B",
        "floor": "2nd Floor",
        "capacity": 25,
        "equipment": ["🧫 Lab Equipment", "🌬️ Fume Hoods", "❄️ AC", "🚿 Safety Shower"],
        "description": "Full chemistry lab with fume hoods, reagent storage, and safety "
                       "equipment for organic and inorganic chemistry practicals.",
        "icon": "🧪",
        "available_count": 12,
    },
    {
        "id": "C301",
        "name": "Electronics Lab C301",
        "building": "Building C",
        "floor": "3rd Floor",
        "capacity": 35,
        "equipment": ["📟 Oscilloscopes", "📡 Function Generators", "📽️ Projector", "💻 Computers"],
        "description": "Electronics and electrical engineering lab with oscilloscopes, "
                       "function generators, breadboards, and component kits.",
        "icon": "⚡",
        "available_count": 24,
    },
    {
        "id": "A102",
        "name": "Biology Lab A102",
        "building": "Building A",
        "floor": "1st Floor",
        "capacity": 30,
        "equipment": ["🔬 Microscopes", "🧫 Lab Equipment", "❄️ AC", "📋 Whiteboard"],
        "description": "Biology lab equipped with high-quality microscopes, specimen "
                       "storage, and preparation areas for microbiology and anatomy labs.",
        "icon": "🧬",
        "available_count": 20,
    },
    {
        "id": "D401",
        "name": "Multimedia Lab D401",
        "building": "Building D",
        "floor": "4th Floor",
        "capacity": 20,
        "equipment": ["💻 iMacs", "🎧 Audio Equipment", "📽️ Projector", "🎬 Green Screen"],
        "description": "Multimedia production lab with iMacs, professional audio "
                       "equipment, and a green screen for video and content production.",
        "icon": "🎨",
        "available_count": 14,
    },
]

# ── Courses ──────────────────────────────────────────────────────────────────
COURSES = [
    "CS101 - Intro to Computer Science",
    "CS201 - Data Structures",
    "CS301 - Algorithms",
    "PHY101 - Physics I",
    "PHY201 - Physics II",
    "CHM101 - General Chemistry",
    "CHM201 - Organic Chemistry",
    "BIO101 - General Biology",
    "EE101 - Circuit Theory",
    "EE201 - Digital Electronics",
    "MM101 - Digital Media",
    "MM201 - Video Production",
]

# ── Instructors ──────────────────────────────────────────────────────────────
INSTRUCTORS = [
    "Dr. Smith",
    "Dr. Johnson",
    "Prof. Williams",
    "Dr. Brown",
    "Prof. Davis",
    "Dr. Wilson",
    "Prof. Anderson",
    "Dr. Taylor",
]

# ── Mock Users ───────────────────────────────────────────────────────────────
MOCK_USER = {
    "id": "64010001",
    "name": "John Doe",
    "email": "john.doe@university.edu",
    "role": "student",
    "department": "Computer Science",
}

# ── Reservations ─────────────────────────────────────────────────────────────
def get_user_reservations():
    """Return mock reservations for the current user."""
    today = datetime.now()
    return [
        {
            "id": 1,
            "lab_id": "A101",
            "lab_name": "Computer Lab A101",
            "date": (today + timedelta(days=1)).strftime("%Y-%m-%d"),
            "day": (today + timedelta(days=1)).strftime("%A"),
            "period": 3,
            "period_time": "10:30 - 11:30",
            "status": "approved",
            "purpose": "CS201 Lab Session - Linked Lists",
            "course": "CS201 - Data Structures",
            "instructor": "Dr. Smith",
            "student_count": 35,
            "created_at": (today - timedelta(days=2)).strftime("%Y-%m-%d"),
        },
        {
            "id": 2,
            "lab_id": "B201",
            "lab_name": "Physics Lab B201",
            "date": (today + timedelta(days=2)).strftime("%Y-%m-%d"),
            "day": (today + timedelta(days=2)).strftime("%A"),
            "period": 5,
            "period_time": "13:00 - 14:00",
            "status": "pending",
            "purpose": "PHY101 Optics Experiment",
            "course": "PHY101 - Physics I",
            "instructor": "Dr. Johnson",
            "student_count": 28,
            "created_at": (today - timedelta(days=1)).strftime("%Y-%m-%d"),
        },
        {
            "id": 3,
            "lab_id": "C301",
            "lab_name": "Electronics Lab C301",
            "date": (today + timedelta(days=3)).strftime("%Y-%m-%d"),
            "day": (today + timedelta(days=3)).strftime("%A"),
            "period": 2,
            "period_time": "09:30 - 10:30",
            "status": "approved",
            "purpose": "EE201 Circuit Lab",
            "course": "EE201 - Digital Electronics",
            "instructor": "Prof. Williams",
            "student_count": 30,
            "created_at": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
        },
        {
            "id": 4,
            "lab_id": "A101",
            "lab_name": "Computer Lab A101",
            "date": (today - timedelta(days=5)).strftime("%Y-%m-%d"),
            "day": (today - timedelta(days=5)).strftime("%A"),
            "period": 1,
            "period_time": "08:30 - 09:30",
            "status": "completed",
            "purpose": "CS101 Python Workshop",
            "course": "CS101 - Intro to Computer Science",
            "instructor": "Dr. Smith",
            "student_count": 38,
            "created_at": (today - timedelta(days=8)).strftime("%Y-%m-%d"),
        },
        {
            "id": 5,
            "lab_id": "B202",
            "lab_name": "Chemistry Lab B202",
            "date": (today - timedelta(days=3)).strftime("%Y-%m-%d"),
            "day": (today - timedelta(days=3)).strftime("%A"),
            "period": 6,
            "period_time": "14:00 - 15:00",
            "status": "rejected",
            "purpose": "CHM201 Titration Lab",
            "course": "CHM201 - Organic Chemistry",
            "instructor": "Dr. Brown",
            "student_count": 22,
            "created_at": (today - timedelta(days=6)).strftime("%Y-%m-%d"),
        },
        {
            "id": 6,
            "lab_id": "A102",
            "lab_name": "Biology Lab A102",
            "date": (today - timedelta(days=7)).strftime("%Y-%m-%d"),
            "day": (today - timedelta(days=7)).strftime("%A"),
            "period": 4,
            "period_time": "11:30 - 12:30",
            "status": "cancelled",
            "purpose": "BIO101 Microscopy Lab",
            "course": "BIO101 - General Biology",
            "instructor": "Dr. Wilson",
            "student_count": 25,
            "created_at": (today - timedelta(days=10)).strftime("%Y-%m-%d"),
        },
    ]


def get_schedule(lab_id, week_offset=0):
    """
    Generate a deterministic mock weekly schedule for a lab room.
    Returns a dict: { day_name: { period_id: { "status": ..., "info": ... } } }
    """
    rng = random.Random(hash(f"{lab_id}_{week_offset}_seed42"))
    schedule = {}

    for day in DAYS:
        schedule[day] = {}
        for period in PERIODS:
            r = rng.random()
            if day in ("Saturday", "Sunday"):
                # Weekends are mostly available
                if r < 0.85:
                    status = "available"
                elif r < 0.95:
                    status = "reserved"
                else:
                    status = "my_reservation"
            else:
                # Weekdays have more reservations
                if r < 0.45:
                    status = "available"
                elif r < 0.72:
                    status = "reserved"
                elif r < 0.85:
                    status = "my_reservation"
                else:
                    status = "pending"

            info = {"status": status}
            if status == "reserved":
                info["reserved_by"] = rng.choice(["Alice Chen", "Bob Lee", "Carol Kim", "David Park"])
                info["course"] = rng.choice(COURSES)
            elif status == "my_reservation":
                info["reserved_by"] = MOCK_USER["name"]
                info["course"] = rng.choice(COURSES)
            elif status == "pending":
                info["reserved_by"] = MOCK_USER["name"]
                info["course"] = rng.choice(COURSES)

            schedule[day][period["id"]] = info

    return schedule


def get_week_dates(week_offset=0):
    """Get the start and end dates of the current week with an offset."""
    today = datetime.now()
    start = today - timedelta(days=today.weekday()) + timedelta(weeks=week_offset)
    end = start + timedelta(days=6)
    week_number = start.isocalendar()[1]

    dates = {}
    for i, day in enumerate(DAYS):
        d = start + timedelta(days=i)
        dates[day] = d.strftime("%b %d")

    return {
        "start": start.strftime("%b %d"),
        "end": end.strftime("%b %d, %Y"),
        "week_number": week_number,
        "dates": dates,
    }


def get_dashboard_stats():
    """Get summary statistics for the dashboard."""
    reservations = get_user_reservations()
    today = datetime.now().strftime("%Y-%m-%d")

    return {
        "available_labs": len(LABS),
        "my_reservations": len([r for r in reservations if r["status"] in ("approved", "pending")]),
        "today_reservations": len([r for r in reservations if r["date"] == today]),
        "upcoming": len([r for r in reservations
                        if r["date"] >= today and r["status"] in ("approved", "pending")]),
    }
