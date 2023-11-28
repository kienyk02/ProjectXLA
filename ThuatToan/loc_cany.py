import cv2


def loc_canny(Img, low_threshold, high_threshold):
    # Làm mờ ảnh để giảm nhiễu
    Img_blurred = cv2.GaussianBlur(Img, (5, 5), 0)
    
    # Phát hiện cạnh bằng phương pháp Canny
    edges = cv2.Canny(Img_blurred, low_threshold, high_threshold)
    
    return edges