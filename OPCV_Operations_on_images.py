import cv2
import numpy as np

img = cv2.imread('Image&Video/messi5.jpg')

""" 
A continuacion se muestran unas cuantas operaciones para sacar informacion sobre una imagen
"""
print(img.shape) #Devuelve un tuple con el tamaño de la imagen, en forma de numero de filas, columnas y canales (MATRIZ)
print(img.size) #Devuelve el numero total de pixeles
print(img.dtype) #Devuelve el tipo de dato que es la imagen (MATRIZ)

#Vamos a mover la pelota, que es nuestra ROI (Region of Interest)
#Se asume que se conocen las coordenadas de la pelota (por rapidez)

#Usando numpy, saco el recuadro que incluye la pelota poniendo el punto inicial y el final
ball = img[280:340, 330:390]

#Ahora voy a meter la pelota en otras coordenadas (en otro rectangulo de coordenadas)
img[273:333, 100:160] = ball

""" Aqui se muestra como unir imagenes"""
#Las operaciones se realizan sobre MATRICES de imagen, no sobre la imagen sin más
img2 = cv2.imread('Image&Video/opencv-logo.png')
#Para usar el método "add" ambas imagenes (o matrices de imagen) deben tener el mismo tamaño, ajustamos tamaños
img = cv2.resize(img,(512,512))
img2 = cv2.resize(img2,(512,512))
#La union de las imagenes tiene los pesos (que imagen predomina sobre cual) ajustados de manera automatica
dst = cv2.add(img,img2)
#Si se quieren ajustar los pesos de manera manual se debe usar "addWeighted", donde alpha es el peso de la primera
#imagen, beta el de la segunda, y gamma un valor escalar que se suma a las imagenes
dst2 = cv2.addWeighted(img,0.2,img2,0.8,0)


cv2.imshow('img',img)
cv2.imshow('img2',img2)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)

""" Finalmente se muestra como separar y unir una imagen en sus valores bgr"""
b,g,r = cv2.split(img)
cv2.imshow('b',b)
cv2.imshow('g',g)
cv2.imshow('r',r)
cv2.waitKey(0)
cv2.destroyAllWindows()