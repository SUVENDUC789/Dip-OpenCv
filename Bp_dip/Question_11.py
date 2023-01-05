# Write a program to add various types of noise (salt and pepper noise, Gaussian noise) to an image.

import cv2 as c
import numpy as np


def Paper_salt_Noise():
    img = c.imread('images/suvendu.jpg', 0)
    img = img/255
    # print(img)
    x, y = img.shape
    g = np.zeros((x, y), dtype=np.float32)
    paper = 0.05
    salt = 1-paper
    for i in range(x):
        for j in range(y):
            rdn = np.random.random()
            if rdn < paper:
                g[i][j] = 0
            elif rdn > salt:
                g[i][j] = 1
            else:
                g[i][j] = img[i][j]

    c.imshow('Image with noise', g)
    c.imshow('Original', img)


if __name__ == '__main__':
    Paper_salt_Noise()
    c.waitKey(0)
    c.destroyAllWindows()
