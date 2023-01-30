import cv2 as c


cap=c.VideoCapture(0);

while True:
    ret,frame=cap.read()
    gray=c.cvtColor(frame,c.COLOR_BGR2GRAY)
    c.imshow('Frame-suv',gray)

    if c.waitKey(0) == ord('q'):
        break

cap.release()
c.destroyAllWindows()