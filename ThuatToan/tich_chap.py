import cv2
import numpy as np

# img=cv2.imread("tich_chap/img5.png",0)
# img=cv2.equalizeHist(img) # cân bằng histogram
# cv2.imshow("Origin",img)

def tichchap(Img,Kernel):
    
    high=Kernel.shape[0] # lấy số hàng và cột của ma trận kernel
    wide=Kernel.shape[1]
    Tichchap=np.zeros((Img.shape[0] , Img.shape[1] ))
    Img = np.pad(Img, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=0)
    for i in range(Tichchap.shape[0]):
        for j in range(Tichchap.shape[1]):
            Tichchap[i,j]= (Img[i:i+high, j:j+wide]*Kernel).sum()
    return Tichchap

# rõ biên
Kernel_1=np.array([[1/3,1/3,1/3],
                   [1/3,1/3,1/3],
                   [1/3,1/3,1/3]])

# rõ biên
Kernel_2=np.array([[1,0,0],
                   [0,1,0],
                   [0,0,1]])

# làm mờ
Kernel_3=Kernel_1*(1/3)

# Prewitt
Kernel_prewitt_X=np.array([[-1,0,1],
                    [-1,0,1],
                    [-1,0,1]])
Kernel_prewitt_Y=np.array([[-1,-1,-1],
                    [0,0,0],
                    [1,1,1]])

# Dãn nở
Kernel_4=np.array([[1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1],
                   [1,1,1,1,1]])

# img2=tichchap(img,Kernel_prewitt_Y)+tichchap(img,Kernel_prewitt_X)

cv2.waitKey()

