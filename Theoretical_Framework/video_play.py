import cv2

cap = cv2.VideoCapture("open_picture/hoop_video.mp4")

while (cap.isOpened()):
    play , frame = cap.read()
    
    if play == True :
        cv2.imshow("output", frame)
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()