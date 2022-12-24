import cv2 as c
import numpy as np
from matplotlib import pyplot as plt


img = c.imread('images/sudokubig.jpg', 0)

_, mask = c.threshold(img, 100, 255, c.THRESH_BINARY_INV)

kernal = np.ones((20, 20), np.uint8)
dilation = c.dilate(mask, kernal, iterations=2)
erosion = c.erode(mask, kernal, iterations=2)

titles = ['images', 'mask', 'dilation', 'erosion']
images = [img, mask, dilation, erosion]

for i in range(len(images)):
    plt.subplot(2, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
