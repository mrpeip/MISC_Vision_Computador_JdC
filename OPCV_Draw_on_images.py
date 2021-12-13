import cv2 as cv
import numpy as np
#Cargamos una imagen en color
img = cv.imread('Image&Video/lena.jpg',1)

#Dibujamos una linea en la imagen usando el metodo "line"
img = cv.line(img,(0,0),(255,255),(255,0,0),5)
""" Los parámetros son: la imagen, las coordenas en la forma (xorigen,yorigen),(xfinal),y(final), el color en forma BGR
Blue Green Red (255,255,255) para los colores, y finalmente lo gordo de la linea
"""
#Dibujamos una flecha
img = cv.arrowedLine(img,(25,0),(200,25),(0,255,0),5)

#Ahora un rectágulo
#NOTA: Aquí las coordenadas van diferente, el primer punto es el del vertice top-left y el otro el bottom-right
#Si ponemos -1 en el grosor, lo que hará será rellenar el rectángulo
img = cv.rectangle(img,(384,0),(500,128),(0,0,255),-1)

#Ahora un circulo
#NOTA: Aqui en lugar de coordenadas tenemos el centro del circulo y el radio, lo demás igual
img = cv.circle(img,(440,63),50,(255,255,0),10)

#Ahora añadimos texto
#NOTA: Los parámetrps son: imagen, coordenada de inicio de texto, fuente(escoger previo),tamaño del texto
#color y grosor
font = cv.FONT_ITALIC
img = cv.putText(img,'Hello There',(10,500),font,3,(0,0,0,5))
"""
Podemos usar numpy para crear imágenes, en este caso se usa la matriz de ceros para crear un fondo negro
Los parámetros son: [altura,anchura,
"""
black = np.zeros([512,512,3],np.uint8)
#Mostramos el resultado
cv.imshow('Imagen',img)
cv.imshow('Negro',black)
cv.waitKey(0)
cv.destroyAllWindows()