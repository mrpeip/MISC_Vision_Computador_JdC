import cv2 as cv
import numpy as np

"""
En la transformación de Hough se trabaja con rectas representadas en coordenadas polares, del tipo:
r = x*cos(teta) + y*sin(teta)
El algoritmo consiste en los siguientes pasos:
1. Detección de los bordes. (Por ejemplo usando Canny)
2. Mapeo de los bordes al espacio Hough (m,c) y almacenamiento en un "acumulador"
3. Interpretación del acumulador para extraer lineas de longitud infinita. Esto se hace mediante thresholding o algo asi.
4. Pasar de lineas infinitas a finitas

OpenCV tiene dos métodos, un estándar y otro probabilístico
"""
#Este ejemplo usa el método estándar
img = cv.imread('Image&Video/sudoku.png')

#Paso a gris para aplicar Canny
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Saco los bordes con Canny
edges = cv.Canny(grey, 50, 150, apertureSize=3)
#Voy a mostrar los bordes que detecta Canny
cv.imshow('canny',edges)
#Saco las lineas con Hough Probabilistic,a diferencia del Standart, no coge todos los puntos
# sino aquellos que son estadísticamente relevantes para la linea. Ojo a los parámetros:
"""
Variable de salida (lines): La función devuelve un vector de líneas. Cada linea está representada como un vector de 
dos o 3 elementos (p,teta) o (p,teta,votes). "p" es la distancia desde la coordenada de origen (0,0) que se toma la
parte superior izquierda de la imagen."teta" es el ángulo de rotación de la linea. "votes" es el valor del acumulador.

image: imagen a tratar

p(rho): Distancia de resolución del acumulador en pixeles (se suele tomar 1)

teta: Ángulo de la resolución del acumulador en RADIANES (suele usar pi/180)

threshold: Parámetro de umbralización del acumulador. Marca un umbral para devolver sólo las lineas que tienen suficiente
"votes" como para sobrepasar el umbral.

minLineLength: Tamaño minimo de la linea (en pxls) para que sea estadísticamente relevante. Menos de esto se 
rechaza

maxLineGap: Maximo hueco (en pxls) permitido entre segmentos de una misma linea para que deje de contar como una
unica linea
"""
lines = cv.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=50, maxLineGap=5)
#!!!!!!! RECORDAR QUE LAS LINEAS ESTAN EN POLARES !!!!!!!


#Itero las lineas:
for line in lines:
    #A diferencia del metodo Standard, el probabilistico devuelve ya los dos puntos para hacer la linea (no hay que
    #pasar a polares)
    x1,y1,x2,y2 = line[0]

    #Dibujo la linea
    cv.line(img, (x1,y1), (x2,y2), (0,255,0, 2))

cv.imshow('Hough Probabilistic',img)
cv.waitKey(0)
cv.destroyAllWindows()
