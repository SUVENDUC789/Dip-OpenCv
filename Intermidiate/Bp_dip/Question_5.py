import cv2 as c
import numpy as np


def Image_negative(img):
    img = 255-img
    c.imshow('Image negative', img)


def Log_transformation():
    img = c.imread('images/spec.webp', 0)
    img2 = np.uint8(np.log1p(img))
    _, img2 = c.threshold(img2, 1, 255, c.THRESH_BINARY)
    c.imshow('Original log', img)
    c.imshow('After log', img2)


def Power_law_transform_OR_Gamma_Transformation():
    img = c.imread('images/sp.webp', 0)
    img2 = np.power(img, 2)
    img3 = np.power(img, 3)
    img4 = np.power(img, 4)

    c.imshow('Original spi', img)
    c.imshow('p2 spi', img2)
    c.imshow('p3 spi', img3)
    c.imshow('p4 spi', img4)


def main():
    img = c.imread('images/suv.jpg', 0)
    c.imshow('Original', img)
    Image_negative(img)


if __name__ == '__main__':
    main()
    Log_transformation()
    Power_law_transform_OR_Gamma_Transformation()
    c.waitKey(0)
    c.destroyAllWindows()
