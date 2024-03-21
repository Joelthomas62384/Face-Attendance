# Gesture Control Attendance System

Welcome to the Gesture Control Attendance System! This system allows you to manage attendance using gestures captured via a camera. Follow the steps below to set up and run the system effectively.

## Setup Instructions

### 1. Virtual Environment

First, create a virtual environment to manage dependencies. Run the following command in your terminal:

```bash
python -m venv venv
```

Activate the virtual environment:

- **For Windows**:

```bash
venv\Scripts\activate
```

- **For macOS and Linux**:

```bash
source venv/bin/activate
```

### 2. Install Dependencies

Install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### 3. Download Dlib

Download the Dlib library from external links and follow the installation instructions provided.

### 4. Set Up Firebase Database

Set up a Firebase database for storing attendance records. Ensure you have the necessary permissions and credentials.

### 5. Download Service Account Key

Download the `ServiceAccountKey.json` file from your Firebase project and place it in the project directory.

### 6. Code Setup

1. Bring the code from the designated location into your project directory.

2. Add images of the students to the `images` folder.

3. Run `image_resizer.py` to resize images.

4. Run `AddtoDataBase.py` to add resized images to the database.

5. Add storage bucket to `EncodeGenerator.py`.

### 7. Running the System

- Run `main.py` to register attendance using gestures.

- Run `app.py` to view the attendance table.

## Additional Notes

- Ensure that your camera is correctly configured and accessible by the system.

- Follow proper lighting conditions for accurate gesture detection.

- Troubleshoot any issues by referring to the system documentation or seeking assistance from the developers.

Happy attendance management with Gesture Control Attendance System! 🎉