import numpy as np
import cv2

img = cv2.imread('images\snowWhite.png', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (100,100), (255,255,255), 10)
cv2.rectangle(img, (20,20), (200,200), (0,255,0),20)
cv2.circle(img, (500, 500),100, (0,0,255), 15, )

pts = np.array([[100,100],[500,100],[100,500],[600,1000]],np.int32)
# pts = pts.res
cv2.polylines(img, [pts], True, (0,0,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Snow White!!', (100,100), font, 2, (100,100,100), 3, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()