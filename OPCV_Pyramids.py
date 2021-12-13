import cv2 as cv
import numpy as np
"""
Usando piramedes de imagenes podemos crear imagenes de distintas resoluciones . Es un tipo de representación 
multi-escala en el que la imagen se somete a smothing y subsampling repetidas veces (reduce la resolución)
Hay 2 tipos de pirámides en OpenCV:
1. Gausiana -- Consiste en aplicar filtro gaussiano y subsampling
2. Laplaciana
"""

img = cv.imread('Image&Video/lena.jpg')

#Gaussian
#Reduce la resolución 1/2
lower_res = cv.pyrDown(img)
#Si aplicamos el método otra vez, reducimos 1/2 de un 1/2, o sea 1/4
lower_res2 = cv.pyrDown(lower_res)

#Este aumenta la resolución 1/2
h_res = cv.pyrUp(img)
# ------ !!! Si hacemos un pyrUp de una imagen a la que hicimos pyrDown va a salir borrosa, porque perdimos resolucion

"""
Voy a crear la pirámide Gaussiana
"""
layer = img.copy()
g_pyramid = [layer]

#Vamos a reducir 5 veces la resolución
for i in range(6):
    layer = cv.pyrDown(layer)
    g_pyramid.append(layer)
    #Con str(i) le asigno un nombre en funcion de la itereacion
    cv.imshow(str(i),layer)


"""
Voy a formar la Laplaciana. No hay una función exclusiva para ella, se crean a partir de las Gaussianas.
Para crear un nivel de la pirámide Laplaciana se toma la diferencia entre ese nivel en la pirámide Gaussiana y 
y la versión expandida del nivel gaussiano superior.

La Laplaciana muestra los edges de las imagenes de la piramide Gaussiana
"""

#Sacamos la utilima imagen del array g_pyramid
layer = g_pyramid[5]
laplace_pyr = [layer]
for i in range(5, 0, -1):
    #Creamos la version extendida del nivel superior
    gauss_expanded = cv.pyrUp(g_pyramid[i])
    laplacian = cv.subtract(g_pyramid[i-1],gauss_expanded)
    cv.imshow(str(i), laplacian)


#cv.imshow('pyrUp',h_res)
#cv.imshow('pyrD', lower_res)
#cv.imshow('pyrD2', lower_res2)
#cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()