#!/usr/bin/python2

from edge_detection import * #In edge_detection, a median filter is applied as well as grayscale is used.
def detectar_formas(img2):
    while len(pixeles)>0: #detect objets in image, until all coordenates corresponding to the borders are covered
        color=(randint(200,300),randint(200,300),randint(200,300)) 
        inicio=choice(pixeles)
        print "inicio: ",inicio
        print "pixeles: ",len(pixeles)
        recorrido1=imagendfs(img2,inicio,pixeles,2) #separate figures by dfs
        for i in recorrido1:
            if i in pixeles:
                pixeles.remove((i[0],i[1])) #remove previously discovered figures
        caja_envolvente(recorrido1,img2)
        recorrido2=imagendfs(img2,inicio,recorrido1,3) #discover all the coordenates within the figure to be later colored
        for i in recorrido2:
            img2[i[0]][i[1]]=color
        centro_masa(img2,recorrido2)
  
def main():
    inicio=(0,0)
    img2=rgb_scale(argv[1]) #get image in rgb
    recorrido=imagendfs(img2,inicio,pixeles,1)
    for i in recorrido:
        img2[i[0]][i[1]]=(50,100,100)
    detectar_formas(img2)
    plt.imshow(img2,cmap = cm.Greys_r) #Drawing modified image with detected shapes
    plt.show()

main()
