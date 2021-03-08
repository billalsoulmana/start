import cv2
import numpy as np
def mousePoints(event,x,y,flags,params):
	if event == cv2.EVENT_LBUTTONDOWN:
		print (x,y)

img = cv2.imread("Resources/cards.jpg")
cv2.imshow("output",img)
cv2.setMouseCallback("output",mousePoints)
cv2.waitKey(0)







