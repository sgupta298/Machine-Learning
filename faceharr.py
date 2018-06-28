#!/usr/bin/python3
import cv2
import numpy as np
face_data = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
eye_data = cv2.CascadeClassifier("haarcascade_eye.xml")
cap = cv2.VideoCapture(0)
while cap.isOpened():
	status,frame = cap.read()
	grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	eye = eye_data.detectMultiScale(grayimg,1.15,5)
	faces = face_data.detectMultiScale(grayimg,1.15,5)
	for (x,y,w,h) in eyeg:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]	
	for (x,y,w,h) in faces:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		roi_gray=grayimg[y:y+h,x:x+w]
		roi_color=frame[y:y+h,x:x+w]		
	cv2.imshow('faces',frame)
	if cv2.waitKey(10) &0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()