import cv2 as cv
import numpy as np
"""
Los contornos son la curva uniendo todos los puntos en un borde que tienen el mismo color. Util en detección de 
objetos. Se suele usar una imagen binaria (gris), que lo hace más facil. El gris se usa para detectar, el color para
mostrar el resultado.
"""


img = cv.imread('Image&Video/opencv-logo.png')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

"""
Para empezar vamos a calcular el umbral o podemos sacar bordes con Canny
"""
ret,th1 = cv.threshold(imgray,127,255,0)

#Tras umbralizar, vamos a sacar los contornos. La variable "countours" devuelve una lista con todos los contornos
#de la imagen. Cada contorno es un array de numpy de las coordenadas (x,y) de los bordes del objeto.


#Los parámetros son: la imagen umbralizada, el modo de obtención de contornos (hay varios), el método de aproximación
#del contorno (hay varios)
countours,hierarchy = cv.findContours(th1,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print("El numero de contornos es: " + str(len(countours)))


#Tras sacar los contornos en forma de array, debemos ahora dibujarlos. Los vamos a dibujar sobre la imagen original.
#Los parámetros son: imagen original, contornos, indice de los contornos, color y grosor
cv.drawContours(img, countours, -1, (0,255,0),3)

cv.imshow('img',img)
cv.imshow('gray',imgray)
cv.waitKey(0)
cv.destroyAllWindows()
