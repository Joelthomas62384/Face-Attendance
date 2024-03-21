import cv2
import face_recognition
import os
import pickle
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountkey.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': '',
    'storageBucket': ''
})


# Importing the Student images 

folderPath = 'images'
imgPathList = os.listdir(folderPath)
imgList = []
studentId_list = []
for path in imgPathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path))) 
    studentId_list.append(path.split(".")[0])
    filename = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(filename)
    blob.upload_from_filename(filename)
    

print(studentId_list)


def findEncodings(imagesList):
    encode_list = []
    for img in imagesList:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encode_list.append(encode)
    return encode_list

print("Encoding Started...")

encodeList = findEncodings(imgList)

encodeListId =  [encodeList,studentId_list]
print("Encoding Complete...")

# print(encodeList)


file = open("encodeFile.p","wb")
pickle.dump(encodeListId,file)
file.close()

print("File Saved...")


