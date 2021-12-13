import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
"""
Histogramas y su uso
"""
img_2 = cv.imread('Image&Video/lena.jpg')
grey = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
#Creo una imagen binaria en blanco y negro
img = np.zeros((200,200), np.uint8)
cv.rectangle(img,(0,100),(200,200), (255,255,255), -1)

"""
Primero mostraremos el histograma usando matplotlib
"""
plt.hist(img.ravel(), 255, [0,255])
cv.imshow('img', img)
plt.show()

#Y para lena
plt.hist(grey.ravel(), 255, [0,255])
cv.imshow('lena_gray', grey)
plt.show()
# Si quisieramos sacarlo en color
b, g, r = cv.split(img_2)
cv.imshow('Lena', img_2)
cv.imshow('b', b)
cv.imshow('g', g)
cv.imshow('r', r)
plt.hist(b.ravel(), 255, [0,255])
plt.hist(g.ravel(), 255, [0,255])
plt.hist(r.ravel(), 255, [0,255])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()

#Se puede ecualizar el histograma para mejorar el contraste de una imagen
cv.imshow('lena_grey',grey)
plt.hist(grey.ravel(), 255, [0,255])
plt.show()

grey_eq = cv.equalizeHist(grey)
cv.imshow('lena_grey_eq',grey_eq)
plt.hist(grey_eq.ravel(), 255, [0, 255])
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()