import cv2

img = cv2.imread("open_picture/hoop4.jpg", 0)

cv2.imshow("hoop", img)

cv2.imwrite("outhoop.jpg", img) #Output name should be have file type

cv2.waitKey(delay=5000)
cv2.destroyAllWindows() #