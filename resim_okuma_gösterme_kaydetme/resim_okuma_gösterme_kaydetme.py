import cv2

img = cv2.imread("ank.jpeg")
##img = cv2.imread("ank.jpeg",cv2.IMREAD_GRAYSCALE)
##print(img)
cv2.namedWindow("image",cv2.WINDOW_NORMAL)
cv2.imshow("image",img)
cv2.imwrite("ank1.jpeg",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
