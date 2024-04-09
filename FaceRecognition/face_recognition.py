import cv2
import numpy as np
import os
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.output(26, GPIO.HIGH)

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('trainer.yml')
path = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(path);
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names =['None','Noor','Kunal']

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while(True):
	ret,img = cam.read()
	img = cv2.flip(img, -1)
	img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(int(minW),int(minH)))

	for (x,y,w,h) in faces:
		cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
		id,check = recognizer.predict(gray[y:y+h,x:x+w])
		if (check<100):
			id = names[id]
			check = "{0}%".format(round(100 - check))
			GPIO.output(26,GPIO.LOW)
			GPIO.output(16,GPIO.HIGH)
			print("Opening Lock")
			time.sleep(10)
			GPIO.output(16,GPIO.LOW)
			GPIO.output(26,GPIO.HIGH)
		else:
			id = "unknown"
			check = "{0}%".format(round(100 - check))
			GPIO.output(16,GPIO.LOW)
                        GPIO.output(26,GPIO.HIGH)

		cv2.putText(img, str(id),(x+5,y-5), font, 1, (255,255,255), 2)
		cv2.putText(img, str(check), (x+5,y+h-5), font, 1, (255,255,0), 1)

	cv2.imshow('Camera', img)
	k = cv2.waitKey(10) & 0xff
	if k == 27:
		break

cam.release()
cv2.destroyAllWindows()
