#!/usr/bin/python2
#import cv2
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
            angulos.append((radians*180)/math.pi)
            #if resultado>255: #validating pixel ranges
            #    resultado=255
            magnitudes.append(resultado)
            #nuevo_array[i][j]=abs(sumax)+abs(sumay)
    return magnitudes

histo=recorrer() #getting magnitudes
#print "histo->\n",histo
def frecuencia(arr): #getting frecuency
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

def prom(elm): #Getting average
    suma=0.0
    for u in elm:
        suma+=u
    return suma/len(elm)
#caj=cajas(frecuencias) # Getting boxes
#promedio=prom(frecuencias)
#promedio=prom(histo) 
#print "caj: ",caj
#print "prom: ", promedio
longitud_magn=len(histo)
threshold=otsu_t2(frecuencias,ancho*alto)
print threshold
r=0
pixeles=[]
for i in xrange(1,ancho-1): #Detecting edges by using previously calculated threshold
     for j in xrange(1,alto-1):
         if histo[r]>threshold:
             img[i][j]=255
             pixeles.append((i,j))
         else:
             img[i][j]=0
         r+=1
plt.imshow(img,cmap = cm.Greys_r) #Drawing modified image with detected shapes
plt.show()
     
