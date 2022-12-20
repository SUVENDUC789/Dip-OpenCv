import cv2 as c
from matplotlib import pyplot as plt

img = c.imread('images/suv.jpg', -1)
c.imshow('Original', img)

# convert image bgr to rgb 
img = c.cvtColor(img, c.COLOR_BGR2RGB)

plt.imshow(img)

plt.xticks([])
plt.yticks([])

plt.show()

c.waitKey(0)
c.destroyAllWindows()
