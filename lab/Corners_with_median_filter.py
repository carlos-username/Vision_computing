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
import abrir_imagen
from grayscale import *
#img=gray_scale(argv[1])
#print img

def median(img):
    alto=len(img)
    ancho=len(img[0])
    img2=[[0]*ancho for j in xrange(alto)]
    for i in xrange(alto):
        for j in xrange(ancho):
            candidatos=[]
            coord=vecinos(i,j,img)
            rl=[]
            gl=[]
            bl=[]
            for m in coord:
                #candidatos.append(img[m[0]][m[1]])
                rl.append(img[m[0]][m[1]][0])
                gl.append(img[m[0]][m[1]][1])
                bl.append(img[m[0]][m[1]][2])
            media_r=len(rl)//2
            rm=sorted(rl)
            gm=sorted(gl)
            bm=sorted(bl)
            #print candidatos
            img2[i][j]=(rm[media_r],gm[media_r],bm[media_r])
    return img2

def main():
    #try:
    #imagen=abrir_imagen.rgb_scale(argv[1])
    new_image=abrir_imagen.rgb_scale(argv[1])
    #new_image=to_grayscale(imagen)
    #gray_scale
    #median_image=median(new_image)
    average_image=median(new_image)
    plt.imshow(average_image,cmap = cm.Greys_r)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    #plt.savefig(argv[2])
    plt.show()
    #except:
    #    print "Indicate an image as parameter"
        
if __name__ == '__main__':
    main()

                        
#img3=median(img)
#plt.imshow(img3,cmap = cm.Greys_r) #Drawing modified image with detected edges
#plt.show()

