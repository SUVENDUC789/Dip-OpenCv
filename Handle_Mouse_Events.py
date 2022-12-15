import cv2
import numpy as np
# print(type(dir(cv2)))

# for i in dir(cv2):
#     if 'EVENT' in i:
#         print(i)

# events=[i for i in dir(cv2) if 'EVENT' in i]

# for k,v in enumerate(events):
#     print(k,v)


def click_event(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        print(x," ",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+","+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2)
        cv2.imshow('imagge',img)

img=np.zeros((512,512,3),np.uint8)
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()


