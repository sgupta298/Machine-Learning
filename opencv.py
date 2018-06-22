import cv2
img = cv2.imread("cat01.jpg")
img2 = cv2.imread("cat02.jpg")
img3 = cv2.imread("cat03.jpg")
cv2.line(img,(2,5),(400,329),(213,45,67),3)
cv2.circle(img3,(259,308),25,(0,255,0),5)
cv2.rectangle(img2,(60,60),(435,278),(0,0,255),4)
font=cv2.FONT_HERSHEY_COMPLEX
cv2.putText(img3,"CAT",(48,489),font,20,(28,56,178),8)
cv2.imshow("cat",img)
cv2.imshow("catrec",img2)
cv2.imshow("catcirc",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
