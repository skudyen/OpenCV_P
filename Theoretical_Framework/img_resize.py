import cv2

img = cv2.imread("open_picture/hoop3.jpg")
imgresize = cv2.resize(img, (900,1000))


cv2.imshow("output", imgresize)
cv2.waitKey(delay=7000)
cv2.destroyAllWindows()