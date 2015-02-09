#!/usr/bin/python2
from sys import argv
import random
import math

class K_clustering:
    def __init__(self,clusters,iteraciones,objetos):
        self.iteracion=iteraciones
        self.clusters=clusters
        self.objetos=objetos
        self.num_carac=len(self.objetos[0]) 
        self.num_puntos=len(self.objetos) 
        self.pertenencias=[ [0]*self.num_puntos for n in xrange(self.clusters) ] #filas son los clusters,columnas son los puntos
        self.centroides=[ [0]*self.num_carac for i in xrange(self.clusters) ] #filas son los clusters, columnas son los caracteristicas de agrupacion
        self.distancias=[ [0]*self.num_puntos for k in xrange(self.clusters) ] #filas son los clusters, columnas son los puntos
        self.generacion_vectores()
        for i in xrange(self.iteracion): # se repite el proceso de acuerdo al numero de iteraciones
            print "Instrumentos: \n"
            self.imprimir(self.objetos)
            print "\nCentroides: \n"
            self.imprimir(self.centroides)
            self.calcular_distancias()
            self.pertenencia()
            print "\npertenencias: \n"
            self.imprimir(self.pertenencias)
            self.reubicacion()
            print "\nnuevos centroides\n"
            self.imprimir(self.centroides)
    def generacion_vectores(self):
        for i in xrange(self.clusters):
            for n in xrange(self.num_puntos):
                n=random.randint(0,self.num_puntos-1)
                for j in xrange(self.num_carac):
                    self.centroides[i][j]=self.objetos[n][j]
            
    def imprimir(self,arreglo):
        for i in arreglo:
            print i
           
    def calcular_distancias(self):
        for i in xrange(self.clusters): # por cada centroide
            for j in xrange(self.num_puntos): # por cada punto
                distancia=0
                for k in xrange(self.num_carac): # por cada caracteristica
                    distancia+=pow(self.objetos[j][k]-self.centroides[i][k],2) #calcula las distancias
                self.distancias[i][j]=math.sqrt(distancia) # guarda en vector de distancias por cada distancia de cada punto
                
        print "\ndistancias:\n"
        #r=0
        #for m in self.distancias:
        #    print "c",r,"=", m
        #    r+=1
        for i in xrange(0,self.clusters): # impresion invidual de las distancias de los puntos con los centroides
            for j in xrange(0,self.num_puntos):
                print "p",j,"c",i,"=%.4f" % self.distancias[i][j]
        
    def pertenencia(self): #subrutina para indicar que puntos se agrupan con que centroide
        self.distancia=zip(*self.distancias) # generar matriz transpuesta de distancias
        for i in xrange(self.num_puntos): 
            minimo = min(self.distancia[i]) # sacar la minima distancia por cada punto
            for x in xrange(self.clusters): 
                if self.distancia[i][x]==minimo: 
                    self.pertenencias[x][i]=1  # poner 1 en donde se encuentre el punto x, 0 en caso contrario
            
    def reubicacion(self):
        medias=[[] for i in xrange(self.clusters)] # vector para guardar las medias para los nuevos centroides
        for i in xrange(self.clusters):
            print "\n"
            print "En centroide",i,"se encuentran:" # indicar que puntos fueron agrupados con cada centroide
            print "\n"
            for x in xrange(self.num_puntos):
                if self.pertenencias[i][x]: # si el punto esta agrupado en el centroide x
                    medias[i].append(self.objetos[x]) #agregar al vector de medias
            transpuesta = zip(*medias[i]) # sacar la matriz transpuesta de las medias
            promedio = lambda items: float(sum(items)) / len(items) # proceso para calcular cada promedio
            #para los nuevos puntos a generar
            suma_p = map(promedio, transpuesta)
            print medias[i] # puntos agrupados en centroide x
            self.centroides[i]=suma_p # actualizacion de centroides
            
#def menor_distancias
# $1=numero de centroides
# $2=numero de instrumentos
# $3=numero de iteraciones
#K_clustering(int(argv[1]),int(argv[2]),int(argv[3])) # primer parametro se refiere al numero de centroides

#segundo parametro se refiere a cuantas iteraciones se desean 


