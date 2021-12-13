import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
El detector de bordes Canny es un operador que puede detectar bordes. El algoritmo se compone de cinco pasos:
1. Reducción de ruido con filtro Gaussiano
2. Calcular el gradiente de la imagen
3. Supresion de los no-máximos
4. Doble umbral (double threshold) para determinar posibles bordes
5. Seguimiento de los bordes por histéresis, detectar solo los bordes fuertes

"""
img  = cv.imread('Image&Video/messi5.jpg',cv.IMREAD_GRAYSCALE)
#Los parámetros de Canny son la imagen y los umbrales de histéresis. Los umbrales debería ser optimizados,
#Se puede usar Otsu o un trackbar para ir ajustando
canny = cv.Canny(img, 100, 200)




titles = ['Original','Canny']
images = [img,canny]
for i in range(2):
    plt.subplot(2,1,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()