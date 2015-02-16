#!/usr/bin/python2

from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.cm as cm
img=rgb_scale(argv[1])
ancho=len(img)
alto=len(img[0])

def luminosity_cof(r,g,b): #luminosity coefficients
    return r*0.2126 + 0.7152*g + 0.0722*b

def suma(rgb):
    return sum(rgb)
def to_grayscale(img):
    img2=[[0]*alto for j in xrange(ancho)]
    for i in xrange(ancho):
        for j in xrange(alto):
            img2[i][j]=luminosity_cof(img[i][j][0],img[i][j][1],img[i][j][2])
    return img2
        #img2[i][j]=suma(img[i][j])
gray=to_grayscale(img)

plt.imshow(gray,cmap = cm.Greys_r)
plt.figure()
def binarizacion(imagen):
    for i in xrange(ancho):
        for j in xrange(alto):
            if imagen[i][j]<100:
                imagen[i][j]=0
            else:
                imagen[i][j]=255
    return imagen
binar=binarizacion(gray)
plt.imshow(binar,cmap = cm.Greys_r) #Drawing modified image with detected edges
plt.show()
