import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountkey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': ''
})
app = firebase_admin.get_app()
database_url = app.options.get('databaseURL')

print("Database URL:", database_url)

ref = db.reference('Students')

data = {
    "13321138031": {
        "name": "Joel Thomas",
        "major": "English",
        "starting_year": 2022,
        "total_attendance": 6,
        "gender": "M",
        "year": 4,
        "last_attendance_time": "2024-3-19 00:54:34"
    },
    "13321138027": {
        "name": "Elon Musk",
        "major": "Physics",
        "starting_year": 2023,
        "total_attendance": 12,
        "gender": "M",
        "year": 2,
        "last_attendance_time": "2024-3-19 00:54:34"
    },
    "13321138009": {
        "name": "Mohanlal",
        "major": "Economics",
        "starting_year": 2021,
        "total_attendance": 2,
        "gender": "M",
        "year": 1,
        "last_attendance_time": "2024-3-19 00:54:34"
    },
    "13321138007": {
        "name": "Mammotty",
        "major": "Malayalam",
        "starting_year": 2021,
        "total_attendance": 6,
        "gender": "M",
        "year": 1,
        "last_attendance_time": "2024-3-19 00:54:34"
    },
    "13321138002": {
        "name": "ShahRukh Khan",
        "major": "English",
        "starting_year": 2022,
        "total_attendance": 6,
        "gender": "M",
        "year": 4,
        "last_attendance_time": "2024-3-19 00:54:34"
    }
}

for key, value in data.items():
    ref.child(key).set(value)
