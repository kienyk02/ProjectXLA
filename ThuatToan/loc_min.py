import numpy as np


def loc_min(Img): 
    img_MIN=np.zeros((Img.shape[0], Img.shape[1]))
    Img = np.pad(Img, pad_width=((1, 1), (1, 1)), mode='constant', constant_values=0)
    for i in range(img_MIN.shape[0]):
        for j in range(img_MIN.shape[1]):
            temp=[Img[i,j],Img[i,j+1],Img[i,j+2],
                  Img[i+1,j],Img[i+1,j+1],Img[i+1,j+2],
                  Img[i+2,j],Img[i+2,j+1],Img[i+2,j+2]]
            temp.sort()
            img_MIN[i,j]= temp[0]
    return img_MIN