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
def adaptive_threshold(image):
    alto=len(image)
    ancho=len(image[0])
    int_image=[[0]*ancho for i in xrange(alto)]
    salida=[[0]*ancho for i in xrange(alto)]
    S = ancho/8
    s2 = S/2
    T = 22.0
    #T = 15.0
    #s=4
    for y in xrange(alto):
        suma=0
        for x in xrange(ancho):
            suma+=image[y][x]
            if not i:
                int_image[y][x]=suma
            else:
                int_image[y][x]=suma+int_image[y-1][x]

    for y in xrange(alto):
        for x in xrange(ancho):
            y0=max(y-s2,0)
            y1=min(y+s2,alto-1)
            x0=max(x-s2,0)
            x1=min(x+s2,ancho-1)
            conta=(x1-x0)*(y1-y0)
            #suma=int_image[y2][x2]-int_image[y1-1][x2]-int_image[y2][x1-1]+int_image[y1-1][x1-1]
            suma = int_image[y1][x1]-int_image[y0][x1]-int_image[y1][x0]+int_image[y0][x0]
            if image[y][x]*conta < suma*(100.-T)/100.:
                salida[y][x]=0
            else:
                salida[y][x]=255
    return salida

def lineas(img,img2,alto,ancho):
    hist=histogram(img)
    binar=adaptive_threshold(img)
    binar2=median(binar)
    vertical=histogram_vertical(binar2,alto,ancho)
    print "vertical: ",vertical
    horizontal=histogram_horizontal(binar2,alto,ancho)
    picos_h=promedio(horizontal)
    picos_v=promedio(vertical)
    print "picos_v: ",picos_v
    print "picos_h: ",picos_h
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
    #agujeros_lon=[]
    agu_porciento=[]
    while holes!=[]:
        inicio=choice(holes)
        figura_actual=imagendfs(binar2,inicio,holes,3)
        for i in figura_actual:
            holes.remove(i)
        agujeros.append(figura_actual)
        #agujeros_lon.append(len(figura_actual))
        porcientos=centro_masa(binar2,figura_actual)
        agu_porciento.append(porcientos[2]) #by percentage
    #print "agujeros",agujeros
    longs={}
    for i in agu_porciento:
        if i in longs:
            longs[i]+=1
        else:
            longs[i]=1
    print "longs: ",longs
    t=otsu_t2(longs,len(longs))
    print "threshold_len: ",t
    conta=0
    for fig in agujeros:
        print agu_porciento[conta]
        if agu_porciento[conta]>=t:
            color=(randint(60,230),randint(110,210),randint(70,255))
            print "fig: ", fig
            caja_envolvente(fig,img2)
            for i in fig:
                img2[i[0]][i[1]]=color
        conta+=1
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


