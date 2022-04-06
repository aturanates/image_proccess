import cv2
import numpy as np

img = cv2.imread("ank.jpeg",0)
img = cv2.resize(img,(640,480))

kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)


cv2.imshow("Original",img)
cv2.imshow("Erosion",erosion)
cv2.imshow("Dilation",dilation)
cv2.imshow("Open",opening)
cv2.imshow("Close",closing)
cv2.imshow("Gradient",gradient)
cv2.imshow("Tophat",tophat)



cv2.waitKey(0)
cv2.destroyAllWindows()