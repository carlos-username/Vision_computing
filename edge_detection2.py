#!/usr/bin/python2
#import cv2
from math import cos,sin,pi
from random import choice
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import matplotlib.cm as cm   
from sys import argv
from abrir_imagen import *
import math
import matplotlib.pyplot as plt
from medias import * #filters
import math
from dfs_and_vec import * #subroutine for dfs
from detectar_cuadro import * #detect box
img2=gray_scale(argv[1])
img=median(img2)
#histo_x=histogram(img3)
#img=binarize(otsu_t2(histo_x,img3),img3)
ancho=len(img)
alto=len(img[0])
Sx=[[-1,0,1],[-2,0,2],[-1,0,1]] # Masks for the Sobel 3 3 3 operator
Sy=[[1,2,1],[0,0,0],[-1,-2,-1]]

mask_long=len(Sx) #gettng mask length
print "ancho: ",ancho
print "alto: ",alto
angulos=[]
#convulucion_discreta
#blancos con ultimo valor en 0
def recorrer(): #getting gradient magnitudes
    magnitudes=[] #vector for magnitudes

    for i in xrange(1,ancho-1):
        for j in xrange(1,alto-1):
            sumax=0.0
            sumay=0.0
            for m in xrange(mask_long):
                for b in xrange(mask_long):
                    if (i+m)-1<ancho and (j+b)-1<alto: #validating borders of matrix, working only on central pixels
                        sumax+=img[(i+m)-1][(j+b)-1]*Sx[m][b] #getting Gx
                        sumay+=img[(i+m)-1][(j+b)-1]*Sy[m][b] #Getting Gy
            #resultado=abs(sumax)+abs(sumay) #Getting magnitudes by using absolute value
            resultado=math.sqrt(pow(sumax,2)+pow(sumay,2))
            radians=math.atan2(sumay,sumax)
            #radians=(radians*180)/math.pi
            #angulos.append(radians)
            #if resultado>255: #validating pixel ranges
            #    resultado=255
            magnitudes.append((resultado,radians))
            #nuevo_array[i][j]=abs(sumax)+abs(sumay)
    return magnitudes

histo=recorrer() #getting magnitudes
#print "histo->\n",histo
def frecuencia(arr): #getting frecuency
    freq={}
    for j in xrange(len(arr)):
        if arr[j][0] in freq:
            freq[arr[j][0]]+=1
        else:
            freq[arr[j][0]]=1
    return freq
frecuencias=frecuencia(histo)
#print frecuencias

#threshold=otsu_t2(frecuencias,img)
#print threshold
        
     
