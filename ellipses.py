#!/usr/bin/python2

from edge_detection2 import *
from math import fabs
threshold=otsu_t2(frecuencias,len(img)*len(img[0]))
dibujo=rgb_scale(argv[1])
print "threshold_otsu: ",threshold
def acceder_bordes(imagen): #Separating gradient pixels
    alto=len(imagen)
    ancho=len(imagen[0])
    r=0
    pixeles=[]
    for y in xrange(1,alto-1): #Detecting edges by using previously calculated threshold
        for x in xrange(1,ancho-1):
            if histo[r][0]>threshold:
                pixeles.append((y,x))
            r+=1
    return pixeles

def tangent(yc,xc,ymin,ymax):
    #global img2
    gx=Gx[yc][xc]
    gy=Gy[yc][xc]
    angle=math.atan2(gy,gx)
    alpha=math.pi/2-angle #substract pi/2 or 90° from the gradient angle to get the tangent one
    if angle != 0 and alpha!=0:
        dx=cos(alpha) #Get y and x component of slope
        dy=sin(alpha)
        m=1.0*(dy/dx)
        for x1 in xrange(ancho):
            y2=int(round(m*(x1-xc)+yc))
            #y3=x1*math.acos(alpha)-y1*math.tan(alpha)
            if y2>=ymin[0]+5 and y2<ymax[0]+5:
                #print "y2",y2
                dibujo[y2][x1]=(0,255,0)
                #img2[y3][x1]=(0,0,0)
        return m #get the tangent slope
def equation(eq1,eq2,ymin,ymax):
    for x in xrange(ancho):
        y1=int(round(eq1[0]*(x-eq1[2])+eq1[1]))
        y2=int(round(eq2[0]*(x-eq2[2])+eq2[1]))
        if y1==y2:
            dibujo[y1][x]=(255,0,100) #if equations cross each other
            for q in xrange(ancho): #horizontal line
                dibujo[y1][q]=(255,0,0)
            for p in xrange(ymin[0],ymax[0]): #vertical line
                dibujo[p][eq1[2]]=(255,100,0)
            return
        
        
def detectar_formas(img2,pixeles):
    alto=len(img2)
    ancho=len(img2[0])
         
    while len(pixeles)>0: #detect objets in image, until all coordenates corresponding to the borders are covered
        borde=[]
        color=(randint(60,230),randint(110,210),randint(70,255))
        inicio=choice(pixeles)
        print "inicio: ",inicio
        print "pixeles: ",len(pixeles)
        recorrido1=imagendfs(img2,inicio,pixeles,False) #separate figures by dfs
        for i in recorrido1:
            if i in pixeles:
                pixeles.remove((i[0],i[1])) #remove previously discovered figures
                borde.append((i[0],i[1]))
        picos=caja_envolvente(recorrido1,img2)
        #for i in recorrido1:
        #    img2[i[0]][i[1]]=color
        #centro=centro_masa(img2,recorrido1) #get mass center of shape
        x_mayor=max(borde,key=lambda item:item[1]) 
        y_mayor=max(borde,key=lambda item:item[0])
        x_menor=min(borde,key=lambda item:item[1])
        y_menor=min(borde,key=lambda item:item[0])
        x_mayor=max(borde,key=lambda item:item[1])
        print "picos: ", picos
        for jk in picos:
            img2[jk[0]][jk[1]]=(255,200,0)
        m_c1=1.0*(picos[0][0]-picos[1][0])/(picos[0][1]-picos[1][1])
        print "m1: ",m_c1
        m_c2=1.0*(picos[2][0]-picos[3][0])/(picos[2][1]-picos[3][1])
        print "m2: ",m_c2
        #for y in xrange(y_menor[0],y_mayor[0]):
        candidatos=[]
        #eqt1=(0,0,0)
        #eqt2=(0,0,0)
        for x in xrange(x_menor[1],x_mayor[1]):
            equ1=int(round(m_c1*(x-picos[1][1])+picos[1][0]))
            equ2=int(round(m_c2*(x-picos[2][1])+picos[2][0]))
            if equ1>=0 and equ1<alto:
                if (equ1,x) in borde and (equ2,x) in borde:
                    slope=1.0*tangent(equ1,x,y_menor,y_mayor) #slope of equation
                    slope2=1.0*tangent(equ2,x,y_menor,y_mayor)
                    eqt1=(slope,equ1,x)
                    eqt2=(slope2,equ2,x)
                    point=equation(eqt1,eqt2,y_menor,y_mayor) #find the point where the two lines intersect

                                                                                                                                                    
def fondo(image):
    pixeles=acceder_bordes(dibujo)
    inicio=(0,0)
    img2=image
    #img2=rgb_scale(image) #get image in rgb
    recorrido=imagendfs(image,inicio,pixeles,True)
    for i in recorrido:
        img2[i[0]][i[1]]=(50,100,100)
    detectar_formas(img2,pixeles)
fondo(dibujo)
plt.imshow(dibujo,cmap = cm.Greys_r) #Drawing modified image with detected shapes
plt.show()
        
#threshold_circles=otsu_t2(votes,len(votes))
#print len(votes)

