import cv2 as cv
import numpy as np

img = cv.imread('Image&Video/smarties.png')
cv.imshow('Original',img)
output = img.copy()
"""
La ecuación que rige como es un circulo es:
(x-xcentro)^2+(y-ycentro)^2 = r
siendo (xcentro,ycentro) el centro del circulo y r el radio
Lo que vamos a buscar detectar es el centro del circulo y su radio
"""
#Hough funciona mejor en gris
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Hough también funciona mejor si hacemos un blur
grey = cv.medianBlur(grey,5)
"""
La funcion HoughCircles nos detecta los circulos en fución de los siguientes parámetros:
circles = Vector de salida con los circulos detectados
image = 8bit, single channel, en gris. La imagen de entrada
method = Método de detección, aplican los mismos que HoughStandard, usaremos HOUGH_GRADIENT
dp = Ratio inverso del la resolucion del acumulador frente a la resolución de la imagen
minDist = Distancia minima entre centros de circulos
param1 = Primer parámetro del método de detección. Depende del metodo. Para HOUGH_GRADIENT es el umbral mayor que se
pasará a Canny.
param2 = Lo mismo que param1. En HOUGH_GRADIENT es el umbral del acumulador para los centros de los circulos en la fase
de detección
minRadius = Radio minimo del circulo
maxRadius = Radio máximo del circulo. Si <=0 usa toda la imagen. Si <0 devuelve solo los centros, no los radios. 
"""
circles = cv.HoughCircles(grey,cv.HOUGH_GRADIENT,1,20,param1=50, param2=30,minRadius=0,maxRadius=0)
#Paso los circulos redondeados
detected_circles = np.uint16(np.around(circles))

for (x, y ,r) in detected_circles[0,:]:
    #Dibujamos el circulo (x,y) es el centro
    cv.circle(output,(x,y),r,(0,255,0),4)
    #Dibujamos el centro, para ello cambiamos el radio a algo muy pequeño para que aparezca como un punto
    cv.circle(output, (x, y), 2, (0, 255, 0), 4)






cv.imshow('output',output)
cv.waitKey(0)
cv.destroyAllWindows()