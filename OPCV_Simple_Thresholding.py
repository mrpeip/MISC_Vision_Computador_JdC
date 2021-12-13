import cv2 as cv
import numpy as np

"""
El thresholding es una operacion utilizada para separar un objeto de su fondo. COnsiste en comparar cada pixel de una
imagen con un valor umbral. Hay dos thresholds, uno en el que el pixel esta por debajo y otro por arriba de un valor.
"""

img = cv.imread('Image&Video/gradient.png',0)
"""
BINARY THRESHOLD: Compara cada pixel de la imagen a 127 y si es menos de eso el pixel pasa a valir 0, y si es mayor
pasa a valir 255 (que como es blanco y negro pues pasa a blanco)
"""
ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

"""
BINARY INVERSE THRESHOLD: Compara cada pixel de la imagen a 127 y si es menos de eso el pixel pasa a valir 255, y si es mayor
pasa a valir 0. O sea, lo opuesto a BINARY
"""
ret,th2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

"""
TRUNC THRESHOLD: Hasta que se alcance el umbral marcado (127) la imagen no se cambia, pero a partir de 127 se asigna
127 a todos los demás
"""
ret,th3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)

"""
TO_ZERO THRESHOLD: Cualquier valor inferior al umbral (127) se asigna 0, a todos los superiores se los deja como está.
Esta técnica tiene inversa, igual que BINARY
"""
ret,th4 = cv.threshold(img,127,255,cv.THRESH_TOZERO)




cv.imshow('th1',th1)
cv.imshow('th2',th2)
cv.imshow('th3',th3)
cv.imshow('th4',th4)
cv.imshow('img',img)


cv.waitKey(0)
cv.destroyAllWindows()