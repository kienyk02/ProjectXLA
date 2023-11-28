# Bộ lọc Laplacian
import cv2
import numpy as np

from ThuatToan.tich_chap import tichchap


laplacian_kernel = np.array([[0, 1, 0],
                             [1, -4, 1],
                             [0, 1, 0]])

def loc_laplacian(Img):
    img_laplacian=tichchap(Img,laplacian_kernel)
    img_laplacian = img_laplacian.astype(Img.dtype)
    # Chuẩn hóa ảnh Laplacian
    img_laplacian = cv2.normalize(img_laplacian, None, 0, 255, cv2.NORM_MINMAX)
    
    # Tăng cường ảnh gốc bằng ảnh Laplacian
    img_enhanced = cv2.addWeighted(Img, 1.5, img_laplacian, 0.5, 0)
    return img_enhanced