#!/usr/bin/python2
#import cv2
from edge_detection2 import *
r=0
pixeles=[]
#H=[]
fr={}
usados=[]
H=[]
selec={}
threshold=otsu_t2(frecuencias,img) #Using otsu automatic threshold, based on: http://en.wikipedia.org/wiki/Otsu%27s_method
print threshold

def freq(histog):
    freq={}
    for j in xrange(len(histog)):
        (magnitud, angulo,rho)=histog[j]
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
            #if histo[r][1] in fr: #Grouping by angles
            #    fr[histo[r][1]].append((i,j))
            #else:
            #    fr[histo[r][1]]=[(i,j)]
            angulo=histo[r][1]
            if angulo != None: #keep angle within 0 and 180
                while angulo < 0:
                    angulo+=pi
                while angulo > pi:
                    angulo-=pi
                rho=(j-alto/2)*cos(angulo)+(ancho/2 - i)*sin(angulo) #get rho and switch coordinates to the center
                angle=int((180 * (angulo / pi)) / 18) #get angle
                H.append((histo[r][0],angle,rho)) 
                selec[angle,rho]=(i,j)
                
                # if angle in fr:
                #     fr[angle].append((i,j))
                # else:
                #     fr[angle]=[(i,j)]
        else:
            img[i][j]=0

        r+=1
sal=freq(H)
def frecuentes(histo, cantidad): #mainly based on Dra. elisa's algorithm to accept or revoke lines according to the votes: http://elisa.dyndns-web.com/teaching/comp/vision/2015.html
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
    candidatos = []
    for valor in frec:
        print valor[0]
        candidatos.append(valor[0])
    
    return candidatos #getting candidates for a line
arreglo_frec = frecuentes(sal, int(round(len(sal) * 10)))

def Conex(elemento):
    #global threshold_long
    conta=1
    Objetos_por_grupo={}
    #longitudes=[]
    for i in elemento:
        elementos=elemento[i]
        conta2=0
        Objetos_por_grupo[(conta,i)]=[]
        while len(elementos)>0:
            inicio=choice(elementos)
            recorrido1=imagendfs(imagen,inicio,elementos,3)
            for r in recorrido1:
                if r in elementos:
                    elementos.remove((r[0],r[1])) #remove previously discovered figures
            Objetos_por_grupo[(conta,i)].append(recorrido1)
            conta2+=1
        print "Grupo: ",conta, "con", conta2
        conta+=1
    #print "longitudes: ",longitudes
    #freq=frecuencia1(longitudes)
    #threshold_long=otsu_t2(freq,len(longitudes)) #Using otsu automatic threshold, based on: http://en.wikipedia.org/wiki/Otsu%27s_method                                                      
    #print "threshold_longitudes: ",threshold_long
    return Objetos_por_grupo
obj=Conex(fr)

imagen=rgb_scale(argv[1])
for j in arreglo_frec:
    if selec.has_key(j):
        if j[0] in fr:
            fr[angle].append((i,j))
        else:
            fr[angle]=[(i,j)]
            
          #  for g in xrange(len(fr[j[0]])):
           #     if (g,selec[j][1]) in fr[j[0]]:
            #        imagen[g][selec[j][1]]=colores[j[0]]
                                        
        
plt.imshow(imagen,cmap = cm.Greys_r) #Drawing modified image
plt.show()
     
