import numpy as np
import cv2

img = cv2.imread('images\ss.jpg', cv2.IMREAD_COLOR)

img[100, 100] = [255, 255, 255]
pixelValue = img[100,100]

# img[100:200, 100:200] = [255, 255, 255]

eye_region = img[100:200, 100:200]
img[0:100, 0:100] = eye_region


print(pixelValue)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()