#ROI
import cv2
import numpy as np

img = cv2.imread("ank.jpeg")
print(img.shape[:2])

roi = img[400:600,1000:1200]

img = cv2.resize(img,(640,480))
cv2.imshow("image",img)
cv2.imshow("roi",roi)
cv2.waitKey(0)
cv2.destroyAllWindows()