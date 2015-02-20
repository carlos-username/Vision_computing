#!/usr/bin/python2
#subroutine to change image to grayscale
from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
#import numpy as np
import matplotlib.cm as cm
#img=rgb_scale(argv[1])

def luminosity_cof(r,g,b): #luminosity coefficients
    return r*0.2126 + 0.7152*g + 0.0722*b

def suma(rgb):
    return sum(rgb)
def to_grayscale(img):
    ancho=len(img)
    alto=len(img[0])
    img2=[[0]*alto for j in xrange(ancho)]
    for i in xrange(ancho):
        for j in xrange(alto):
            img2[i][j]=luminosity_cof(img[i][j][0],img[i][j][1],img[i][j][2])
    return img2

