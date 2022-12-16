import cv2 as c

img = c.imread('images/gradient0_to_255.jpg', 0)

# if pixel value is lessthen 127 then value is 0 other wise 255
_, th1 = c.threshold(img, 127, 255, c.THRESH_BINARY)

# uppercase reverse
_, th2 = c.threshold(img, 127, 255, c.THRESH_BINARY_INV)

# i dont know what is doing 
_, th3 = c.threshold(img, 127, 255, c.THRESH_TRUNC)
_, th4 = c.threshold(img, 127, 255, c.THRESH_TOZERO)
_, th5 = c.threshold(img, 127, 255, c.THRESH_TOZERO_INV)

c.imshow('Image', img)
# c.imshow('th1', th1)
# c.imshow('th2', th2)
# c.imshow('th3', th3)
c.imshow('th4', th4)
c.imshow('th5', th5)

c.waitKey(0)
c.destroyAllWindows()
