#!/usr/bin/python2

import Tkinter, tkFileDialog, cv2
import matplotlib.pyplot as plt
import numpy as np
from random import choice
window = Tkinter.Tk()

def abrir_dialogo(): 
    path = tkFileDialog.askopenfilename()
    imag = cv2.imread(path)
    img=cv2.cvtColor(imag, cv2.COLOR_BGR2RGB)
    #img[:,:,2] = 0
    #imagen(img)
    new_r=recorrido_frec(img)
    plt.imshow(new_r)
    plt.show()

      #plt.imshow(imagen)
def recorrido_frec(imagen):
    print "ancho: ",len(imagen)
    print "alto: ",len(imagen[0])
    Array_col=[]
    Diccionario_colores={}
    for i in xrange(len(imagen)):
        for j in xrange(len(imagen[0])):
            suma=sum(imagen[i][j])
            Array_col.append(suma)
            if suma in Array_col:
                if suma in Diccionario_colores:
                    Diccionario_colores[suma]+=1
                else:
                    Diccionario_colores[suma]=1
                    #print Diccionario_colores[suma]
    mayor=-1
    for b in Diccionario_colores:
        if Diccionario_colores[b]>mayor:
            mayor=Diccionario_colores[b]
            valor=b
    figura=[]
    print "mayor: ",mayor
    print "valor: ",valor
    puntos={"Xmax":(-1,0),"Xmin":(valor,0),"Ymax":(0,-1),"Ymin":(0,valor)}
    
    for x in xrange(len(imagen)):
        for c in xrange(len(imagen[0])):
            suma=sum(imagen[x][c])
            if suma != valor:
                if x>puntos["Xmax"][0]:
                    puntos["Xmax"]=(x,c)
                if c>puntos["Ymax"][1]:
                    puntos["Ymax"]=(x,c)
                if c<puntos["Ymin"][1]:
                    puntos["Ymin"]=(x,c)
                if x<puntos["Xmin"][0]:
                    puntos["Xmin"]=(x,c)
                figura.append((x,c))
   # x_r=puntos["Xmax"][0]-puntos["Xmin"][0]
    #y_r=puntos["Ymax"][1]-puntos["Ymin"][1]
    print puntos
    for r in puntos:
        imagen[puntos[r][0]][puntos[r][1]]=(255,51,51)
    #r=0
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymin"][1]]=(51,255,51)
  
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmin"][0]][q]=(51,255,51)
    
    for q in xrange(puntos["Xmin"][0],puntos["Xmax"][0]):
        imagen[q][puntos["Ymax"][1]]=(51,255,51)
        
    for q in xrange(puntos["Ymin"][1],puntos["Ymax"][1]):
        imagen[puntos["Xmax"][0]][q]=(51,255,51)
        
        #r+=1
    #print puntos
    #print len(figura)
    #corden=choice(figura)
    #imagendfs(imagen,corden,figura)
    return imagen

def imagendfs(imagen,cordn,figura):
    visitados=[]
    start1=cordn[0] #randint(0,len(imagen))
    start2=cordn[1] #randint(0,len(imagen[0]))
    pila=[(start1,start2)]
    #pila1=[(start1,start2)]
    while pila!=[]:
        nodo=pila.pop()    
        if (nodo[0],nodo[1]) not in visitados: # and (nodo[0],nodo[1]) in figura:
            mayor=-1
            visitados.append(nodo)
            vec=vecinos(nodo[0],nodo[1])
            for n in vec:
                for j in visitados:
                    if n != j:
                        if (n[0],n[1]) in figura and (n[0],n[1]) not in pila:
                            if n[0]>mayor:
                                mayor=n[0]
                                y=n[1]
            pila.append((mayor,y))
            print nodo,"->",imagen[nodo[0]][nodo[1]],"->",sum(imagen[nodo[0]][nodo[1]])
            print "vis->",visitados
            print "longitud->",len(visitados)
    print "Xmax->",mayor
    print len(visitados)
    #return visitados
  #  print "i->",i
  #      for i in xrange(len(imagen)):
  #          for j in xrange(len(imagen[0])):
   #             print i,",",j,",",imagen[i][j]
   #             print "vec->",sorted(vecinos(i,j,imagen))
            
def vecinos(posX,posY):
    #print "pos actuales->",posX,posY
    #vecinos=[]
    axis=[]
    #sum_pixels=[]
    for fila in xrange(posX-1,posX+2):
        for columna in xrange(posY-1,posY+2):
            #if fila<Xmax and columna<Ymax and fila>=0 and columna>=0 and (fila != posX or columna != posY):
            if fila>=0 and columna>=0 and (fila != posX or columna != posY):
                axis.append((fila,columna))
                #print fila,columna
                #print fila,columna,arreglo[fila][columna]
                #vecinos.append(arreglo[fila][columna])
                
                #sum_pixels()
                #print arreglo[fila][columna]
                #sum(arreglo[fila][columna]))
    return axis
B = Tkinter.Button(window, text ="imagen", command = abrir_dialogo)
B.pack()

window.mainloop()

