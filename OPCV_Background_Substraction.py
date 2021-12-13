import cv2 as cv
import numpy as np
"""
Mediante extracción de fondos puedo sacar la máscara del froreground de una imagen, también conocida como la imagen
binaria que contiene los píxeles que pertenecen a un objeto en movimiento de una imagen cuando la cámara está
estática. Es util por ejemplo para detectar y contar coches desde una cámara de tráfico, o personas.
"""
#Cargo el video con el que vamos a trabajar
vcap = cv.VideoCapture('vtest.avi')
#Voy a crear la clase que hace la separacion. Se basa en un algoritmo de segmentación foreground background Gaussiano
#mixto. En este caso vamos a usar MOG2.
fore_g_back_g = cv.createBackgroundSubtractorMOG2(detectShadows=True)
#Hay otro que se llama KNN
fore_g_back_g_2 = cv.createBackgroundSubtractorKNN()
while True:
    ret,frame = vcap.read()
    if frame is None:
        break
    #Sacamos la máscara del foreground
    foreground_mask = fore_g_back_g.apply(frame)
    foreground_mask_2 = fore_g_back_g_2.apply(frame)
    #La mostramos
    cv.imshow('FGMask_MOG2',foreground_mask)
    cv.imshow('FGMask_KNN', foreground_mask_2)
    cv.imshow('Frame',frame)

    key = cv.waitKey(30)
    if key == 'q' or key == 27:
        break


vcap.release()
cv.destroyAllWindows()