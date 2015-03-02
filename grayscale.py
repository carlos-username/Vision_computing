#!/usr/bin/python2

#from abrir_imagen import *
from sys import argv
import matplotlib.pyplot as plt
#import numpy as np
#import matplotlib.cm as cm
#img=rgb_scale(argv[1])
from medias import *
def luminosity_cof(r,g,b): #luminosity coefficients
    return r*0.2126 + 0.7152*g + 0.0722*b

def suma(rgb):
    return sum(rgb)

def to_grayscale(img):
    ancho=len(img)
    alto=len(img[0])
    img2=[[0]*alto for j in xrange(ancho)]
    for i in xrange(ancho):
        for j in xrange(alto):
            img2[i][j]=luminosity_cof(img[i][j][0],img[i][j][1],img[i][j][2])
    return img2


def histogram(imagen):
    Diccionario_colores={}
    Array_col=[]
    #histo=[]
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            suma=imagen[i][j]
            Array_col.append(imagen[i][j])
            if suma in Array_col:
                if suma in Diccionario_colores:
                    Diccionario_colores[imagen[i][j]]+=1
                else:
                    Diccionario_colores[imagen[i][j]]=1
 
    return Diccionario_colores

def histogram2(imagen):
    histo=[0 for i in xrange(256)]
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            h=0xFF & imagen[i][j]
            histo[h]+=1
    return histo

def otsu_t(hist,imagen):
    total=len(imagen)*len(imagen[0])
    no_of_bins = len( hist ) # should be 256

    sum_total = 0.0
    for x in range( no_of_bins ):
        if not hist[x]:
            continue
        else:
            sum_total += x * hist[x]

    weight_background   = 0.0
    weight_foreground   = 0.0
    sum_background   = 0.0
    vmax=-1
    #inter_class_variances = []
    t=0
    for threshold in xrange(no_of_bins):
        # background weight will be incremented, while foreground's will be reduced
        if hist[threshold]:
            weight_background += hist[threshold]
            if weight_background == 0 :
                continue

            weight_foreground = total - weight_background
            if weight_foreground == 0 :
                break

            sum_background += threshold * hist[threshold]
            mean_background = sum_background / weight_background
            mean_foreground = (sum_total - sum_background) / weight_foreground

            varb=weight_background * weight_foreground * pow(mean_background - mean_foreground,2)
            if varb>=vmax:
                vmax=varb
                t=threshold
    return t

def otsu_t2(hist,imagen):
    total=len(imagen)*len(imagen[0])
    no_of_bins = len( hist ) # should be 256

    sum_total = 0
    for x in hist:
        sum_total += x * hist[x]

    weight_background   = 0.0
    weight_foreground   = 0.0
    sum_background   = 0.0
    vmax=-1
    #inter_class_variances = []
    t=0
    for threshold in hist:
        # background weight will be incremented, while foreground's will be reduced
        weight_background += hist[threshold]
        if weight_background == 0 :
            continue

        weight_foreground = total - weight_background
        if weight_foreground == 0 :
            break

        sum_background += threshold * hist[threshold]
        mean_background = sum_background / weight_background
        mean_foreground = (sum_total - sum_background) / weight_foreground

        varb=weight_background * weight_foreground * pow(mean_background - mean_foreground,2)
        if varb>vmax:
            vmax=varb
            t=threshold
            
    return t

def binarize(threshold,imagen):
    
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            if imagen[i][j]>=threshold:
                imagen[i][j]=255
            else:
                imagen[i][j]=0
    #imagen2=median(imagen)
    return imagen
