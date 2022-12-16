import cv2 as c 

img1=c.imread('images/rolls_royce.jpeg')
img2=c.imread('images/suv.jpg')

img1=c.resize(img1,(512,512))
img2=c.resize(img2,(512,512))

final=c.add(img1,img2)

c.imshow('final',final)

c.waitKey(0)

c.destroyAllWindows()
