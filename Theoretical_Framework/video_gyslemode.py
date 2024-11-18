import cv2

cap =cv2.VideoCapture("open_picture/hoop_video.mp4")

while cap.isOpened :
    play , frame = cap.read()

    if play :
        videoresize = cv2.resize(frame, (550,400))
        grey = cv2.cvtColor(videoresize,cv2.COLOR_BGR2GRAY)
        cv2.imshow("output", grey)
        if cv2.waitKey(10) & 0xFF == ord ("q") :
            break
    else :
        break
cap.release()
cv2.destroyAllWindows()