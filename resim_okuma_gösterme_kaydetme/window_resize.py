import cv2

##cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.namedWindow("image")
img = cv2.imread("ank.jpeg")

img = cv2.resize(img,(640,480))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()