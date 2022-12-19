# Dip-OpenCv
OpenCV is a library of programming functions mainly aimed at real-time computer vision. 

### Simple image Thresholding :
```python
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
c.imshow('th1', th1)
c.imshow('th2', th2)
c.imshow('th3', th3)
c.imshow('th4', th4)
c.imshow('th5', th5)

c.waitKey(0)
c.destroyAllWindows()

```

### Adaptive image Thresholding :
```python
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
```