import numpy as np
import cv2 as cv

img = cv.imread("Filtros/Road.jfif",0)

#Filtro de medias

av_1 = cv.blur(img,(5,5))
av_2 = cv.boxFilter(img,-1,(5,5),normalize=True)

cv.imshow("Original",img)
cv.imshow("av1",av_1)
cv.imshow("av2",av_2)

#Filtro Gaussiano
gaus = cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
cv.imshow("gauss",gaus)

#Filtro de mediana
med = cv.medianBlur(img,7)
cv.imshow("med",med)

#Filtro bilateral
bi = cv.bilateralFilter(img,5,0,0)
cv.imshow("bi",bi)
cv.waitKey(0)
cv.destroyAllWindows()