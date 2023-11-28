# Bộ lọc Sobel cho phương ngang
import cv2
import numpy as np

from ThuatToan.tich_chap import tichchap


sobel_x = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])

# Bộ lọc Sobel cho phương dọc
sobel_y = np.array([[-1, -2, -1],
                   [0, 0, 0],
                   [1, 2, 1]])
def loc_sobel(Img):
    img_sobel_x=tichchap(Img,sobel_x)
    img_sobel_y=tichchap(Img,sobel_y)
    # img_sobel_x = cv2.filter2D(Img, cv2.CV_64F, sobel_x) / 8.0  # 8.0 là một hệ số để giảm độ lớn
    # img_sobel_y = cv2.filter2D(Img, cv2.CV_64F, sobel_y) / 8.0
    img_sobel = np.sqrt(img_sobel_x**2 + img_sobel_y**2).astype(np.uint8)
    return img_sobel