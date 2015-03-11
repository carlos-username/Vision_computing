#!/usr/bin/python2
from random import randint
def vecinos(posX,posY,imagen):
    axis=[]
    for fila in xrange(posX-1,posX+2):
        for columna in xrange(posY-1,posY+2):
            if fila<len(imagen) and columna<len(imagen[0]) and fila>=0 and columna>=0 and (fila != posX or columna != posY):
                axis.append((fila,columna))

    return axis


def imagendfs(imagen,coord,figura,correr):
    #print "coord: ",coord
    color1=(50,100,100)
    color2=(51,255,51)
    visitados=[]
    pila=[coord]
    nodo=coord
    while pila!=[]:
        nodo=pila.pop()
        if nodo not in visitados:
            visitados.append(nodo)
            vec=vecinos(nodo[0],nodo[1],imagen)
            for n in vec:
                if n not in visitados and n not in pila:
                    if correr==True:
                        if n not in figura: 
                            pila.append(n)
                    elif correr==False:
                        if tuple(imagen[n[0]][n[1]])!=color1 and tuple(imagen[n[0]][n[1]])!=color2:
                            pila.append(n)
                    if correr==3:
                        if n in figura:
                            pila.append(n)
    return visitados

