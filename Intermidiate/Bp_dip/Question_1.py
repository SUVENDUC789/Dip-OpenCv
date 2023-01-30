import cv2 as c 
from hsv_to_Rgb import hsv_To_Rgb as h2r

def how_many_color_format_support():
    for i in dir(c):
        if 'COLOR_' in i:
            print(i)

def rgb_to_gray_convart():
    img = c.imread('images/suv.jpg')
    img_gray=c.cvtColor(img,c.COLOR_BGR2GRAY)
    c.imshow('Suvendu_Gray_Window',img_gray)
    c.waitKey(0)
    c.destroyAllWindows()

def rgb_to_Hsv_convart():
    img = c.imread('images/suv.jpg')
    img_hsv=c.cvtColor(img,c.COLOR_BGR2HSV)
    c.imshow('Suvendu_Hsv_Window',img_hsv)
    c.imwrite('suv_hsv.png',img_hsv)
    c.waitKey(0)
    c.destroyAllWindows()


def gray_to_binary_convart():
    img=c.imread('images/suv.jpg',0)
    ret,binary=c.threshold(img,127,256,c.THRESH_BINARY)
    c.imshow('Suvendu_Binary_Window',binary)
    c.waitKey(0)
    c.destroyAllWindows()

def rgb_to_binary():
    gray_to_binary_convart()

if __name__=="__main__":
    rgb_to_gray_convart()
    gray_to_binary_convart()
    rgb_to_binary()
    rgb_to_Hsv_convart()
    h2r()
