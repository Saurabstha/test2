import numpy
import cv2

face_cascade = cv2.CascadeClassifier('xml\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('xml\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+h, y+h), (255, 0, 0), 2)
        cv2.rectangle(img, (x, y), (x + 40, y + 20), (255, 0, 0), 2)
        cv2.putText(img, 'Face', (x,y), font, 2, (100, 100, 100), 3, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
            # cv2.putText(img, 'eye', (ex, ey), font, 2, (100, 100, 100), 3, cv2.LINE_AA)

        cv2.imshow('img', img)
        k = cv2.waitKey(30) & 0xff == ord('q')
        if k == 27:
            break

cap.release()
cv2.destroyAllWindow()