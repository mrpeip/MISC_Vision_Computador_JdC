import cv2 as cv
import numpy as np
"""
Vamos a mezclar la mitad de una manzana y la mitad de una naranja. !!!!! OJO COMPLICADO!!!! 
"""



apple = cv.imread('Image&Video/apple.jpg')
orange = cv.imread('Image&Video/orange.jpg')

#Por poder, puedo partir las imagenes a la mitad y unirlas usando numpy y partiendo por pixels, ya que se que ambas
#son de 512x512

#En la manzana estoy cortando por la mitad en la x por la izquierda, y en la naranaja por la derecha, pero queda una
# linea en el medio, que no queda bien
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))

"""
Para mezclas ambas imagenes, podemos usar las piramides de imagenes, para ello hay que:
1. Cargar las dos imagenes
2. Calcular la pirámide gaussiana de cada imagen para los niveles necesarios para que quede bien (en este caso 6)
3. De las pirámedes Gaussianas, sacar las Laplacianas
4. Unir la manzana y la naranja en cada nivel de la pirámide Laplaciana
6. A partir de esta union de pirámides Laplacianas, recrear la imagen original
"""
#El paso 1 ya lo tenemos

#2a) Calculamos la piramide Gaussiana de la manzana

apple_layer = apple.copy()
a_gauss_pyr = [apple_layer]

for i in range(6):
    apple_layer = cv.pyrDown(apple_layer)
    a_gauss_pyr.append(apple_layer)

#2b) Calculamos la piramede Gaussiana para la naranja

orange_layer = orange.copy()
o_gauss_pyr = [orange_layer]

for i in range(6):
    orange_layer = cv.pyrDown(orange_layer)
    o_gauss_pyr.append(orange_layer)

#3a) Calculamos la pirámide Laplaciana de la manzana

apple_layer = a_gauss_pyr[5]
lap_apple_pyr = [apple_layer]
for i in range(5,0,-1):
    a_gauss_ext = cv.pyrUp(a_gauss_pyr[i])
    a_laplacian = cv.subtract(a_gauss_pyr[i-1],a_gauss_ext)
    lap_apple_pyr.append(a_laplacian)

#3b) Calculamos la pirámide Laplaciana de la naranja
orange_layer = o_gauss_pyr[5]
lap_orange_pyr = [orange_layer]
for i in range(5, 0, -1):
    o_gauss_ext = cv.pyrUp(o_gauss_pyr[i])
    o_laplacian = cv.subtract(o_gauss_pyr[i-1],o_gauss_ext)
    lap_orange_pyr.append(o_laplacian)

#4) Unimos la mitad izquierda de la manzana con la mitad derecha de la naranja para cada nivel de la pirámide
#Laplaciana
apple_orange_pyr = []
n = 0
#zip() une los parámetros que le metas en forma de un tuple, rollo: a = [Jenny,Paco] b = [Marcos, Juan]
#zip(a,b) = [(Jenny,Marcos),(Paco,Juan)]
for apple_lap,orange_lap in zip(lap_apple_pyr,lap_orange_pyr):
    n += 1
    #Vamos a sacar las columnas, filas y canales de cualquiera de las dos imágenes (ya que ambas deberían ser iguales)
    cols,rows,chan = apple_lap.shape
    #Unimos cada nivel de la pirámide por la mitad, a partir de las variables iteretivas *_lap
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    #Unimos cada imagen unida en la pirámide común
    apple_orange_pyr.append(laplacian)


#5) Reconstruimos la imagen a partir de la pirámide combinada

apple_orange_reconstruct = apple_orange_pyr[0]
for i in range(1,6):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyr[i],apple_orange_reconstruct)


cv.imshow('Reconstructed',apple_orange_reconstruct)



#Con estos comandos puedo ver que las imagenes tienen la misma forma (tamaño y tal)
print(apple.shape)
print(orange.shape)




cv.imshow('apple', apple)
cv.imshow('appleorange', apple_orange)
cv.imshow('orange', orange)
cv.waitKey(0)
cv.destroyAllWindows()