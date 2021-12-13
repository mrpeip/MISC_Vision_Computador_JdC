import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Image&Video/smarties.png',0)
_,mask = cv.threshold(img,220,255,cv.THRESH_BINARY_INV)


"""
Si vemos las imagenes, al aplicar el thresholding siguen quedando huecos negros dentro de las bolas,
para eleminar esos huecos vamos a apicar la transformación morfologica de dilation
"""
#Para ello usamos esta función. Esta funcion requiere un kernel, un kernel es un cuadrado o una forma que queremos
#aplicar a la imagen, lo definimos en numpy con una matriz de 1s que viene a decir que queremos meter blancos a la imagen

#En este caso el kernel es un cuadrado de 2x2
kernel = np.ones((2,2),np.uint8)

#Si solo aplicamos el kernel una vez no vamos a eliminarlos todos, para ello añadimos el parámetro iterations que
#causa que apliquemos el kernel varias veces a la imagen
dilation = cv.dilate(mask,kernel, iterations= 2)
cv.imshow('Binary',mask)
cv.imshow('Dilated',dilation)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Podemos ampliar el numero de iteraciones, o aumentar el tamaño del kernel eliminamos más negros, pero también vamos
fusionando circulos y haciendolos crecer, porque cambia los pixeles
"""

"""
La segunda transformación es erode, lo que hace es erosionar los bordes de la imagen/objeto foreground 
que causa que el kernel pase por toda la imagen y un pixel de la imagen original que puede ser 1 o 0 se considerará 1 
solo si todos los pixeles bajo el kernel son 1, de otra manera se le asigna 0
"""

erosion = cv.erode(mask,kernel, iterations=3)
cv.imshow('Binary',mask)
cv.imshow('Eroded',erosion)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Otras operaciones son "open" y "close". Opening es hacer una erosion seguida de un dilation. Closing es lo opuesto
una dilation seguida de una erosion
"""

opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernel)

closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernel)
cv.imshow('Binary',mask)
cv.imshow('Opening',opening)
cv.imshow('Closing',closing)
cv.waitKey(0)
cv.destroyAllWindows()
"""
Com la funcion morphologyEx tenemos un monton de operaciones, aqui muestro algunas:
gradient --  Hace la diferencia entra la dilation y la erosion de una imagen
tophat --  Es la diferencia entre la imagen y opening
muchas mas, ver documentacion
"""

gradient = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernel)
cv.imshow('XOR/Gradient',gradient)
cv.waitKey(0)
cv.destroyAllWindows()
tophat = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernel)

titles = ['Image','mask','dilation','erosion','opening','closing','gradient','tophat']
images = [img,mask,dilation,erosion,opening,closing,gradient,tophat]
for i  in range(8):
    plt.subplot(4,4,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()