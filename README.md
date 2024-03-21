# Gesture Control Attendance System

Welcome to the Gesture Control Attendance System! This system allows you to take attendance using gestures captured through a camera. Follow the steps below to set up and use the system.

## Installation

1. **Create Virtual Environment**: Set up a Python virtual environment using `venv`:
   ```bash
   python -m venv venv
   ```

   ```
   /venv/Scripts/activate.ps1
   ```


2. **Download Dlib**: Visit the [GitHub repository](https://github.com/z-mahmud22/Dlib_Windows_Python3.x) and download the Dlib library. Follow the instructions provided in the repository to ensure you download the correct version for your system.

   - For Windows users, download the Dlib library from the provided GitHub link.
   - For other operating systems, please refer to the official Dlib documentation for installation instructions.

   Once downloaded, proceed with the installation according to your operating system and Python version.

    For Windows users:
        - Open a command prompt.
        - Navigate to the directory where you downloaded the Dlib library.
        - Use pip to install the library by running the following command, replacing `[path_to_downloaded_file]` with the actual path to the downloaded file and `[python_version]` with your Python version:


            
            pip install [path_to_downloaded_file]\[dlib_library_file_name].whl
            

    For example:

         
            pip install C:\Downloads\dlib-19.22.0-cp39-cp39-win_amd64.whl
            

   Make sure to adjust the file name and path according to the version you downloaded and your Python version.


    ```bash
    pip install path/to/the/dlibfile/
    ```

3. **Install Dependencies**: Install required Python packages from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```



3. **Download Dlib**: Visit the [GitHub repository](https://github.com/z-mahmud22/Dlib_Windows_Python3.x) and download the Dlib library. Follow the instructions provided in the repository to ensure you download the correct version for your system.

   - For Windows users, download the Dlib library from the provided GitHub link.
   - For other operating systems, please refer to the official Dlib documentation for installation instructions.

   Once downloaded, proceed with the installation according to your operating system and Python version.

For Windows users:
   - Open a command prompt.
   - Navigate to the directory where you downloaded the Dlib library.
   - Use pip to install the library by running the following command, replacing `[path_to_downloaded_file]` with the actual path to the downloaded file and `[python_version]` with your Python version:


     ```
     pip install [path_to_downloaded_file]\[dlib_library_file_name].whl
     ```

     For example:

     ```
     pip install C:\Downloads\dlib-19.22.0-cp39-cp39-win_amd64.whl
     ```

   Make sure to adjust the file name and path according to the version you downloaded and your Python version.


```bash
pip install path/to/the/dlibfile/
```

## Database Setup

1. **Firebase Database**: Set up your Firebase database and obtain the `serviceAccountKey.json` file.

## Getting Started

1. **Add Student Images**: Place the images of students in the `images` folder.

2. **Image Resizer**: Run `image_resizer.py` to resize the images for better processing.

3. **Add to Database**: Run `AddtoDataBase.py` to add student information to the database.

4. **Encode Generator**: Add your storage bucket to `Encode Generator.py` and run the script to generate encodings.

5. **Attendance Registration**: Run `main.py` to start capturing gestures and register attendance.

6. **View Attendance**: Run `app.py` to view the attendance table.

## Supported Formats

The system supports image formats: JPEG, JPG, and PNG.

## License

This project is licensed to Joel Thomas. See the [LICENSE](LICENSE) file for details.

For any questions or issues, please contact kattuparamban1103@gmail.com.

Thank you for using the Gesture Control Attendance System!