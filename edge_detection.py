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
print img

ancho=len(img)
alto=len(img[0])
Sx=[[-1,0,1],[-2,0,2],[-1,0,1]] # Masks for the Sobel 3 3 3 operator
Sy=[[1,2,1],[0,0,0],[-1,-2,-1]]

mask_long=len(Sx) #gettng mask length
print "ancho: ",ancho
print "alto: ",alto
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
            resultado=abs(sumax)+abs(sumay) #Getting magnitudes by using absolute value
            #resultado=math.sqrt(pow(sumax,2)+pow(sumay,2))
            if resultado>255: #validating pixel ranges
                resultado=255
            magnitudes.append(resultado)
            #nuevo_array[i][j]=abs(sumax)+abs(sumay)
    return magnitudes

histo=recorrer() #getting magnitudes
print "histo->\n",histo
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

def cajas(element): #Grouping elements in 2-element boxes
    cajitas=[]
    kl=[]
    print element
    for k in element:
        kl.append(element[k])
    #res=0
    if len(kl)%2!=0:
        for n in xrange(0,len(kl),2):
            if n==len(kl)-1:
                res=kl[n]
                if res>255:
                    res=255.0
                cajitas.append(res)
            else:
                res=kl[n]+kl[n+1]
                if res>255:
                    res=255.0
                cajitas.append(res)
    else:
        for n in xrange(0,len(kl),2):
            res=kl[n]+kl[n+1]
            if res>255:
                res=255.0
            cajitas.append(res)

    return cajitas
                                
def prom(elm): #Getting average
    suma=0.0
    for u in elm:
        suma+=u
    return suma/len(elm)
caj=cajas(frecuencias) # Getting boxes

promedio=prom(caj) 
print "caj: ",caj
print "prom: ", promedio
for i in xrange(ancho): #Detecting edges by using previously calculated threshold
     for j in xrange(alto):
         if img[i][j]>=promedio+20:
             img[i][j]=255
         else:
             img[i][j]=0


plt.bar(range(0,len(caj)), caj) #Drawing histogram
plt.figure()
plt.imshow(img,cmap = cm.Greys_r) #Drawing modified image with detected edges
plt.show()

                    

