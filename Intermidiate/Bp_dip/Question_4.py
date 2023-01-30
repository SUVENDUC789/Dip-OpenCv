# Write a program to perform color separation into R, G, and B from an color image.


import cv2 as c

img = c.imread('images/rgb01.png')

b, g, r = c.split(img)

i1=c.imshow('blue Image',b)

i2=c.imshow('green Image',g)

i3=c.imshow('red Image',r)

c.imshow('Original',img)
c.waitKey(0)
c.destroyAllWindows()

