import cv2 as cv
import numpy as np
"""
Object tracking consiste en detectar y seguir un objeto en un video. Mean shift
"""
def clic(event,x,y,flags,params):
    if event == cv.EVENT_LBUTTONDOWN:
        xyval = str(x) + " " + str(y)
        #QUITAR QUE ESCRIBA TEXTO EN LA VERSION FINAL!!!!!
        #cv.putText(frame,xyval,(x,y),cv.FONT_HERSHEY_DUPLEX,1,(0,255,0),2)
        cv.imshow('test',frame)
        points.append((x,y))
#Cargo el video, voy a detectar y seguir un coche
vcap = cv.VideoCapture('traffic.mp4')
#Saco el primer frame del video
ret,frame = vcap.read()
#Calculo la posición inicial de la ventana
#1º Testeo la posición del primer frame, y miro a ver donde está con un mouse event:
cv.imshow('test',frame)
points = []
#HACER SOLO DOS CLICS!!!!!!
cv.setMouseCallback('test',clic)
cv.waitKey(0)
#Con los dos puntos extraidos del mouse event, creo la ROI y una trackwindow
print(points)
print(points[0][0])

#Recordar, cuando hago frame es: frame[yinicial:yfinal,xinicial:xfinal]
ROI = frame[points[0][1]:points[1][1],points[0][0]:points[1][0]]
#La trackwindow guarda la informacion: (x, y, height, width)
height, width, channels = ROI.shape
track_window = (points[0][0],points[0][1],width,height)
print(track_window)
cv.imshow('ROI',ROI)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Voy a hacer un histogram back projection, esto lo que hace es crear una imagen del mismo tamaño de la imagen original
(frame en este caso) pero con un solo canal donde cada pixel de esa nueva imagen corresponda a la probabilidad de que
ese pixel pertenezca al objeto que buscamos detectar (la ROI donde está el objeto sale con más blanco). Para hacer esto
se sigue los siguientes pasos:
"""
#Paso a HSV
HSV_ROI = cv.cvtColor(ROI,cv.COLOR_BGR2HSV)
#Defino la máscara (es como hacer object detection con HSV)
mask = cv.inRange(HSV_ROI,np.array((0.,60.,32.)),np.array((180.,255.,255.)))
#Defino el histograma (SOLO VAMOS A USAR EL CANAL DEL "HUE" DE HSV, QUE ES EL 0).
ROI_Hist = cv.calcHist([HSV_ROI],[0],mask,[180],[0,180])
#Normalizamos el histograma entre 0 y 255
cv.normalize(ROI_Hist,ROI_Hist,0,255,cv.NORM_MINMAX)
#Este histograma va a andar cambiando con cada frame
"""
Para aplicar mean shift debo tener en cuenta unas cuantas consideraciones:
1. Coger el primer frame del video
2. Definir la posición inicial de la ventana de interés del objeto a seguir

"""
#Defino los criterior de finalización del mean Shift, son un parámetro necesario de esa función
#Va a ser que avance un pixel o que hayan pasado 10 iteraciones
term_crit = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)
while True:
    ret,frame = vcap.read()
    if ret == True:
        #Paso la imagen a HSV, por lo del histograma de antes
        HSV_Frame = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        #Calculo la backprojection los parámetros on:
        """
        imagen = La imagen a tratar (cada frame) en forma de lista
        channel = El canal a utilizar. El "Hue" es 0 (HAY QUE USAR [])
        histogram = El histograma a utilizar, que es el calculado anteriormente
        range = El rango para el canal. En el caso del Hue de 0 a 180
        
        """
        dst = cv.calcBackProject([HSV_Frame],[0],ROI_Hist, [0,180],1)
        #Voy a aplicar mean shift
        ret,track_window = cv.meanShift(dst,track_window,term_crit)
        #Voy a dibujar un rectángulo sobre la imagen del coche que sigo
        x,y,w,h = track_window
        final_image = cv.rectangle(frame,(x,y),(x+w,y+h),255,4)
        #cv.imshow('Frame',frame)
        cv.imshow('Final', final_image)
        #cv.imshow('Back Projection', dst)
        key = cv.waitKey(0)
        if key == 'q':
            break
    else:
        break
vcap.release()
cv.destroyAllWindows()
