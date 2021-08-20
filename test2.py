import time
import numpy as np
import cv2
import torch
import torch.backends.cudnn as cudnn
from models.experimental import attempt_load
from utils.general import non_max_suppression
import telepot
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

from firebase import firebase
import os
import pyrebase
import os


def save1(date_, url, number):
    my_image = url
    storage.child("Detected").child(my_image).put(my_image)
    time.sleep(1)
    users_ref.push().set({
        'number': number,
        'url': url,
        'date': date_,
    })





# telegram  
# Replace with your token
token = '1944147483:AAFz_reVI6EtLhK8bRoHfHjjf29JqtRxQY0'  # telegram token
# Replace with your receiver id
receiver_id = 1266606453  # https://api.telegram.org/bot1944147483:AAFz_reVI6EtLhK8bRoHfHjjf29JqtRxQY0/getUpdates
bot = telepot.Bot(token)
bot.sendMessage(receiver_id, 'Your camera is active now.')  # send a message on telegram

# Firebase

# Fetch the service account key JSON file contents
cred = credentials.Certificate('serviceAccountKey.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://becarful-canada-default-rtdb.firebaseio.com/'
})

ref = db.reference('')
users_ref = ref.child('Images')

config = {
    "apiKey": "ae04102012555bfcae7ebdae8b6c9ea38ae2eb3f",
    "authDomain": "https://accounts.google.com/o/oauth2/auth",
    "databaseURL": "https://becarful-canada-default-rtdb.firebaseio.com/",
    "projectId": "becarful-canada",
    "storageBucket": "becarful-canada.appspot.com",
    "messagingSenderId": "104645753169902597075"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

camera = 0  # webcam
# Capture with opencv and detect object
path = ''
# path = '/content/yolov5'
weights = f'best_face.pt'
# weights = f'best_yolov5.pt'
device = torch.device('cpu')

model = attempt_load(weights, map_location=device)  # load FP32 model
stride = int(model.stride.max())  # model stride
cudnn.benchmark = True
cam = cv2.VideoCapture(0)
time.sleep(2)

# gs://becarful-canada.appspot.com

while (cam.isOpened()):
    time.sleep(0.2)  # wait for 0.2 second
    ret, frame = cam.read()
    if ret == True:
        now = time.time()
        img = torch.from_numpy(frame).float().to(device).permute(2, 0, 1)
        img /= 255.0  # 0 - 255 to 0.0 - 1.0

        if img.ndimension() == 3:
            img = img.unsqueeze(0)

        pred = model(img, augment=False)[0]
        pred = non_max_suppression(pred, 0.01, 0.01, classes=0, agnostic=True)  # img, conf, iou, classes, ...

        print('time -> ', time.time() - now)

        for det in pred:
            if len(det):
                print(det)
                time_stamp = int(time.time())
                fcm_photo = f'{time_stamp}.png'
                cv2.imwrite(fcm_photo, frame)  # notification photo
                # bot.sendPhoto(receiver_id, photo=open(fcm_photo, 'rb'))  # send message to telegram
                now = datetime.now()
                # dd/mm/YY H:M:S
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
                save1(dt_string, fcm_photo, "")
                # time.sleep(1)  # wait for 1 second. Only when it detects.


    else:
        break

cam.release()
cv2.destroyAllWindows()
