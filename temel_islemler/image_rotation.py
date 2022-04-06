import cv2
import numpy as np

img = cv2.imread("ank.jpeg",0)
img = cv2.resize(img,(640,480))
row,col = img.shape

M = cv2.getRotationMatrix2D((row/2,col/2),270,1)

dst = cv2.warpAffine(img,M,(col,row))

cv2.imshow("dst",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()