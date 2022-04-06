import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("ank.jpeg",0)
img = cv2.resize(img,(640,480))

ret,th1 = cv2.threshold(img,127,200,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)

cv2.imshow("IMG",img)
cv2.imshow("IMG th1",th1)
cv2.imshow("IMG th2",th2)
cv2.imshow("IMG th3",th3)


cv2.waitKey(0)
cv2.destroyAllWindows()