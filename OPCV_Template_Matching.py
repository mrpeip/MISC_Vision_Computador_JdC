import cv2 as cv
import  numpy as np

"""
Template matching consiste en encontrar una imagen o patron dentro de otra imagen
"""

img = cv.imread('Image&Video/messi5.jpg')
#Pasamos la imagen a gris
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#Cargamos la cara de Messi, en escala de grises
face = cv.imread('Image&Video/messi5_face.jpg',0)
#Uso las fuciones de OPCV. Indico la imagen, y la template. Los métodos están descritos en la bibliografía de OPCV.
res = cv.matchTemplate(img_gray,face,cv.TM_CCOEFF_NORMED)
#"res" incluye un montón de valores, entre ellos el valor del más brillante, que muestra donde hizo match.
print(res)
#Vamos a buscar ese punto más brillante usando numpy
#Definimos que valor de brillo será umbral para decir que hay match
thresh = 0.9
#A partir de los puntos (deben ser pocos, a ser posible 2) vamos a dibujar el rectángulo que nos indique el match
w,h = face.shape[::-1] #Sacamos las columnas y las filas en forma inversa
#Para cada match, vamos a dibujar un rectágulo
loc = np.where(res >= thresh)
for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h),(0,255,0),4)
cv.imshow('img',img)
cv.waitKey()
cv.destroyAllWindows()