import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
"""
El gradiente de una imagen es un cambio de dirección de la intensidad o el color en una imagen.
Se usan para detectar bordes (edges) en las imagenes. Existen varios tipos de gradientes.
"""
img  = cv.imread('Image&Video/messi5.jpg',0)
cv.imshow('Original',img)
#Aqui no funciona muy bien 0, usaría cv.GRAYSCALE
"""
Gradiente Laplaciano.
Parámetros: imagenes, datatype (debe poder lidiar con negativos y decimales, por tanto un float). opcionalmente se
puede dar un valor fijo al kernel, que puede mejorar o empeorar las cosas
"""

laplace = cv.Laplacian(img, cv.CV_64F,ksize= 3)
#Vamos a coger el valor absoluto del laplaciano para pasarlo de vuelta a un int, que es lo que es la imagen
laplace = np.uint8(np.absolute(laplace))
cv.imshow('Laplace',laplace)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Sobel: Hay 2 dos tipos, Sobelx y Sobely. Sobel_X es bueno para cambios en la dirección vertical mientras que 
Sobel_Y es bueno en la dirección horizontal . Se puede combinar el resultado ambas.

Parámetros: imagen, tipo de datos (recomendado float), si es en x [dx] (1/0), si es en y [dy] (1/0).
Opcionalmente el tamaño de kernel en int, como en Laplace
"""

sobel_x = cv.Sobel(img, cv.CV_64F, 1, 0)
sobel_y = cv.Sobel(img, cv.CV_64F, 0, 1)
#Debemos volver a pasarlo a int, porque las imagenes son int
sobel_x = np.uint8(np.absolute(sobel_x))
sobel_y = np.uint8(np.absolute(sobel_y))

#Se pueden combinar los dos sobel en uno
sobel_comb = cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('Sobel x',sobel_x)
cv.imshow('Sobel y',sobel_y)
cv.imshow('Sobel',sobel_comb)
cv.waitKey(0)
cv.destroyAllWindows()

titles = ['image','Laplacian','Sobel X', 'Sobel Y','Sobel']
images = [img,laplace,sobel_x,sobel_y,sobel_comb]
for i in range(5):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()