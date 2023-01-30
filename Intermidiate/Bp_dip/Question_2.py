import cv2 as c

def Anticlockwise():
    img = c.imread('images/suv.jpg')
    rows, cols, ht = img.shape
    matrix=c.getRotationMatrix2D((rows/2,cols/2),60,1)
    new_img=c.warpAffine(img,matrix,(cols,rows))
    c.imshow('Anticlockwise_Output',new_img)


def clockwise():
    img = c.imread('images/suv.jpg')
    rows, cols, ht = img.shape
    matrix=c.getRotationMatrix2D((rows/2,cols/2),-60,1)
    new_img=c.warpAffine(img,matrix,(cols,rows))
    c.imshow('clockwise_Output',new_img)


if __name__=="__main__":
    clockwise()
    Anticlockwise()
    c.waitKey(0)
    c.destroyAllWindows()