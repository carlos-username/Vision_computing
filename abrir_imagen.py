#!/usr/bin/python2

#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import cv2
from grayscale import *
def gray_scale(Img):
    image2 = cv2.imread(Img)
    #image=cv2.resize(image2,(200,200))
    gray_image = to_grayscale(image2)
    return gray_image

def rgb_scale(Img):
    imag = cv2.imread(Img)
    #imag=cv2.resize(imag,(200,200))
    img=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    return img
                            
    



