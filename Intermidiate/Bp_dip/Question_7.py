import cv2
import numpy as np

# Load the image and convert it to grayscale
image = cv2.imread('images/suv.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Brightness enhancement
brightness_enhanced = cv2.addWeighted(gray, 1.2, np.zeros(gray.shape, dtype=gray.dtype), 0, 10)

# Brightness suppression
brightness_suppressed = cv2.addWeighted(gray, 0.8, np.zeros(gray.shape, dtype=gray.dtype), 0, -10)

# Contrast manipulation
contrast_manipulated = cv2.addWeighted(gray, 1.5, np.zeros(gray.shape, dtype=gray.dtype), 0, 0)

# Gray level slicing without background
min_threshold = 50
max_threshold = 150
(thresholded, binary) = cv2.threshold(gray, min_threshold, max_threshold, cv2.THRESH_BINARY)

# Save the enhanced images
cv2.imwrite('brightness_enhanced.jpg', brightness_enhanced)
cv2.imwrite('brightness_suppressed.jpg', brightness_suppressed)
cv2.imwrite('contrast_manipulated.jpg', contrast_manipulated)
cv2.imwrite('gray_level_sliced.jpg', binary)

cv2.imshow('brightness_enhanced', brightness_enhanced)
cv2.imshow('brightness_suppressed', brightness_suppressed)
cv2.imshow('contrast_manipulated', contrast_manipulated)
cv2.imshow('binary', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
