import cv2 
import numpy as np
# img=cv2.imread("loc_trung_vi/img1.jpg",0)
def AmBan(Img):  
    img_amban=np.zeros((Img.shape[0], Img.shape[1] ))
    for i in range(Img.shape[0]):
        for j in range(Img.shape[1]):
            img_amban[i][j]=255-Img[i,j]         
    return img_amban


cv2.waitKey()