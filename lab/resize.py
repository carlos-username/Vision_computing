#!/usr/bin/python2
#import matplotlib.pyplot as plt
import numpy as np
#from random import randint
import matplotlib.cm as cm
from sys import argv
import math
import matplotlib.pyplot as plt
#from dfs_and_vec import * 
from grayscale import *
import abrir_imagen
#img=gray_scale(argv[1])
#print img

def resize(img,h_n,w_n):
    alto=len(img)
    print "alto: ",alto
    ancho=len(img[0])
    print "ancho: ",ancho
    #ratio_x=h_n/alto
    #ratio_y=w_n/ancho
    ratio_x = int((ancho<<20)/w_n) +1 #multiply by 65536 (Getting rid of decimals)
    print ratio_x
    ratio_y = int((alto<<20)/h_n) +1 #multiply by 65536 (Getting rid of decimals)
    print ratio_y
    img2=[[0]*w_n for j in xrange(h_n)]
    for y in xrange(h_n):
        for x in xrange(w_n):
            #y2=int(y/ratio_y) #for proportional dimensions
            #x2=int(x/ratio_x)
            y2=((y*ratio_y)>>20) #to divide by 65536 (this gets rid of decimals) 
            x2=((x*ratio_x)>>20) #to divide by 65536
            #y2=y*ratio_y/2**16 #to divide by 65536
            #x2=x*ratio_x/2**16 #to divide by 65536
            #print y2,x2
            img2[y][x]=img[y2][x2]

    return img2

def main():
    new_image=abrir_imagen.gray_scale(argv[1])
    alto=len(new_image)
    ancho=len(new_image[0])
    #Proportions=argv[2] #decide, 0 for making the image smaller or 1 for larger
    #if Proportions:
    #    Dim1=int(argv[3])
    #    Dim2=int(argv[4])
    #else:
    #    Dim1=alto/argv[3]
    #    Dim2=ancho/argv[4]
    Dim1=int(argv[2])
    Dim2=int(argv[3])
   
    resized_image=resize(new_image,Dim1,Dim2)
    print "new_image: ",len(resized_image),len(resized_image[0])
    plt.imshow(resized_image,cmap = cm.Greys_r)
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.savefig(argv[4])
    plt.show()
    #except:
    #    print "Indicate an image as parameter"
        
if __name__ == '__main__':
    main()


