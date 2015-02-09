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
from k_means import *
img=gray_scale(argv[1])
#img=[[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]
print img

ancho=len(img)
alto=len(img[0])
Sx=[[-1,0,1],[-2,0,2],[-1,0,1]]
Sy=[[1,2,1],[0,0,0],[-1,-2,-1]]
#Sx=[[-1,0,1],[-1,0,1],[-1,0,1]]
#Sy=[[1,1,1],[0,0,0],[-1,-1,-1]]

mask_long=len(Sx)
print "ancho: ",ancho
print "alto: ",alto
#convulucion_discreta
#blancos con ultimo valor en 0
def recorrer():
    magnitudes=[]
    for i in xrange(1,ancho-1):
        for j in xrange(1,alto-1):
            sumax=0.0
            sumay=0.0
            for m in xrange(mask_long):
                for b in xrange(mask_long):
                    if (i+m)-1<ancho and (j+b)-1<alto:
                        sumax+=img[(i+m)-1][(j+b)-1]*Sx[m][b]
                        sumay+=img[(i+m)-1][(j+b)-1]*Sy[m][b]
            resultado=abs(sumax)+abs(sumay)
            if resultado>255:
                resultado=255
            magnitudes.append(resultado)
            #nuevo_array[i][j]=abs(sumax)+abs(sumay)
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

def cajas(element):
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
def prom(elm):
    suma=0.0
    for u in elm:
        suma+=u
    return suma/len(elm)
caj=cajas(frecuencias)
#print caj
        
#def get_threshold(frecuencias):
#B = np.reshape(histo, (ancho, alto))
#B=np.resize(histo, 10).reshape(5,2)
#print "redimension: \n",B
#K_clustering(2,1,B)
#print "frecuencia-> \n",frecuencias
promedio=prom(caj)
print "caj: ",caj
print "prom: ", promedio
for i in xrange(ancho):
     for j in xrange(alto):
         if img[i][j]>=promedio+20:
             img[i][j]=255
         else:
             img[i][j]=0


plt.bar(range(0,len(caj)), caj)
plt.figure()


#plt.bar(range(0,len(histo)), histo)
#plt.figure()
#plt.show()
# #print histo
#K_clustering(2,3,converted)

plt.imshow(img,cmap = cm.Greys_r)
# #plt.figure()
plt.show()



#guardar la imagen nueva 
                    

