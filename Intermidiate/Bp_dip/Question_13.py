import cv2 as c

img = c.imread('images/sudokubig.jpg', 0)

_, th = c.threshold(img, 127, 255, c.THRESH_BINARY)

th2 = c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_MEAN_C, c.THRESH_BINARY, 11, 2)
th3 = c.adaptiveThreshold(img, 255, c.ADAPTIVE_THRESH_GAUSSIAN_C, c.THRESH_BINARY, 11, 2)

c.imshow('Original', img)
c.imshow('Simple_Thresold', th)
c.imshow('Adaptive_Thresolding', th2)
c.imshow('Adaptive_Thresolding (GAUSSIAN)', th3)

c.waitKey(0)

c.destroyAllWindows()