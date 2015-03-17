#!/usr/bin/python2

from edge_detection2 import *
from math import fabs
threshold=otsu_t2(frecuencias,len(img[0])*len(img[1]))
dibujo=rgb_scale(argv[1])
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
def ecuacion_circulo(centro,y,x): #get equation from circle
    r=math.sqrt((x-centro[1])**2+(y-centro[0])**2)
    return r

def votos_fig(figura,radio,xmax,ymax,xmin,ymin): #getting votes for the centers to be considered
    #print figura
    #global dibujo
    votos={}
    votos2={}
    for coord in figura:
        y=coord[0]
        x=coord[1]
        gx=Gx[y][x]
        gy=Gy[y][x]
        g = math.sqrt(pow(gx,2)+pow(gy,2))
        if math.fabs(g)>0:
            cosTheta = gx / g
            sinTheta = gy / g
            xc = int(round(x - radio * cosTheta))
            yc = int(round(y - radio * sinTheta))
            if xc>=xmin[1] and xc<xmax[1] and yc>=ymin[0] and yc<ymax[0]: #votes inside the bounding box
                dibujo[yc][xc]=(178,34,34) #Drawing votes within the image
                if (yc,xc) in votos:
                    votos[(yc,xc)]+=1
                    votos2[votos[(yc,xc)]]=votos[(yc,xc)]
                else:
                    votos[(yc,xc)]=1
                    votos2[votos[(yc,xc)]]=votos[(yc,xc)]
    threshold=otsu_t2(votos2,len(votos2)) #using Otsu threshold for votes
    print "threshold: ",threshold
    sumax=0
    sumay=0
    conta=0
    for m in votos:
        if votos[m]>=threshold:
            #dibujo[m[0]][m[1]]=(0,50,250)
            #nuevos.append(m)
            sumay+=m[0]
            sumax+=m[1]
            conta+=1
    promy=int(round(sumay/conta)) #Get average of x corresponding to selected votes
    promx=int(round(sumax/conta)) ##Get average of y corresponding to selected votes
    print "promx: ",promx
    print "promy: ",promy
    dibujo[promy][promx]=(0,50,250)
    return (promy,promx)

def detectar_formas(img2,pixeles):
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
        caja_envolvente(recorrido1,img2)
        for i in recorrido1:
            img2[i[0]][i[1]]=color
        centro=centro_masa(img2,recorrido1) #get mass center of shape
        x_mayor=max(borde,key=lambda item:item[1]) 
        y_mayor=max(borde,key=lambda item:item[0])
        x_menor=min(borde,key=lambda item:item[1])
        y_menor=min(borde,key=lambda item:item[0])
        radio1=x_mayor[1]-centro[1] #distance from greatest x to center of mass
        radio2=y_mayor[0]-centro[0] #distance from greatest y to center of mass
        radio3=centro[1]-x_menor[1] #distance from lowest x to center of mass
        radio4=centro[0]-y_menor[0] #distance from lowest x to center of mass
        radio=(radio1+radio2+radio3+radio4)/4 #Average of all radius respect to the center of mass
        print "radio: ",radio
        #radiox=radio2
        centro_nuevo=votos_fig(borde,radio,x_mayor,y_mayor,x_menor,y_menor)
        radio_nuevo=int(round(centro_nuevo[1]-x_menor[1]))
        #for y in xrange(y_menor[0],y_mayor[0]):
        #    for x in xrange(x_menor[1],x_mayor[1]):
        for y in xrange(len(dibujo)): #Drawing circle by checking by substituting points in the equation 
            for x in xrange(len(dibujo[0])):
                radioc=int(round(ecuacion_circulo(centro_nuevo,y,x)))
                if radioc==radio_nuevo: #if the radios obtained by the coordinates is equal to the one previously calculated.
                    dibujo[y][x]=(0,50,250) #then it draws the points
                
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

