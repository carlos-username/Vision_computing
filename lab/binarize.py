#!/usr/bin/python2

#from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
from grayscale import * 
#import numpy as np
#import matplotlib.cm as cm
#img=rgb_scale(argv[1])
def histogram(imagen):
    Diccionario_colores={}
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            if imagen[i][j] in Diccionario_colores:
                Diccionario_colores[imagen[i][j]]+=1
            else:
                Diccionario_colores[imagen[i][j]]=1
    return Diccionario_colores
                                                                            
def otsu_t2(hist,imagen):  #Using otsu automatic threshold, based on: http://en.wikipedia.org/wiki/Otsu%27s_method    
    #total=len(imagen)*len(imagen[0])
    total=imagen #normally size of image
    bins_number = len( hist ) # histogram size (how many groups were formed)
    sum_total = 0.0
    for x in hist:
        sum_total += x * hist[x]

    weight_BR   = 0.0
    weight_FR   = 0.0
    sum_BR   = 0.0
    vmax=-1
    t=0
    for threshold in hist:
        # background weight is going to be incremented, meanwhile foreground weight will be diminished
        weight_BR += hist[threshold]
        if weight_BR == 0:
            continue

        weight_FR = total - weight_BR 
        if weight_FR == 0:
            break

        sum_BR += threshold * hist[threshold]
        average_background = sum_BR / weight_BR
        average_foreground = (sum_total - sum_BR) / weight_FR

        varb=weight_BR * weight_FR * pow(average_background - average_foreground,2)
        if varb>vmax: #get the threshold
            vmax=varb
            t=threshold
            
    return t

def binarize(threshold,imagen):
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            if imagen[i][j]>threshold:
                imagen[i][j]=255
            else:
                imagen[i][j]=0
    return imagen

def main():
    try:
        imagen=abrir_imagen.rgb_scale(argv[1])
        alto=len(imagen)
        ancho=len(imagen[0])
        new_image=to_grayscale(imagen)
        frecuencias=histogram(new_image)
        print frecuencias
        threshold=otsu_t2(frecuencias, alto*ancho)
        binarized_image=binarize(threshold,new_image)
        plt.imshow(binarized_image,cmap = cm.Greys_r)
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.savefig(argv[2])
        plt.show()
    except:
        print "Indicate an image as parameter"
        
if __name__ == '__main__':
    main()
                                    
