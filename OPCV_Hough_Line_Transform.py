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
cv.imshow('Original',img)

#Paso a gris para aplicar Canny
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#Saco los bordes con Canny
edges = cv.Canny(grey, 30, 170, apertureSize=3)
#Voy a mostrar los bordes que detecta Canny
cv.imshow('canny',edges)
#Saco las lineas con Hough Standard, ojo a los parámetros:
"""
Variable de salida (lines): La función devuelve un vector de líneas. Cada linea está representada como un vector de 
dos o 3 elementos (p,teta) o (p,teta,votes). "p" es la distancia desde la coordenada de origen (0,0) que se toma la
parte superior izquierda de la imagen."teta" es el ángulo de rotación de la linea. "votes" es el valor del acumulador.

image: imagen a tratar

p(rho): Distancia de resolución del acumulador en pixeles (se suele tomar 1)

teta: Ángulo de la resolución del acumulador en RADIANES (suele usar pi/180)

threshold: Parámetro de umbralización del acumulador. Marca un umbral para devolver sólo las lineas que tienen suficiente
"votes" como para sobrepasar el umbral.
"""
lines = cv.HoughLines(edges, 1, np.pi/180, 200)
#!!!!!!! RECORDAR QUE LAS LINEAS ESTAN EN POLARES !!!!!!!

#Itero las lineas:
for line in lines:
    rho, teta = line[0]
    #Vamos a pasar de polares a cartesianas
    a = np.cos(teta)
    b = np.sin(teta)
    #Sacamos el origen de la linea (que debería ser el (0,0) o el top-left de la imagen
    x0 = a*rho
    y0 = b*rho
    #Vamos a sacar otros 2 puntos, para ello usamos la ecuación:
    #   x = r*cos(teta) +/- (offset)*sin(teta)    Usamos + en un punto y menos en otro
    #   y = r*sin(teta) -/+ (offset)*cos(teta)    Ojo a usar signos opuestos respecto a x!!!
    #NOTA: r*cos(teta) es x0, y sin(teta) = b
    #Donde el offfset (en pixeles) es cuanto queremos separar los puntos
    x1 = int(x0 - 1000*b)
    y1 = int(y0 + 1000*a)
    x2 = int(x0 + 1000*b)
    y2 = int(y0 - 1000*a)
    #Dibujamos la linea, usaremos dos puntos:
    cv.line(img, (x1,y1), (x2,y2), (0,0,255),2)

cv.imshow('Hough',img)
cv.waitKey(0)
cv.destroyAllWindows()