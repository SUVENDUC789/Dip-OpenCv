import cv2 as c

def hsv_To_Rgb():
    img_hsv=c.imread('suv_hsv.png')
    img_rgb=c.cvtColor(img_hsv,c.COLOR_HSV2BGR)
    c.imshow('hsv_to_Rgb',img_rgb)
    c.waitKey(0)
    c.destroyAllWindows()


if __name__=="__main__":
    hsv_To_Rgb()
