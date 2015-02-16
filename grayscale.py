#!/usr/bin/python2

from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.cm as cm

# img=rgb_scale(argv[1])
ancho=len(img)
alto=len(img[0])
img2=[[0]*alto for j in xrange(ancho)]
def luminosity_cof(r,g,b): #luminosity coefficients
    return r*0.2126 + 0.7152*g + 0.0722*b

def suma(rgb):
    return sum(rgb)

for i in xrange(ancho):
    for j in xrange(alto):
        img2[i][j]=luminosity_cof(img[i][j][0],img[i][j][1],img[i][j][2])
        #img2[i][j]=suma(img[i][j])

plt.imshow(img2,cmap = cm.Greys_r) #Drawing modified image with detected edges
plt.show()
