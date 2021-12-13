import numpy as np
import cv2
from matplotlib import pyplot as plt
#Leo la imagen con OpenCV
img = cv2.imread("Histogram_and_umbral/Apple.jfif",cv2.IMREAD_GRAYSCALE)
cv2.imshow("Apple",img)
#Utilizo matplotlib para calcular y mostrar el histograma, utilizando la funcion "hist"
#La funcion .ravel() permite normalizar el histograma entre el numero de pixels
#Parámetros: Imagen, maximo valor de los pixels, rango de valores de los pixels
plt.hist(img.ravel(),256,[0,256])
plt.show()
#Mediante "calcHist" puedo hacer lo mismo con Open CV
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
#ECUALIZAR UN HISTOGRAMA
eq_hist = cv2.equalizeHist(img)
cv2.imshow("Equalized",eq_hist)

#UMBRALIZACION/ THRESHOLDING BÁSICO
#Usando THRESH_BINARY devolvera bien blanco (255) a los valores que no superen el umbral y negro (0) a los que si
_,binary = cv2.threshold(img,130,256,cv2.THRESH_BINARY)
cv2.imshow("Umbral_BIN",binary)
#Usando THRESH_BINARY_INV con los mismos parámetros, obtengo el mismo resultado que antes pero con los valores de negro y blanco invertidos
_,binary_inv = cv2.threshold(img,130,256,cv2.THRESH_BINARY_INV)
cv2.imshow("Umbral_INV_BIN",binary_inv)
#Usando THRESH_TRUNC la imagen se mantiene como está hasta el valor umbral, y a partir de él se sustituye todo por ese valor
_,binary_trunc = cv2.threshold(img,130,256,cv2.THRESH_TRUNC)
cv2.imshow("Umbral_BINARY_TRUNC",binary_trunc)
#Usando THRESH_TOZERO causa que cuando el valor de un pixel es menor que el threshold, lo pinta de negro, y por encima del umbral se matiene como era
_,binary_to_zero = cv2.threshold(img,130,256,cv2.THRESH_TOZERO)
cv2.imshow("Umbral_BINARY_TOZERO",binary_to_zero)
#Usando THRESH_TOXERO_INV hacemos lo mismo que con el anterior, pero si NO supera el umbral queda igual, y si lo supera pasa a negro
_,binary_to_zero_inv = cv2.threshold(img,130,256,cv2.THRESH_TOZERO_INV)
cv2.imshow("Umbral_BINARY_TOZERO_INV",binary_to_zero_inv)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
