#!/usr/bin/python2
#import matplotlib.pyplot as plt
import numpy as np
#from random import randint
import matplotlib.cm as cm
from sys import argv
from abrir_imagen import *
import math
import matplotlib.pyplot as plt
from dfs_and_vec import * 

#img=gray_scale(argv[1])
#print img

def median(img):
    ancho=len(img)
    alto=len(img[0])
    for i in xrange(ancho):
        for j in xrange(alto):
            candidatos=[]
            coord=vecinos(i,j,img)
            for m in coord:
                candidatos.append(img[m[0]][m[1]])
            media=len(candidatos)//2
            values=sorted(candidatos)
            img[i][j]=values[media]
    return img
#plt.imshow(img,cmap = cm.Greys_r) #Drawing modified image with detected edges
#plt.show()

