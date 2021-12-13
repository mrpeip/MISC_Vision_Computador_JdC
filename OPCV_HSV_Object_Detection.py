import cv2 as cv
import numpy as np
"""
Este programa muestra como aplicar una máscara por color usando el formato de color HSV (Hue, Saturacion, Brillo)
, ya que este formato permite modificar más parámetros que el BGR. Para ello se carga una imagen de entrenamiento y
posteriormente un video. Para configurar los rangos de Hue Saturacion y Brillo de la máscara, se crear varias trackbars
que permiten modificarlos hasta obtener un valor óptimo.
"""

def nothing(x):
    pass

#Genero una clase de captura de video, para grabar un video con la webcam
vcap = cv.VideoCapture(0)

#Creo la ventana desde donde
cv.namedWindow('Tracking')
cv.createTrackbar('Lower_Hue','Tracking',0,255,nothing)
cv.createTrackbar('Lower_Sat','Tracking',0,255,nothing)
cv.createTrackbar('Lower_Value','Tracking',0,255,nothing)

cv.createTrackbar('Upper_Hue','Tracking',255,255,nothing)
cv.createTrackbar('Upper_Sat','Tracking',255,255,nothing)
cv.createTrackbar('Upper_Value','Tracking',255,255,nothing)
while True:
    #Esta imagen es de un training set sencillo que muestra claro este tipo de deteccion
    #frame = cv.imread('Image&Video/smarties.png')

    #Esta es una manera de capturar el video de la webcam
    _,frame = vcap.read()
    #Comenzamos pasando la imagen de BGR a HSV
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    #Sacamos los valores de cada traackbar
    lower_hue = cv.getTrackbarPos('Lower_Hue','Tracking')
    lower_sat = cv.getTrackbarPos('Lower_Sat', 'Tracking')
    lower_val = cv.getTrackbarPos('Lower_Value', 'Tracking')

    upper_hue = cv.getTrackbarPos('Upper_Hue', 'Tracking')
    upper_sat = cv.getTrackbarPos('Upper_Sat', 'Tracking')
    upper_val = cv.getTrackbarPos('Upper_Value', 'Tracking')

    #Ahora definimos el umbral inferior y superior de la máscara (lo que va a dejar ver)
    #Seleccionamos el valor HSV más bajo
    lower_b = np.array([lower_hue,lower_sat,lower_val])
    #Seleccionamos el valor HSV más alto
    upper_b = np.array([upper_hue,upper_sat,upper_val])

    #Definimos la máscara como el rango de valores HSV que se encuentre dentro del rango de umbrales
    mask = cv.inRange(hsv, lower_b, upper_b)
    #Aplicamos la máscara a la imagen con una operación bitwise AND sobre la propia imagen
    res = cv.bitwise_and(frame, frame, mask=mask)
    cv.imshow('mask',mask)
    cv.imshow('res',res)
    cv.imshow('frame',frame)

    key = cv.waitKey(1)
    if key == 27:
        break
vcap.release()
cv.destroyAllWindows()