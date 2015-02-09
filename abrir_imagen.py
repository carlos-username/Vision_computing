#!/usr/bin/python2

#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import cv2
def gray_scale(Img):
    image2 = cv2.imread(Img)
    image=cv2.resize(image2,(100,100))
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image
    #plt.imshow(gray_scale, cmap = cm.Greys_r)
    #plt.show()

def rgb_scale(Img):
    imag = cv2.imread(Img)
    img=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    return img
    #plt.imshow(img)
    #plt.show()
                            
    



