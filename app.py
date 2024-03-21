from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Initialize Flask app
app = Flask(__name__)

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountkey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://faceattendancerealtime-e4bb4-default-rtdb.firebaseio.com/'
})

# Fetch a reference to the database service
ref = db.reference('Students/')  # Assuming 'Attendance' is the node containing attendance data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/attendance')
def attendance():
    # Fetch attendance data from Firebase Realtime Database
    attendance_data = ref.get()
    print("Attendance data:", attendance_data)  # Debug print
    return render_template('attendance.html', attendance_data=attendance_data)


if __name__ == '__main__':
    app.run(debug=True)
