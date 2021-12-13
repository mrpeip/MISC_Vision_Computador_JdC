import cv2
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
Aqui vamos a aplicar filtros lineales (espaciales) para eliminar ruido !!
"""
img = cv.imread('Image&Video/noisy_chaplin.png')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
img_bi = cv.imread('Image&Video/taj.jpg')


"""
Filtro homogeneo o de la media: Cada pixel de salida es la media de sus vecinos de kernel
En filtros homogeneos el kernel tiene esta forma:

kernel = 1/(Kwith * Kheight) = [1 1 1; 1 1 1; 1 1 1; ...] (ojo notacion de matriz de matlab)
EJ: kernel = 1/25*[1 1 1 1 1;1 1 1 1 1; 1 1 1 1 1; 1 1 1 1 1; 1 1 1 1 1] (5x5)=25 
"""
kernel_h = 1 / 25 * np.ones((5, 5), np.float32)
# La función filter2D realiza un filtro homogéneo. Sus parámetros son:
# La imagen, la profundidad de la imagen de salida, el kernel
homog_f = cv.filter2D(img, -1, kernel_h)
cv.imshow('Media', homog_f)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Se pueden aplicar low y high pass filters. Los filtros de paso bajo son útiles para eliminar ruido, mientras que 
los filtros de paso alto sirven para econtrar edges en las imágenes
"""

# PRIMER LOW PASS: Box Filter
# Parámetros: imagen, tamaño del kernel

blur = cv2.blur(img, (5, 5))

# SEGUNDO LOW PASS: Gaussian
# El filtro gaussiano usa un kernel con distintos pesos para la dirección x y para la y, en el resultado los píxeles
# situados en el centro del kernel tienen más peso que los exteriores
# El filtro gaussiano se usa concretamente para eliminar ruido de alta frecuencia !!!!!! -----

# Parámetros: imagen, tamaño del kernel, sigmaX(desviación estándar)

gauss = cv.GaussianBlur(img, (5, 5), 1)
cv.imshow('Gauss', gauss)
cv.waitKey(0)
cv.destroyAllWindows()
# TERCER LOW PASS: Mediana
# Este filtro reemplaza cada valor de un pixel por la mediana de los valores de los pixeles vecinos.
# Funciona muy bien para ruidos de tipo salt and pepper.

# El tamaño del kernel debe ser un numero impar! Y solo un int
median = cv.medianBlur(img, 5)
cv.imshow('Mediana', median)
cv.waitKey(0)
cv.destroyAllWindows()

# CUARTO: Filtro bilateral. Este filtro no emborrona los bordes, que a veces es necesario
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral', bilateral)
cv.waitKey(0)
cv.destroyAllWindows()
#Ahora usando la imagen con ruido Gaussiano
bilateral_2 = cv.bilateralFilter(img_bi, 9, 75, 75)
gauss_2 = cv.GaussianBlur(img_bi, (5, 5), 1)
cv.imshow('Origina_BI',img_bi)
cv.imshow('Bilateral', bilateral_2)
cv.imshow('Gauss_2', gauss_2)
cv.waitKey(0)
cv.destroyAllWindows()

titles = ['Original', 'Mean', 'Box', 'Gauss', 'Median', 'Bilateral']
images = [img, homog_f, blur, gauss, median, bilateral]
for i in range(6):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
