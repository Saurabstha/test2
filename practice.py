import numpy as np

import cv2

img = cv2.imread('images\\1.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

