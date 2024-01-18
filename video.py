import cv2

cap=cv2.VideoCapture(-1) # video reading.... 0,1,-1 is the webcam index,change it according to our system

#to read frame by frame
while True:
    success,frame=cap.read() #we should give 2 variable name here.
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#to view frame by frame 
    cv2.imshow('video_capture',frame) #display the video frame by frame.
    if cv2.waitKey(1) & 0XFF==27:# 0XFF--ASCI character of ESC key.
        break
cap.release()
cv2.destroyAllWindows()