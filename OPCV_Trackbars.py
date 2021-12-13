import cv2 as cv
import numpy as np
"""
Este código crea varios slicers en la ventana que muestra la imagen. Estos slicers permiten modificar valores 
dentro de la imagen
"""
#Defino la función que define lo que hace la Trackbar
def nothing(x):
    print(x)


#Genero una imagen en negro (que así se ve bien)
img = np.zeros([300,512,3],np.uint8)
cv.namedWindow('img')
"""
Creo las trackbars, una para cada color BGR. Le doy un nombre, le digo en que ventana actúa, su valor inicial (minimo)
y su valor máximo. Finalmente indico la función que se realizará para cada valor (en nuestro caso: nothing(x), que no
hace nada, pero es un requerimiento)
"""
cv.createTrackbar('B','img',0,255,nothing)
cv.createTrackbar('G','img',0,255,nothing)
cv.createTrackbar('R','img',0,255,nothing)

switch = '0 : OFF\n 1 : ON'
cv.createTrackbar('Switch','img',0,1,nothing)

while(1):
    cv.imshow('img',img)
    key = cv.waitKey(1) & 0xFF #Cerrar al hacer clic en Esc
    if key == 27:
        break
    #Vamos a sacar el valor de cada trackbar
    b = cv.getTrackbarPos('B','img')
    g = cv.getTrackbarPos('G', 'img')
    r = cv.getTrackbarPos('R', 'img')
    s = cv.getTrackbarPos('Switch','img')
    #Si el switch esta en cero, no hacemos nada, de otra manera modificamos todos los pixeles con el valor BGR que
    #hayamos metido en los trackbar de BGR
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv.destroyAllWindows()