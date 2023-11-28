import numpy as np


SE=np.array([[255,255,255,255,255,0,255,255,255,255,255],
             [255,255,255,255,0,0,0,255,255,255,255],
             [255,255,255,0,0,0,0,0,255,255,255],
             [255,255,0,0,0,0,0,0,0,255,255],
             [255,0,0,0,0,0,0,0,0,0,255],
             [0,0,0,0,0,0,0,0,0,0,0],
             [255,0,0,0,0,0,0,0,0,0,255],
             [255,255,0,0,0,0,0,0,0,255,255],
             [255,255,255,0,0,0,0,0,255,255,255],
             [255,255,255,255,0,0,0,255,255,255,255],
            [255,255,255,255,255,0,255,255,255,255,255]])
def phep_gian(img):
    gian=np.zeros((img.shape[0] , img.shape[1] ))
    img = np.pad(img, pad_width=5, mode='constant', constant_values=255)
    for i in range(gian.shape[0]):
        for j in range(gian.shape[1]):
            check=True
            for k in range(SE.shape[0]):
                if check==False:
                    break
                for h in range(SE.shape[1]):
                    if(img[i+k][j+h]==SE[k][h] and SE[k][h]==0):
                        gian[i][j]=0
                        check=False
                        break
            if check:
                gian[i][j]=255
    return gian
            