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
    counter_carro=0
    counter_moto=0
    counter_camion=0
            
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if w > 20 and h > 20:
            M = cv2.moments(contour)
            c_x = int(M['m10']/M['m00'])
            c_y = int(M['m01']/M['m00'])
            area=int(M["m00"])
            diff=c_y-y_linea
            if diff>1 and diff<=10 and c_x<=x_linea and c_x>=0: #area threshold to classify
                if area<=1000:
                    counter_moto+=1
                if area>1000 and area<=4800:
                    counter_carro+=1
                if area>5000:
                    counter_camion+=1
                counter+=1
            else:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
                cv2.circle(frame,(int(c_x),int(c_y)),1,(0,255,0),4)
    return (counter,counter_moto, counter_carro,counter_camion)

def detect_lines(gray):
    edges = cv2.Canny(gray,100,300)
    lines = cv2.HoughLines(edges, 2, np.pi/180, 40)[0]
    lines1=[]
    for (rho, theta) in lines[:5]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        x1 = int(x0 + 1000*(-b))
        x2 = int(x0 - 1000*(-b))
        if x1 and x2:
            lines1.append((x1,x2))
    x_m=min(lines1,key=lambda item:item[0])
    x_M=max(lines1,key=lambda item:item[1])
    return (x_m[0]+80,x_M[1])

def crop_area(framex):
    framex=cv2.resize(framex,(900,400),interpolation = cv2.INTER_CUBIC)
    framex=cv2.cvtColor(framex,cv2.COLOR_RGB2GRAY)
    return detect_lines(framex)
  
def detection(capture,kernel):
    frame1=capture.read()[1]
    horiz=crop_area(frame1) #cropping image area
    counter2=0
    counter_carro=0
    counter_moto=0
    counter_camion=0
    while True:
        #counter=0
        ret, frame = capture.read()
        if ret:
            frame=cv2.resize(frame,(900,400),interpolation = cv2.INTER_CUBIC) #resizing with linear interpolation
            frame = frame[:,horiz[0]:horiz[1]]
            frame2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY) 
            newf=cv2.GaussianBlur(frame,(5,5),0)
            fgmask = fgbg.apply(newf,learningRate=0.005) #using a learning rate of 0.005
            new_frame=cv2.GaussianBlur(fgmask.copy(),(7,7),2) #applying gausian filter to post-processing
            new_frame = cv2.threshold(new_frame.copy(),127,255,cv2.THRESH_BINARY)[1] #postprocesing
            alto=len(frame)
            ancho=len(frame[0])
            cv2.line(frame,(0,alto//2),(ancho,alto//2),(100,175,150),2)
            closing = cv2.morphologyEx(new_frame, cv2.MORPH_CLOSE, kernel,iterations=2) #two iterations for closing operation
            contours=cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0] #getting contours
            valores=bounding_boxes(frame,contours,alto//2,ancho) #getting bounding boxes
            counter2+=valores[0] #getting counting values
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
