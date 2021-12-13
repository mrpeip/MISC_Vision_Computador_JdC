import cv2 as cv
import numpy as np

"""
Shi Tomasi es una mejora de Harris. Es igual que Harris excepto por como se calcula la puntuación R.
Permite detectar las equinas de la imagen (las de verdad, no todas)
"""

img = cv.imread('Image&Video/pic1.png')

#Paso a gris
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#El metodo de Shi Tomasi se llama goodFeaturesToTrack en honor a como se llamó el paper.
"""
image
maxNumberOfCorners = Numero maximo de esquinas a detectar. Si hay mas, devuelve las mejores
qualityLevel = Calidad minima esperada de una esquina
minDistance = Distancia euclidea minima entre esquinas
"""
corners = cv.goodFeaturesToTrack(grey,50,0.01,10)

#Pasamos las esquinas a numeros enteros
corners = np.int0(corners)

for i in corners:
    x,y = i.ravel()
    cv.circle(img,(x,y),3,(0,255,0),-1)

cv.imshow('Shi',img)
cv.waitKey(0)
cv.destroyAllWindows()