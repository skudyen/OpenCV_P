import cv2
img = cv2.imread("open_picture/hoop2.jpg")

cv2.imshow("output", img) #Show out put picture
cv2.waitKey(delay=5000) #Setup the delay //the deley has * by (ms)1000
cv2.destroyAllWindows() #Is open the window picture
