import cv2
import numpy as np

# img=cv2.imread("loc_trung_vi/img1.jpg")
# img=cv2.resize(img,(0,0),fx=1.1,fy=1.1)
# cv2.imshow("Origin",img)
# img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# img=cv2.equalizeHist(img)

def trungvi(Img): 
    Trungvi=np.zeros((Img.shape[0], Img.shape[1] ))
    Img = np.pad(Img, pad_width=1, mode='constant', constant_values=0)
    for i in range(Trungvi.shape[0]):
        for j in range(Trungvi.shape[1]):
            temp=[Img[i,j],Img[i,j+1],Img[i,j+2],
                  Img[i+1,j],Img[i+1,j+1],Img[i+1,j+2],
                  Img[i+2,j],Img[i+2,j+1],Img[i+2,j+2]]
            temp.sort()
            Trungvi[i,j]= temp[4]
    return Trungvi
# lọc nhiễu hạt
# img2=trungvi(img)
# img2=np.uint8(img2)
# cv2.imshow("trung vi",img2)
# k=cv2.waitKey()
# if k==ord("s"):
#     cv2.imwrite("loc_trung_vi/anhmoi.jpg",img2)