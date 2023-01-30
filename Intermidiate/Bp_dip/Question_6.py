import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('images/suv.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply histogram equalization
equalized = cv2.equalizeHist(gray)

# Save the equalized image
cv2.imwrite('equalized.jpg', equalized)
cv2.imshow('Suvendu_equalized', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
