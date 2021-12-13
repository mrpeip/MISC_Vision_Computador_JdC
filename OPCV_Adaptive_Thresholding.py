import cv2 as cv
import numpy as np

"""
En casos donde hay diferente iluminacion en diferentes regiones de la imagen, el thresholding basico falla, para ello
se usa thresholding adaptativo, que calcula el umbral no de manera global(como hace el simple) sino de manera local 
para distintas regiones.
"""
img = cv.imread('Image&Video/sudoku.png',0)
cv.imshow('img',img)

#Realizando un threshold normal, como por ejemplo binario:
_,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
cv.imshow('th_binary',th1)
#Se ve que la imagen se corta, y no muestra las cosas bien

"""
Ahora aplicaremos distintas metodologías adaptativas. Primero decimos la imagen, el maximo valor que toma,
el método adaptativo, el metodo de thresholding que queremos, el tamaño del "neigbourhood" (que debe ser impar)
y finalmente una constante que le vamos a restar a la media (normal o Gaussiana)
"""
#Media
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('ath1',th2)
#Media Gaussiana
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
cv.imshow('ath2',th3)


cv.waitKey(0)
cv.destroyAllWindows()