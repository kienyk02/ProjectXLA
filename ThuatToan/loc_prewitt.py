import cv2
import numpy as np

from ThuatToan.tich_chap import tichchap


kernel_prewitt_x = np.array([[-1, 0, 1],
                             [-1, 0, 1],
                             [-1, 0, 1]])

kernel_prewitt_y = np.array([[-1, -1, -1],
                             [0, 0, 0],
                             [1, 1, 1]])
def loc_prewitt(Img):
    img_prewitt_x=tichchap(Img,kernel_prewitt_x)
    img_prewitt_y=tichchap(Img,kernel_prewitt_y)
    # img_prewitt_x = cv2.filter2D(Img, cv2.CV_64F, kernel_prewitt_x)/8.0
    # img_prewitt_y = cv2.filter2D(Img, cv2.CV_64F, kernel_prewitt_y)/8.0
    img_prewitt = np.sqrt(img_prewitt_x**2 + img_prewitt_y**2).astype(np.uint8)
    return img_prewitt