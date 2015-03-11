#!/usr/bin/python2
#import matplotlib.pyplot as plt
import numpy as np
#from random import randint
import matplotlib.cm as cm
from sys import argv
import math
import matplotlib.pyplot as plt
from dfs_and_vec import * 
from grayscale import *
#img=gray_scale(argv[1])
#print img

def median(img):
    ancho=len(img)
    alto=len(img[0])
    img2=[[0]*alto for j in xrange(ancho)]
    for i in xrange(ancho):
        for j in xrange(alto):
            candidatos=[]
            coord=vecinos(i,j,img)
            for m in coord:
                candidatos.append(img[m[0]][m[1]])
            media=len(candidatos)//2
            values=sorted(candidatos)
            img2[i][j]=values[media]
    return img2
def main():
    try:
        imagen=abrir_imagen.rgb_scale(argv[1])
        new_image=to_grayscale(imagen)
        median_image=median(new_image)
        plt.imshow(new_image,cmap = cm.Greys_r)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.savefig(argv[2])
        plt.show()
    except:
        print "Indicate an image as parameter"
        
if __name__ == '__main__':
    main()

                        
#img3=median(img)
#plt.imshow(img3,cmap = cm.Greys_r) #Drawing modified image with detected edges
#plt.show()

