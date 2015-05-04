#!/usr/bin/python2

import numpy as np
import cv2
#from mftracker import *
#from PIL import *
#from SimpleCV import *
from sys import argv
#global counter
#global cc
def bounding_boxes(frame,contours,y_linea,x_linea):
    counter=0
    counter_carro=0
    counter_moto=0
    counter_camion=0
            
    for contour in contours:
        (x,y,w,h) = cv2.boundingRect(contour)
        if w > 10 and h > 15: #restricting bounding boxes to at least some h and w
            M = cv2.moments(contour)
            c_x = int(M['m10']/M['m00']) #getting coordinates for mass center
            c_y = int(M['m01']/M['m00'])
            area=M["m00"] #filtering kinds of cars by area
            diff=c_y-y_linea
            if diff>=0 and diff<=8 and c_x<=x_linea and c_x>=x_linea//2: #right lane
                if area<=450:
                    counter_moto+=1
                if area>450 and area<=3000:
                    counter_carro+=1
                if area>3000:
                    counter_camion+=1
                counter+=1
            else:
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2) #Drawing bounding box
                cv2.circle(frame,(int(c_x),int(c_y)),1,(0,255,0),4)
            diff2=y_linea-c_y
            if diff<0 and diff2<=8 and c_x<=x_linea//2 and c_x>=0: #left lane
                if area<=450:
                    counter_moto+=1
                if area>450 and area<=3000:
                    counter_carro+=1
                if area>3000:
                    counter_camion+=1
                counter+=1
            else:
                cv2.putText(frame, str(area),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5, (255, 255, 255), 1, True) #drawing the area
                cv2.rectangle(frame, (x,y), (x+w,y+h), (255, 0, 0), 2)
                cv2.circle(frame,(int(c_x),int(c_y)),1,(0,255,0),4)
           
    return (counter,counter_moto, counter_carro,counter_camion)

def detect_lines(gray): #getting to detect lines for finding the area intended for analysis
    edges = cv2.Canny(gray,100,300) #canny edge detector
    lines = cv2.HoughLines(edges, 2, np.pi/180, 40)[0]
    lines1=[]
    for (rho, theta) in lines[:5]:
        # lines (only choose the 5 strongest ones)
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

def crop_area(framex): #get the area to be cropped
    framex=cv2.resize(framex,(900,400),interpolation = cv2.INTER_CUBIC) # using cubic interpolationx
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
            #preprocessing part
            frame = frame[:,horiz[0]:horiz[1]] # cropping image to area of highway
            frame2=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
            newf=cv2.GaussianBlur(frame2,(5,5),0)
            fgmask = fgbg.apply(newf,learningRate=0.005) #Learning rate for the adaptive background (the smaller it is, the faster the BG gets updated)
            new_frame=cv2.GaussianBlur(fgmask.copy(),(7,7),0) #Post-processing part
            new_frame2 = cv2.threshold(new_frame.copy(),127,255,cv2.THRESH_BINARY)[1] #threshold of 127 due to the fact that documentation says that extra shadowws around the foreground needs it
            new_frame=cv2.blur(new_frame2,(5,5)) #averaging filter to diminish noise
            alto=len(frame)
            ancho=len(frame[0])
            cv2.line(frame,(0,alto//2),(ancho,alto//2),(100,175,150),2)
            closing = cv2.morphologyEx(new_frame, cv2.MORPH_CLOSE, kernel,iterations=4) #using morphological operator (closing to close gaps)
            contours=cv2.findContours(closing,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
            valores=bounding_boxes(frame,contours,alto//2,ancho)
            counter2+=valores[0] #total counter
            counter_carro+=valores[2] #counter for cars
            counter_moto+=valores[1] #countrer for motorcycle
            counter_camion+=valores[3] #contour for heavy vehicles
            print "C: ",counter2
            cv2.putText(frame, str(counter2)+"->"+"Car:"+str(counter_carro)+"-> Moto:"+str(counter_moto)+"-> Truck:"+str(counter_camion),(0,150),cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 255, 150), 1, True)
            cv2.imshow("Background substraction", fgmask)
            cv2.imshow("Track", frame)
            cv2.imshow("background sub with processing", closing)
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
cap = cv2.VideoCapture(argv[1])

fgbg = cv2.BackgroundSubtractorMOG2()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) #creating structuring element for the closing operator
detection(cap,kernel)    
cap.release()
cv2.destroyAllWindows()
