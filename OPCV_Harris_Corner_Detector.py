import cv2 as cv
import numpy as np

"""
Este metodo detecta "esquinas". Las esquinas son las zonas de las imagenes donde hay grandes variaciones en intensidad
en todas las direcciones (x e y). Tiene 3 pasos:
1. Detectar que ventanas tienen grandes variaciones de intensidad en la dirección x y en l y
2. Para cada ventana detectada, se calcula su puntuación "R" (cuanto se estima la esquina)
3. Tras aplicar un umbral a las puntuaciones, se seleccionan las esquinas importantes.
"""

img = cv.imread('Image&Video/pic1.png')
cv.imshow('Original',img)
cv.waitKey(0)
cv.destroyAllWindows()

#Paso a gris
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#El metodo de Harris toma la imagen en formato Float32, asi que lo paso a ese
grey = np.float32(grey)

#El metodo tiene los siguientes parámetros
"""
dst = Imagen de salida
image = imagen a tratar en formato de escala de grises y float32
blockSize = Tamaño de la ventana para detectar esquinas. Por tanto ventana de [y*y] tamaño.
ksize = Parametro de apertura de el metodo Sovel que se usa
k = Parámetros de Harris 
"""
dst = cv.cornerHarris(grey, 2, 3, 0.05)
#Dilatamos el resultado para mejorarlo
dst = cv.dilate(dst,None)

#Marcamos las esquinas con color rojo
img[dst>0.01*dst.max()] = [0,0,255]

cv.imshow('Harris2',img)

cv.waitKey(0)
cv.destroyAllWindows()