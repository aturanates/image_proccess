import cv2
import numpy as np

img = cv2.imread("ank.jpeg",0)
img = cv2.resize(img,(640,640))
row,col = img.shape

M = np.float32([[1,0,20],[0,1,100]])

dst = cv2.warpAffine(img,M,(row,col))

cv2.imshow("dst",dst)
print(img)

cv2.waitKey(0)
cv2.destroyAllWindows()