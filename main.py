"""
Just display any image 
other window .
"""

# pip install opencv-python
import cv2 as c

# read image 2d or 3d form
img = c.imread('images/suv.jpg', 0)

# Just read the image
c.imshow('Suv-Image', img)

# waitkey method 
k = c.waitKey(0)

if k == ord('s'):
    # with out write image just destroy all window
    c.destroyAllWindows()
else:
    # create new image (Creating another file )
    c.imwrite('Suv_copy.png', img)

    # destroy another file
    c.destroyAllWindows()

# pip install -r requirments.txt