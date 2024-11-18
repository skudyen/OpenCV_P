import cv2

cap = cv2.VideoCapture(0) #parameter that point to camera

while (True):
    vcap , frame = cap.read() #receive frame form cam frame by frame
    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()