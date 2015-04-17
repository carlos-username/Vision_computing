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
from grayscale import *
from agujeros import adaptive_threshold
img2=gray_scale(argv[1])
img3=adaptive_threshold(img2)
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
def frecuencia1(arr): #getting frecuency
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
                                                
#convulucion_discreta
def magnitudes_resultado(image,mask):
    alto=len(image)
    ancho=len(image[0])
    mask_h=len(mask)
    mask_w=len(mask[0])
    magnitudes_r=[[0]*ancho for i in xrange(alto)]
    for i in xrange(1,alto-1):
        #row=[]
        for j in xrange(1,ancho-1):
            suma_r=0.0
            for m in xrange(mask_h):
                for b in xrange(mask_w):
                    vert=(i+m)-1
                    horiz=(j+b)-1
                    if vert<alto and horiz<ancho: #validating borders of matrix, working only on central pixels
                        suma_r+=image[vert][horiz]*mask[m][b] #getting Gx
            #row.append(suma_r)
            magnitudes_r[i][j]=suma_r
    return magnitudes_r
Gx=magnitudes_resultado(img,Sx)
Gy=magnitudes_resultado(img,Sy)
print "Gx: ", len(Gx), len(Gx[0])
print "Gy: ", len(Gy), len(Gy[0])
#print "lon_alto: ",len
def recorrido(image):
    alto=len(image)
    ancho=len(image[0])
    magnitudes=[]
    for y in xrange(1,alto-1):
        for x in xrange(1,ancho-1):
            resultado=math.sqrt(pow(Gx[y][x],2)+pow(Gy[y][x],2))
            radians=math.atan2(Gy[y][x],Gx[y][x])
            magnitudes.append((resultado,round(radians)))
    return magnitudes

histo=recorrido(img) #getting magnitudes
suma=0.0
for i in histo:
    suma+=i[0]
prom=suma/len(histo)
#print "len histo: ",len(histo)
#print histo
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
longitud_magn=len(histo)
#print frecuencias

#threshold=otsu_t2(frecuencias,img)
#print threshold
def main():
    for i in xrange(1,ancho-1): #Detecting edges by using previously calculated threshold
        for j in xrange(1,alto-1):
            if histo[r]>threshold:
                img[i][j]=255
                #pixeles.append((i,j))
                #vec=vecinos(i,j,img)
                #for m in vec:
                #    img[m[0]][m[1]]=255
            else:
                img[i][j]=0
            r+=1
    plt.imshow(img,cmap = cm.Greys_r) #Drawing modified image with detected shapes
    plt.show()
    
            

if __name__ == '__main__':
    main()
            
     
