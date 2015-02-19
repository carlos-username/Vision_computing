#!/usr/bin/python2
from random import randint
def vecinos(posX,posY,imagen):
    axis=[]
    for fila in xrange(posX-1,posX+2):
        for columna in xrange(posY-1,posY+2):
            if fila<len(imagen) and columna<len(imagen[0]) and fila>=0 and columna>=0 and (fila != posX or columna != posY):
                axis.append((fila,columna))

    return axis


def imagendfs(imagen,coord,figura):
    print "coord: ",coord
    visitados=[]
    pila=[coord]
    nodo=coord
    while pila!=[]:
        nodo=pila.pop()
        if (nodo[0],nodo[1]) not in visitados:
            visitados.append(nodo)
            vec=vecinos(nodo[0],nodo[1],imagen)
            for n in vec:
                for j in visitados:
                    if n != j:
                        if (n[0],n[1]) not in pila and (n[0],n[1]) in figura: 
                                pila.append(n)
           # print visitados
    #print "visitados_final->\n",visitados
    #print len(visitados)
    return visitados

