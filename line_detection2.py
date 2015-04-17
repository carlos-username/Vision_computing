#!/usr/bin/python2
#import cv2
from edge_detection2 import *
from scipy import arange
r=0
pixeles=[]
#H=[]
fr={}
usados=[]
H=[]
selec={}
threshold=otsu_t2(frecuencias,longitud_magn) #Using otsu automatic threshold, based on: http://en.wikipedia.org/wiki/Otsu%27s_method
print threshold
imagen=rgb_scale(argv[1])
def freq(histog):
    freq={}
    for j in xrange(len(histog)):
        (angulo,rho)=histog[j]
        comb=(angulo,rho)
        if comb in freq:
            freq[comb]+=1
        else:
            freq[comb]=1
    return freq
                                            
for i in xrange(1,ancho-1): #Detecting edges by using previously calculated threshold
    for j in xrange(1,alto-1):
        if histo[r][0]>threshold:
            img[i][j]=255
            pixeles.append((i,j))
            if histo[r][1] in fr: #Grouping by angles
                fr[histo[r][1]].append((i,j))
            else:
                fr[histo[r][1]]=[(i,j)]
        else:
            img[i][j]=0

        r+=1
sal=freq(H)
alto=len(imagen)
ancho=len(imagen[0])
#threshold_long=0
def frecuentes(histo, cantidad): 
    frec = []
    candidatos=[]
    for valor in histo:
        if valor is None:
            continue
        frecuencia = histo[valor]
        aceptar = False
        if len(frec) <= cantidad:
            aceptar = True
        if not aceptar:
            for (v, f) in frec:
                if frecuencia > f:
                    aceptar = True
                break
        if aceptar:
            frec.append((valor, frecuencia))
            frec = sorted(frec, key = lambda tupla: tupla[1])
            if len(frec) > cantidad:
                frec.pop(0)
    for valor in frec:
        candidatos.append(valor[0])
            
    return candidatos #getting candidates for a line
#arreglo_frec = frecuentes(sal, int(round(len(sal) * 100)))
            
def hough(angulo,elem,selec):
    #selec={}
    #if angulo != None:
    #H=[]
    H=[]
    for j in elem:
        while angulo < 0:
            angulo+=pi
        while angulo > pi:
            angulo-=pi
        rho=(j[1]-ancho/2)*cos(angulo)+(alto/2 - j[0])*sin(angulo) #get rho and switch coordinates to the center
        angle=int((180 * (angulo / pi)) / 18) #get angle
            #angle=int((180 * (angulo / pi)) / 18) #get angle
        #rho=(j[1])*cos(angulo)+(j[0])*sin(angulo) #get rho and switch coordinates to the center
        H.append((angle,rho))
        selec[angle,rho]=(j[0],j[1])
  
    return H

def funcion(componentes,T):
    for m in componentes:
        selec={}
        #print "Grupo"
        angulo=m[1]
        cont=[]
        for i in xrange(len(componentes[m])):
            #if len(componentes[m][i])>=T:
            for n in xrange(len(componentes[m][i])):
                cont.append(componentes[m][i][n])
        if angulo:
            if len(cont)>threshold_long:
                sal=freq(hough(angulo,cont,selec))
                
                arreglo_frec = frecuentes(sal, int(round(len(sal) * 10)))
            
                color=(randint(50,150),randint(100,200),randint(100,200)) 
                
                line=[]
                for b in arreglo_frec: # getting to color the candidates that are within the groups of angles
                    if selec.has_key(b):
                        imagen[selec[b][0]][selec[b][1]]=color
                        line.append((selec[b][0],selec[b][1]))
        if not angulo:
            for y in xrange(alto):
                print selec[angulo]
                if (y,selec[angulo][1]) in cont:
                    imagen[y][selec[angulo][1]]=color
                      
                            # distance=[]
            # for cr in comp:
            #     if cr[1]!=line[0][1] and cr[0]!=line[0][0]:
            #         dist=math.sqrt(pow(comp[0][0]-cr[0],2)+pow(comp[0][1]-cr[1],2))
            #         distance.append((cr[0],cr[1],dist))
            #     print "dis: ",distance
            #     if len(distance)>=1:
            #         p2=max(distance,key=lambda item:item[2])
            #         p1=min(distance,key=lambda item:item[2])
            #         print "g_d: ",p2
            #         print "g_min: ",p1
            #         if p2[1]-p1[1]>0:
            #             m1=1.0*(p2[0]-p1[0])/(p2[1]-p1[1])
            #             for x in xrange(ancho):
            #                 y=int(m1*(x-p1[1])+p1[0])
            #                 if y>=0 and y<alto:
            #                     imagen[y][x]=color
            

                 
