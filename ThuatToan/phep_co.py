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
def phep_co(img):
    co=np.zeros((img.shape[0] , img.shape[1] ))
    img = np.pad(img, pad_width=5, mode='constant', constant_values=255)
    for i in range(co.shape[0]):
        for j in range(co.shape[1]):
            check=True
            for k in range(SE.shape[0]):
                if check==False:
                    break
                for h in range(SE.shape[1]):
                    if(img[i+k][j+h]!=SE[k][h] and SE[k][h]==0):
                        co[i][j]=255
                        check=False
                        break
            if check:
                co[i][j]=0
    return co
            