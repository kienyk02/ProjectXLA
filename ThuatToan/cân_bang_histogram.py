import cv2
import numpy as np

img=cv2.imread("tich_chap/img3.jpg",0)
img_hist=cv2.equalizeHist(img)
cv2.imshow("Origin",img)
cv2.imshow("Binary",img_hist)
cv2.waitKey()