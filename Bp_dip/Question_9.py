# Write a program to compare two images using image subtraction.

import cv2 as c

img1=c.imread('images/suv.jpg')
img2=c.imread('images/suvendu.jpg')
img2=c.imread('images/spi.jpg')

if img1.shape == img2.shape :
    print('Image have same size and channels')

    difference=c.subtract(img1,img2)
    b,g,r=c.split(difference)

    if c.countNonZero(b) ==0 and c.countNonZero(g)==0 and c.countNonZero(r)==0:
        print('Image are Equal')
else :
    print('Image are not equal')


c.imshow('Image 1',img1)
c.imshow('Image 2',img2)

c.waitKey(0)
c.destroyAllWindows()