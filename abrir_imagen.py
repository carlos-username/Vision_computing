#!/usr/bin/python2

#from grayscale import *
import cv2
def gray_scale(Img):
    image2 = cv2.imread(Img)
    #image2=cv2.resize(image2,(300,300))
    #image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #gray_image = to_grayscale(image)
    gray_image=cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    return gray_image

def rgb_scale(Img):
    imag = cv2.imread(Img)
    #imag=cv2.resize(imag,(300,300))
    img=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    return img
                            
    



