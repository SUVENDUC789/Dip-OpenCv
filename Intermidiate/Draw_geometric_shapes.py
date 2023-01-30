import cv2 as c

img = c.imread('images/suv.jpg', 1)

# img = c.line(img, (0, 0), (255, 255), (255, 0, 0), 10)
# img=c.arrowedLine(img, (0, 0), (255, 255), (255, 0, 0), 10)
# img=c.rectangle(img,(300+100+80,100),(350-20,200),(0,0,255),3)
img=c.circle(img,(480-80,200-10-40),80-8,(0,255,0),5)

c.imshow('My Image', img)

k = c.waitKey(0)

if k == ord('q'):
    c.destroyAllWindows()
