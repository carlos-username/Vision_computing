#!/usr/bin/python2

import numpy as np
import cv2
#from mftracker import *
#from PIL import *
#from SimpleCV import *
from sys import argv
from sklearn.cluster import *
#global counter
#global cc
cc=[]
def bounding_boxes(frame,contours,y_linea,x_linea):
    counter=0
    #print contours
    #hull=[]
    counter_carro=0
    counter_moto=0
    counter_camion=0
            
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        #(x1,y1),radius = cv2.minEnclosingCircle(contour)
        #center = (int(x1),int(y1))
        #if radius>20:
        #    cv2.circle(frame,center,int(radius),(0,255,0),2)
        if w > 20 and h > 20:
            M = cv2.moments(contour)
            c_x = int(M['m10']/M['m00'])
            c_y = int(M['m01']/M['m00'])
            area=int(M["m00"])
            #porciento=int(area*100/(y_linea*2*x_linea))
            #print area
            #hs=cv2.convexHull(contour)
            #print hs
            #cv2.drawContours(frame,[hs],0,(0,0,255),2)
            #cc.append(area)
            diff=c_y-y_linea
            if diff>1 and diff<=10 and c_x<=x_linea and c_x>=0:
                if area<=1000:
                    #print #porciento
                    counter_moto+=1
                if area>1000 and area<=4800:
                    counter_carro+=1
                if area>5000:
                    counter_camion+=1
                counter+=1
                    #print "Counter: ",counter
            else:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
                cv2.circle(frame,(int(c_x),int(c_y)),1,(0,255,0),4)
    return (counter,counter_moto, counter_carro,counter_camion)

def detect_lines(gray):
    edges = cv2.Canny(gray,100,300)
    lines = cv2.HoughLines(edges, 2, np.pi/180, 40)[0]
    lines1=[]
    for (rho, theta) in lines[:5]:
        # blue for infinite lines (only draw the 5 strongest)
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        #y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        #y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        #y2 = int(y0 - 1000*(a))
        if x1 and x2:
            lines1.append((x1,x2))
        #cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
    x_m=min(lines1,key=lambda item:item[0])
    x_M=max(lines1,key=lambda item:item[1])
    #print lines1
    return (x_m[0]+80,x_M[1])

def crop_area(framex):
    framex=cv2.resize(framex,(900,400),interpolation = cv2.INTER_CUBIC)
    framex=cv2.cvtColor(framex,cv2.COLOR_RGB2GRAY)
    return detect_lines(framex)
  
def detection(capture,kernel):
    #capture.set(cv2.cv.CV_CAP_PROP_FPS, -20)
    frame1=capture.read()[1]
    horiz=crop_area(frame1)
    counter2=0
    counter_carro=0
    counter_moto=0
    counter_camion=0
    while True:
        #counter=0
        ret, frame = capture.read()
        if ret:
            frame=cv2.resize(frame,(900,400),interpolation = cv2.INTER_CUBIC)
            frame = frame[:,horiz[0]:horiz[1]]
            frame2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            newf=cv2.GaussianBlur(frame,(5,5),0)
            fgmask = fgbg.apply(newf,learningRate=0.005)
            new_frame=cv2.GaussianBlur(fgmask.copy(),(7,7),2)
            new_frame = cv2.threshold(new_frame.copy(),127,255,cv2.THRESH_BINARY)[1]
            alto=len(frame)
            ancho=len(frame[0])
            cv2.line(frame,(0,alto//2),(ancho,alto//2),(100,175,150),2)
            closing = cv2.morphologyEx(new_frame, cv2.MORPH_CLOSE, kernel,iterations=2)
            contours=cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
            valores=bounding_boxes(frame,contours,alto//2,ancho)
            counter2+=valores[0]
            counter_carro+=valores[2]
            counter_moto+=valores[1]
            counter_camion+=valores[3]
            print "C: ",counter2
            cv2.putText(frame, str(counter2)+"->"+"C:"+str(counter_carro)+"-> M:"+str(counter_moto)+"-> T:"+str(counter_camion),(0,150),cv2.FONT_HERSHEY_SIMPLEX,1, (255, 0, 0), 1, True)
            cv2.imshow("Background substraction", fgmask)
            cv2.imshow("Track", frame)
            cv2.imshow("background sub with processing", closing)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
cap = cv2.VideoCapture(argv[1])

fgbg = cv2.BackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
detection(cap,kernel)    
cap.release()
cv2.destroyAllWindows()
#frame=cv2.resize(frame,(width/2, height/2), interpolation = cv2.INTER_LINEAR)
#cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#height, width = frame.shape[:2]
            # image=new_frame.copy()
            # (h, w) = image.shape[:2]
            # image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
            # image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
            # image = image.reshape((image.shape[0] * image.shape[1], 3))
            # clt = MiniBatchKMeans(n_clusters = 2)
            # labels = clt.fit_predict(image)
            # quant = clt.cluster_centers_.astype("uint8")[labels]
            # quant = quant.reshape((h, w, 3))
            # image = image.reshape((h, w, 3))
            # quant = cv2.cvtColor(quant, cv2.COLOR_LAB2BGR)
            # image = cv2.cvtColor(image, cv2.COLOR_LAB2BGR)
            # image = cv2.cvtColor(np.hstack([image, quant]), cv2.COLOR_BGR2GRAY)
           
#simple_i=Image(fgmask.transpose(1,0,2)[:,:,::-1])
#simple_i=Image(fgmask, cv2image=True)
#blobs = simple_i.findBlobs()
#mftrack(frame)
#rect = cv2.minAreaRect(fgmask2)
#box = cv2.cv.BoxPoints(rect)
#box = np.int0(box)
#new=cv2.drawContours(im,[box],0,(0,0,255),2)
#cv2.imshow('frame',fgmask2)
        
