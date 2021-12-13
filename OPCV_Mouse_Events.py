import cv2
import numpy as np
"""
Antes de empezar, mediante el siguinte print se pueden ver todos los eventos que tiene open cv
"""
events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)
#Definimos una función que nos devuelva informacion cuando hagamos clic
def click_event (event,x,y,flags,param):
    #Si se hace clic izquierdo
    if event == cv2.EVENT_LBUTTONDOWN:
        font = cv2.FONT_HERSHEY_PLAIN
        xyvalue = str(x) + ' ' + str(y)
        #Escribo el valor de la posicion donde hice clic
        cv2.putText(img,xyvalue,(x,y),font,.5,(255,255,0),2)
        cv2.imshow('Image',img)
    #Si se hace clic derecho
    if event == cv2.EVENT_RBUTTONDOWN:
        #Si hago clic derecho voy a mostrar los colores BGR del punto
        #Para ello trato la imagen (img) como si fuera una lista, donde meto los valores de x e y y selecciono
        #El canal de color que quiero (0 - azul,1 - verde, 2 -rojo)
        blue = img[y,x,0]
        green = img[y,x,1]
        red = img[y,x,2]
        font = cv2.FONT_HERSHEY_PLAIN
        bgrvalue = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, bgrvalue, (x, y), font, 1, (255, 255, 0), 2)
        cv2.imshow('Image', img)
    #Ahora vamos a dibujar una linea de un punto a otro de la imagen con clic central
    #Si hacemos clic central en el raton
    if event == cv2.EVENT_MBUTTONDOWN:
        #Vamos a dibujar un circulo que marque el inicio
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        #Guardo el punto clicado en una lista como un tuple (x,y)
        points.append((x,y))
        #Si se ha clicado el primer punto, el siguiente debe crear la linea
        if len(points) >=2:
            #Uno el ultimo valor de (x,y) con el anterior OJO! Entonces esto es una polilinea
            cv2.line(img,points[-1],points[-2],(255,0,0),4)
        cv2.imshow('Image',img)



#Como es mas comodo ver esto sobre una pantalla negra, la creo con numpy
img = np.zeros([512,512,3],np.uint8)
cv2.imshow('Image',img)
#Inicializo la lista que va a almacenar los puntos clicados con mmb
points = []
cv2.setMouseCallback('Image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()