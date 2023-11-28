import cv2


def loc_otsu(Img):
    # Áp dụng phương pháp Otsu để chuyển đổi thành ảnh nhị phân
    _, binary_otsu = cv2.threshold(Img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return binary_otsu