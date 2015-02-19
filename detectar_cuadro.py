#!/usr/bin/python2

def caja_envolvente(figura,imagen):
    puntos={"Xmax":(0,0),"Xmin":(0,0),"Ymax":(0,0),"Ymin":(0,0)}
    puntos["Xmax"]=max(figura,key=lambda item:item[0])
    puntos["Xmin"]=min(figura,key=lambda item:item[0])
    puntos["Ymax"]=max(figura,key=lambda item:item[1])
    puntos["Ymin"]=min(figura,key=lambda item:item[1])
    # for c in figura:
    #     if c[0]>puntos["Xmax"][0]:
    #         puntos["Xmax"]=(c[0],c[1])
    #     if c[1]>puntos["Ymax"][1]:
    #         puntos["Ymax"]=(c[0],c[1])
    #     if c[1]<puntos["Ymin"][1]:
    #         puntos["Ymin"]=(c[0],c[1])
    #     if c[0]<puntos["Xmin"][0]:
    #         puntos["Xmin"]=(c[0],c[1])
    
    print puntos
    for r in puntos:
        imagen[puntos[r][0]][puntos[r][1]]=(255,51,51)
        
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymin"][1]]=(51,255,51)
        
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmin"][0]][q]=(51,255,51)
        
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymax"][1]]=(51,255,51)
        
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmax"][0]][q]=(51,255,51)
                                                                                                                                                                                                                   
