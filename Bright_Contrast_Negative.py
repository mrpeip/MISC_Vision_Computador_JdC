import cv2 as cv
import numpy as np

#Cargo la imagen en escala de grises
img = cv.imread("Brillo_Contraste_Negativo/girl.png",0)

#La operacion matematica para modificar brillo y contraste es:
# new_img = alpha* img + beta (Pixel a pixel)
#Donde alpha controla el constraste y beta el brillo
alpha = 1
beta = 50
#Uso la funcion addWeighted para aumentar el contraste y el brillo segun alpha y beta. Uso una matriz de ceros para ajustar como segunda source, aunque se puede usar la
#misma imagen, como demuestra test. Importante, para esta funcion el brillo lo controla "gamma" NO "beta" por lo que hay que poner nuestra beta en "gamma" y poner beta a 0
new_img = cv.addWeighted(img,alpha,np.zeros(img.shape,img.dtype),0,beta)
#En test: Con addWeighted cargo la imagen, le pongo su alpha,cargo la misma imagen, pongo su beta a 0 y pongo su gamma. EN esta funcion, gamma controla el brillo, no beta!!!
test = cv.addWeighted(img,alpha,img,0,beta)

#NEGATIVO DE UNA IMAGEN
#Crear el negativo es sencillo, hay que usar la funcion bitwise_not (Ver operaciones bitwise)
negative = cv.bitwise_not(img)


cv.imshow("Original",img)
cv.imshow("Adjusted",new_img)
cv.imshow("T",test)
cv.imshow("Negative",negative)
cv.waitKey(0)
cv.destroyAllWindows()