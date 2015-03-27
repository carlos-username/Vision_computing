#!/usr/bin/python2
import math
import cv2
def caja_envolvente(figura,imagen):
    puntos={"Xmax":(0,0),"Xmin":(0,0),"Ymax":(0,0),"Ymin":(0,0)}
    puntos["Xmax"]=max(figura,key=lambda item:item[0])
    puntos["Xmin"]=min(figura,key=lambda item:item[0])
    puntos["Ymax"]=max(figura,key=lambda item:item[1])
    puntos["Ymin"]=min(figura,key=lambda item:item[1])
    
    print puntos
    #for r in puntos:
    #    imagen[puntos[r][0]][puntos[r][1]]=(255,255,0)
    picos=[]
    #picos.append((puntos["Ymin"][0],puntos["Xmin"][1]))
    
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmin"][0]][q]=(51,255,51)
    picos.append((puntos["Xmin"][0],q))
   
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymin"][1]]=(51,255,51)
    picos.append((q,puntos["Ymin"][1]))
    picos.append((puntos["Xmin"][0],puntos["Ymin"][1]))
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmax"][0]][q]=(51,255,51)
    picos.append((puntos["Xmax"][0],q))
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymax"][1]]=(51,255,51)
    #picos.append((q,puntos["Ymax"][1]))
   
    #distx=math.sqrt(pow(puntos["Xmax"][0]-puntos["Xmin"][0],2)+pow(puntos["Xmax"][1]-puntos["Xmin"][1],2))/2
    #disty=math.sqrt(pow(puntos["Ymax"][1]-puntos["Ymin"][1],2)+pow(puntos["Ymax"][0]-puntos["Ymin"][0],2))/2
    #imagen[puntos["Xmin"][0]+distx][puntos["Ymin"][1]+disty]=(0,0,0)
    return picos

def centro_masa(imagen,figura):
    ancho_im=len(imagen)
    alto_im=len(imagen[0])
    num_pix=len(figura)
    sumax=[i[0] for i in figura]
    promx=sum(sumax)/len(figura)
    sumay=[i[1] for i in figura]
    promy=sum(sumay)/len(figura)
    imagen[promx][promy]=(0,0,0)
    porciento_figura=num_pix*100.0/(ancho_im*alto_im)
    print "Porciento: ",porciento_figura
    return (promx,promy)
