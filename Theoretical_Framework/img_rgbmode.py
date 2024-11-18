import cv2

img = cv2.imread("open_picture/hoop3.jpg",0) #this section is change the color mode.

cv2.imshow("output", img)
cv2.waitKey(delay=5000)
cv2.destroyAllWindows()