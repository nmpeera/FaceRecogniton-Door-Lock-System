import cv2
import numpy as np
from PIL import Image
import os

path = "Dataset"

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
trainer = cv2.face.createLBPHFaceRecognizer()

def getImagesAndLabels(path):
	imgPath = [os.path.join(path,f)for f in os.listdir(path)]
	samples = []
	ids = []
	for imagePath in imgPath:
		PIL_img = Image.open(imagePath).convert('L')
		imgNumpy = np.array(PIL_img, 'uint8')
		id = int(os.path.split(imagePath)[-1].split(".")[1])
		faces = faceCascade.detectMultiScale(imgNumpy)
		for (x,y,w,h) in faces:
			samples.append(imgNumpy[y:y+h, x:x+w])
			ids.append(id)
	return samples,ids

faces,ids = getImagesAndLabels(path)
trainer.train(faces,np.array(ids))
trainer.save('trainer.yml')
print("[INFO]{0} faces trained.".format(len(np.unique(ids))))
