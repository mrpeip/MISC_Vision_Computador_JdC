import cv2 as cv
import numpy as np
#IMREAD_GREYSCALE y 0 hacen lo mismo
img = cv.imread("Otsu/boat.jpg",0)
#El metodo Otsu puede hacerse a mano en Python o se puede usar la funcion de OpenCV que ya lo incluye

#Defino dos variables, una que almacena el valor Otsu de umbral y otra que almacena la imagen resultante
otsu_threshold, img_res = cv.threshold(img,0,256,cv.THRESH_BINARY + cv.THRESH_OTSU)

print("El umbral por Otsu es: ",otsu_threshold)

#Muestro el resultado
cv.imshow("Original",img)
cv.imshow("Otsu",img_res)
cv.waitKey(0)
cv.destroyAllWindows()
