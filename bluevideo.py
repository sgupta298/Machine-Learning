#!/usr/bin/python3

import  cv2
import numpy as np
cam = cv2.VideoCapture(0)

while cam.isOpened():
	status,img = cam.read()
	onlyblue = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
	low=np.array([100,128,50])
	high=np.array([140,262,255])
	imgblue=cv2.inRange(onlyblue,low,high)
	maskedimage=cv2.bitwise_and(img,img,mask=imgblue)
	cv2.imshow('original',img)
	cv2.imshow('onlyblue',maskedimage)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cam.release()
cv2.destroyAllWindows()
