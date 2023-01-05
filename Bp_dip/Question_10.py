import cv2 as c

def main():
    ms=c.imread('images/ms.jfif')
    India=c.imread('images/india.jfif')

    ms=c.resize(ms,(512,512))
    India=c.resize(India,(512,512))

    final_add=c.add(India,ms)
    f_sub=c.subtract(India,ms)
    f_mul=c.multiply(India,ms)
    f_div=c.divide(India,ms)

    c.imshow('Final',final_add)
    c.imshow('Final_Sub',f_sub)
    c.imshow('Final_Mul',f_mul)
    c.imshow('Final_Div',f_div)

if __name__ == '__main__':
    main()
    c.waitKey(0)
    c.destroyAllWindows()