def Conex(elemento):
    global threshold_long
    conta=1
    Objetos_por_grupo={}
    longitudes=[]
    for i in elemento:
        elementos=elemento[i]
        conta2=0
        Objetos_por_grupo[(conta,i)]=[]
        while len(elementos)>0:
            inicio=choice(elementos)
            recorrido1=imagendfs(imagen,inicio,elementos,3)
            longitudes.append(len(recorrido1))
            #print "Elemento: ", recorrido1
            for r in recorrido1:
                if r in elementos:
                    elementos.remove((r[0],r[1])) #remove previously discovered figures
            Objetos_por_grupo[(conta,i)].append(recorrido1)
            conta2+=1
        print "Grupo: ",conta, "con", conta2
        conta+=1
    print "longitudes: ",longitudes
    freq=frecuencia1(longitudes)
    threshold_long=otsu_t2(freq,len(longitudes)) #Using otsu automatic threshold, based on: http://en.wikipedia.org/wiki/Otsu%27s_method
    print "threshold_longitudes: ",threshold_long
    return Objetos_por_grupo
        #Objetos_por_grupo[1]
        
obj=Conex(fr)
funcion(obj,threshold_long)
plt.imshow(imagen,cmap = cm.Greys_r) #Drawing modified image
plt.show()

            # angulo=histo[r][1]
            # if angulo in fr:
            #     if angulo != None: #keep angle within 0 and 180
            #         while angulo < 0:
            #             angulo+=pi
            #         while angulo > pi:
            #             angulo-=pi
            #         rho=(j-alto/2)*cos(angulo)+(ancho/2 - i)*sin(angulo) #get rho and switch coordinates to the center
            #         angle=int((180 * (angulo / pi)) / 18) #get angle
            #         #rho=(j)*cos(angulo)+(i)*sin(angulo) #get rho and switch coordinates to the center
            #         #angle=int((180 * (angulo / pi)) / 18) #get angle
            #         H.append((histo[r][0],angle,rho)) 
            #         selec[angle,rho]=(i,j)
            #     else:
            #         selec[None,None]=(i,j)

# def frecuentes(histo, cantidad): #mainly based on Dra. elisa's algorithm to accept or revoke lines according to the votes: http://elisa.dyndns-web.com/teaching/comp/vision/2015.html
#     frec = []
#     candidatos=[]
#     for valor in histo:
#         if valor is None:
#             continue
#         frecuencia = histo[valor]
#         aceptar = False
#         if len(frec) <= cantidad:
#             aceptar = True
#         if not aceptar:
#             for (v, f) in frec:
#                 if frecuencia > f:
#                     aceptar = True
#                     break
#         if aceptar:
#             frec.append((valor, frecuencia))
#             frec = sorted(frec, key = lambda tupla: tupla[1])
#             if len(frec) > cantidad:
#                 frec.pop(0)
#     candidatos = []
#     for valor in frec:
#         print valor[0]
#         candidatos.append(valor[0])
    
#     return candidatos #getting candidates for a line
# arreglo_frec = frecuentes(sal, int(round(len(sal) * 1000)))


# imagen=rgb_scale(argv[1])
# ancho=len(imagen[0])
# alto=len(imagen)
# color=(randint(50,150),randint(100,200),randint(100,200))
# coord=[]
# for gh in fr: #grouping coordenates present within the groups previously formed
#     for p in fr[gh]:
#         coord.append(p)
# print "cord: ",coord
# for j in arreglo_frec: # getting to color the candidates that are within the groups of angles
#     if selec.has_key(j) and selec[j] in coord:
#         #if j[0]==0:
#         #    angle=0.1
#         #    y=(-math.cos(angle)/math.sin(angle))*(conta)+(j[1]/math.sin(angle))
#         imagen[selec[j][0]][selec[j][1]]=color

# #def dibujar():
# #    for y in xrange(alto):
# #        for x in xrange(ancho):
# #            if selec(
     
