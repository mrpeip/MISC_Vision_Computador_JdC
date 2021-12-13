import cv2
import numpy as np
"""
En este ejemplo se van a realizar operaciones bitwise, que son bastante utiles para trabajar con mascaras
Comenzamos cargando dos imagenes, una creada con numpy para ser un fondo negro con un rectangulo blanco, y otra
que cogemos de internet que son dos rectangulos, uno blanco y uno negro
"""
img1 = np.zeros([250,500,3],np.uint8)
img1 = cv2.rectangle(img1,(200,0),(300,100),(255,255,255),-1)
#Dado que la imagen de los rectangulos es de: 806x602 y la otra de 500x250, debo reajustarla
img2 = cv2.imread('Image&Video/black_white_rectangle.png')
#Recordar: Ancho, alto
img2 = cv2.resize(img2,(500,250))

""" ------- Aqui comienzan las operaciones bitwise -------
- Estas operaciones consisten en aplicar puertas logicas a las imagenes. (AND, OR, NOT....)
"""
#Aplicamos una puerta AND, que solo es 1 cuando ambas son 1. Se toma el negro como 0 y el blanco como 1
#Dado que el blanco y el negro nunca coinciden, sale todo negro (0)
bitAnd = cv2.bitwise_and(img2,img1)

#Aplicamos una puerta OR. Donde si A o B son 1, entonces 1
bitOr = cv2.bitwise_or(img2,img1)

#Aplicamos una puerta XOR. Cuando A y B son 0 o 1, 0 todo lo demas 1
#NOTA: XOR no luce con las imagenes que tenemos
bitXOR = cv2.bitwise_xor(img2,img1)

#Aplicamos NOT, que niega la imagenes.
bitNot = cv2.bitwise_not(img1)


cv2.imshow('Image1',img1)
cv2.imshow('Image2',img2)
cv2.imshow('bitAnd',bitAnd)
cv2.imshow('bitOR',bitOr)
cv2.imshow('bitXOR',bitXOR)
cv2.imshow('bitNot',bitNot)


cv2.waitKey(0)
cv2.destroyAllWindows()