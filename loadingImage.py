import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread('images\snowWhite.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('img', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img)
plt.show()