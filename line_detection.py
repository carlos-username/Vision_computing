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
            if histo[r][1] in fr: #Grouping by angles
                fr[histo[r][1]].append((i,j))
            else:
                fr[histo[r][1]]=[(i,j)]
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
arreglo_frec = frecuentes(sal, int(round(len(sal) * 0.7))) 

imagen=rgb_scale(argv[1])
color=(randint(50,150),randint(100,200),randint(100,200))
coord=[]
for gh in fr: #grouping coordenates present within the groups previously formed
    for p in fr[gh]:
        coord.append(p)
print "cord: ",coord
for j in arreglo_frec: # getting to color the candidates that are within the groups of angles
    if selec.has_key(j) and selec[j] in coord:
        imagen[selec[j][0]][selec[j][1]]=color
    
        
plt.imshow(imagen,cmap = cm.Greys_r) #Drawing modified image
plt.show()
     
