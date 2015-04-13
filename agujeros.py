#!/usr/bin/python2
#import matplotlib.pyplot as plt
import numpy as np
#from random import randint
import matplotlib.cm as cm
from sys import argv
import math
import matplotlib.pyplot as plt
#from dfs_and_vec import * 
#from grayscale import *
import abrir_imagen
from grayscale import *
from random import choice
from medias import *
from dfs_and_vec import *
from detectar_cuadro import *
#from grayscale import *
#img=gray_scale(argv[1])
#print img

def histogram_vertical(img,alto,ancho):
    dicc={}
    for y in xrange(alto):
        suma=0
        for x in xrange(ancho):
            suma+=img[y][x]
        dicc[y]=suma
    return dicc

def histogram_horizontal(img,alto,ancho):
    dicc={}
    for x in xrange(ancho):
        suma=0
        for y in xrange(alto):
            suma+=img[y][x]
        dicc[x]=suma
    return dicc

def frec(dic):
    nuevo={}
    for i in dic:
        if dic[i] in nuevo:
            nuevo[dic[i]]+=1
        else:
            nuevo[dic[i]]=1
    return nuevo

def descartar(histo,t):
    finales={}
    for i in histo:
        if histo[i]<t:
            finales[i]=histo[i]
    return finales

def promedio(histo):
    suma=0
    dic2={}
    for i in histo:
        suma+=histo[i]
    prom=suma/len(histo)
    for val in histo:
        if histo[val]<prom:
            dic2[val]=histo[val]
    return dic2

def lineas(img,img2,alto,ancho):
    #img=to_grayscale(image)
    hist=histogram(img)
    #tr_mg=otsu_t2(hist,alto*ancho)
    #blur = cv2.GaussianBlur(img,(5,5),0)
    binar=adaptive_threshold(img)
    binar2=median(binar)
    
    #binar=adaptive_thresh(img)
    #img=binarize(tr_mg,img)
    vertical=histogram_vertical(binar2,alto,ancho)
    #binar=adaptive_thresh(img)
    
    print "vertical: ",vertical
    horizontal=histogram_horizontal(binar2,alto,ancho)
    #frecuencia_h=frec(horizontal)
    
    #frecuencia_v=frec(vertical)
    #print "frecuencia_v: ", frecuencia_v
    #threshold_h=otsu_t2(frecuencia_h,len(frecuencia_h))
    #print "t_h",threshold_h
    #threshold_v=otsu_t2(frecuencia_v,len(frecuencia_v))
    #print "t_v",threshold_v
    #picos_v=descartar(vertical,threshold_v)
    #picos_h=descartar(horizontal,threshold_h)
    picos_h=promedio(horizontal)
    picos_v=promedio(vertical)
    #threshold_v=promedio(vertical)
    #picos_v=descartar(vertical,threshold_v)
    #picos_h=descartar(horizontal,threshold_h)   
    print "picos_v: ",picos_v
    print "picos_h: ",picos_h
    #print len(picos_v)
    #print len(picos_h)
    vert=[]
    horiz=[]
    color1=(255,0,0)
    for y in picos_v:        
        for x in xrange(ancho):
            img2[y][x]=color1
            
    color=(0,0,255)
    holes=[]
    for x in picos_h:
        for y in xrange(alto):            
            img2[y][x]=color
            if y+1<alto:
                if tuple(img2[y+1][x])==color1 and not binar2[y+1][x]:
                    holes.append((y,x))
                    img2[y][x]=(100,150,150)
    figura_actual=[]
    agujeros=[]
    agujeros_lon=[]
    while holes!=[]:
        inicio=choice(holes)
        figura_actual=imagendfs(binar2,inicio,holes,3)
        for i in figura_actual:
            holes.remove(i)
        agujeros.append(figura_actual)
        agujeros_lon.append(len(figura_actual))
    #print "agujeros",agujeros
    longs={}
    for i in agujeros_lon:
        if i in longs:
            longs[i]+=1
        else:
            longs[i]=1
    print "longs: ",longs
    t=otsu_t2(longs,len(longs))
    print "threshold_len: ",t
    for fig in agujeros:
        if len(fig)>=t:
            print "fig: ", fig
            caja_envolvente(fig,img2)
            
    return img2


def main():
    #try:
    imagen1=rgb_scale(argv[1])
    imagen2=gray_scale(argv[1])
    alto=len(imagen1)
    ancho=len(imagen1[0])
    print "alto: ",alto
    print "ancho: ",ancho
    ejemplo=lineas(imagen2,imagen1,alto,ancho)
            
    
    plt.imshow(ejemplo,cmap = cm.Greys_r)
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
