import cv2 
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(cap.isOpened()):
    ret,frame=cap.read()
    if ret == True:
        # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        font=cv2.FONT_HERSHEY_SIMPLEX
        text=str(datetime.datetime.now())
        frame=cv2.putText(frame,text,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)

        cv2.imshow('Frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()