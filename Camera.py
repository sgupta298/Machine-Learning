import cv2
import time
cam = cv2.VideoCapture(0)
print(cam.isOpened())
if(cam.isOpened()):
    print("camera is ready to a capture")
else:
    print("error with opening camera")
if(cam.isOpened()):
    status,frame = cam.read()
    time.sleep(2)
    cv2.imshow("captured image",frame)
    cv2.imwrite("picture.jpeg",frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()