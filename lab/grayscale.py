#!/usr/bin/python2

#from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys
import cv2
sys.path.append('../')
import abrir_imagen

def luminosity_cof(r,g,b): #luminosity coefficients
    return r*0.2126 + 0.7152*g + 0.0722*b

def suma(rgb):
    return sum(rgb)

def to_grayscale(img):
    alto=len(img)
    ancho=len(img[0])
    img2=[[0]*ancho for j in xrange(alto)]
    for i in xrange(ancho):
        for j in xrange(alto):
            img2[i][j]=round(luminosity_cof(img[i][j][0],img[i][j][1],img[i][j][2]))
    return img2

def main():
    try:
        imagen=abrir_imagen.rgb_scale(argv[1])
        new_image=to_grayscale(imagen)
        plt.imshow(new_image,cmap = cm.Greys_r)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.savefig(argv[2])
        plt.show()
    except:
        print "Indicate an image as parameter and the name of image"
    
if __name__ == '__main__':
    main()
