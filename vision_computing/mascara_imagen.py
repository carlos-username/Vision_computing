#!/usr/bin/python2
#import cv2
import matplotlib.pyplot as plt
import numpy as np
from random import randint
import matplotlib.cm as cm   
from sys import argv
from abrir_imagen import *
import math
import matplotlib.pyplot as plt
img=gray_scale(argv[1])
#img=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
#print img
ancho=len(img)
alto=len(img[0])
Sx=[[-1,0,1],[-2,0,2],[-1,0,1]]
Sy=[[1,2,1],[0,0,0],[-1,-2,-1]]
mask_long=len(Sx)
print "ancho: ",ancho
print "alto: ",alto
#convulucion_discreta
#blancos con ultimo valor en 0
def recorrer():
    for i in img:
        print i
    magnitudes=[]
    r=0
    #nuevo_array=[[0]*alto for i in xrange(ancho)]
    for i in xrange(1,ancho-1):
        for j in xrange(1,alto-1):
            sumax=0.0
            sumay=0.0
            for m in xrange(mask_long):
                for b in xrange(mask_long):
                    if (i+m)-1<ancho and (j+b)-1<alto:
                        sumax+=img[(i+m)-1][(j+b)-1]*Sx[m][b]
                        sumay+=img[(i+m)-1][(j+b)-1]*Sy[m][b]
                    if m==1 and b==1:
                        r+=1
            #print sumax
            #print sumay
            resultado=abs(sumax)+abs(sumay)
            #resultado=math.sqrt(pow(sumax,2)+pow(sumay,2))
            if resultado>255:
                resultado=255
            magnitudes.append(resultado)
            #nuevo_array[i][j]=abs(sumax)+abs(sumay)
    print "r: ",r
    print "magnitudes: ", len(magnitudes)
    print "restantes: ", (alto*ancho)-r
    return magnitudes

histo=recorrer()
print "histo->\n",histo
def frecuencia(arr):
    val=[]
    freq={}
    for j in xrange(len(arr)):
        val.append(arr[j])
        if arr[j] in val:
            if arr[j] in freq:
                freq[arr[j]]+=1
            else:
                freq[arr[j]]=1
    return freq
frecuencias=frecuencia(histo)
print "frecuencia-> \n",frecuencias

plt.bar(range(0,len(histo)), histo)
plt.figure()
#plt.show()
            
plt.imshow(img, cmap = cm.Greys_r)
#plt.figure()
plt.show()



#guardar la imagen nueva 
                    

