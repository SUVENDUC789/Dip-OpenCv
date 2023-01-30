import cv2
import numpy as np

# Load the image
image = cv2.imread('images/suv.jpg')

# Mean filtering
mean_filtered = cv2.blur(image, (5, 5))

# Weighted average filtering
weighted_average_filtered = cv2.boxFilter(image, -1, (5, 5), normalize=True)

# Median filtering
median_filtered = cv2.medianBlur(image, 5)

# Max filtering
max_filtered = cv2.dilate(image, np.ones((5, 5), np.uint8))

# Min filtering
min_filtered = cv2.erode(image, np.ones((5, 5), np.uint8))

# Save the filtered images
cv2.imwrite('mean_filtered.jpg', mean_filtered)
cv2.imwrite('weighted_average_filtered.jpg', weighted_average_filtered)
cv2.imwrite('median_filtered.jpg', median_filtered)
cv2.imwrite('max_filtered.jpg', max_filtered)
cv2.imwrite('min_filtered.jpg', min_filtered)

cv2.imshow('mean_filtered', mean_filtered)
cv2.imshow('weighted_average_filtered', weighted_average_filtered)
cv2.imshow('median_filtered', median_filtered)
cv2.imshow('max_filtered', max_filtered)
cv2.imshow('min_filtered', min_filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
