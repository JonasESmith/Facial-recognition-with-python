import numpy as np
import cv2
from PIL import ImageGrab

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# profile_cascade = cv2.CascadeClassifier('haarcascade_profileface.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
# fullbody_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# this grabs the first camera attached to the computer
cap = cv2.VideoCapture(0)
while True:

    # this grabs the screen
    # I use the bellow line when I want to the ability on group photos or videos
    ## frame = np.array(ImageGrab.grab(bbox=(0, 40, 800, 600)))

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # edges = cv2.Canny(frame, 100, 100)
    faces = face_cascade.detectMultiScale(gray, 1.15, 5)
    # profile = profile_cascade.detectMultiScale(gray, 1.2, 5)
    # fullbody = fullbody_cascade.detectMultiScale(gray)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #roi_gray = gray[y:y+h, x:x+w]
        #roi_color = frame[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray, 1.01, 5)
        #for (ex,ey,ew,eh) in eyes:
        #    cv2.rectangle(roi_color, (ex, ey ), (ex+ew, ey+eh), (0, 255, 0), 2)
    #for (x, y, w, h) in profile:
    #    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    #for (x, y, w, h) in fullbody:
    #    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # shows the frame
    cv2.imshow('window', frame)
    # press Q to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

