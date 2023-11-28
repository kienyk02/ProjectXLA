import cv2
import numpy as np

img=cv2.imread("loc_trung_vi/img1.jpg",0)
# convert to binary image
ret,binary_img=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow("Origin",img)
cv2.imshow("Binary",binary_img)

cv2.waitKey()