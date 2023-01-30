import cv2 as c 

img = c.imread('images/suv.jpg',0)

ret,img=c.threshold(img,127,256,c.THRESH_BINARY)
c.imshow('Gray_Image',img)
c.imwrite('2bitImage.png',img)
c.waitKey(0)
c.destroyAllWindows()