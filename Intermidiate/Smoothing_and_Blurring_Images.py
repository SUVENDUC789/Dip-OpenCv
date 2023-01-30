import cv2 as c
from matplotlib import pyplot as plt
import numpy as np

img = c.imread('images/noise.jpg')
img = c.cvtColor(img, c.COLOR_BGR2RGB)

kernal = np.ones((5, 5), np.float32)/25
dst = c.filter2D(img, -1, kernal)
blur = c.blur(img, (50, 50))
gblur = c.GaussianBlur(img, (5, 5), 0)

median=c.medianBlur(img,5)

title = ['Original', 'Filter', 'blur' ,'gblur','median']
images = [img, dst, blur,gblur,median]

for i in range(len(title)):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(title[i])
    plt.xticks([]), plt.yticks([])

plt.show()
