# Write a program to average two images together into a single image. Display the new image.

import cv2 as c 

ms=c.imread('images/ms.jfif')
India=c.imread('images/india.jfif')

ms=c.resize(ms,(512,512))
India=c.resize(India,(512,512))

final=c.add(India,ms)

c.imshow('Ms Dhoni',ms)
c.imshow('India',India)
c.imshow('Final',final)

c.waitKey(0)
c.destroyAllWindows()