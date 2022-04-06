import cv2
import numpy as np

img = cv2.imread("ank.jpeg")
img = cv2.resize(img,(640,480))

img_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("image",img)
cv2.imshow("image1",img_rgb)
cv2.imshow("image2",img_hsv)
cv2.imshow("image3",img_gray)


cv2.waitKey(0)
cv2.destroyAllWindows()