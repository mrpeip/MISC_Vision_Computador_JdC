import cv2 as cv
import numpy as np

img = cv.imread('Image&Video/shapes_1.png')
img_Gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Umbralizamos la imagen
_, thresh = cv.threshold(img_Gray, 240, 255, cv.THRESH_BINARY)
# Sacamos los contornos de la foto
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

for contour in contours:
    # Este metodo aproxima curvas polinomicas con una precision especifica. Epsilon es el parametro que ajusta la
    # precision. cv.arcLenght saca la longitud de un curva. Los True son para expresar que los contornos son
    # formas cerradas
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True)
    # [] es otra manera de escribirlo, vale poner approx sin mas. Ponemos 0 porque solo debería haber un contorno.
    cv.drawContours(img, [approx], 0, (255, 0, 0), 4)
    # Vamos a sacar las coordenadas de la forma para decir que es. Con ravel, el primer ídice es la x y el segundo y
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    # En funcion de la cantidad de puntos de la curva poligonal podemos descifrar que forma es
    # Si tiene 3 vertices es un triangulo
    if len(approx) == 3:
        cv.putText(img, 'Triangle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    # Si tiene 4 vértices puede ser un cuadrado o un rectágulo
    elif len(approx) == 4:
        x, y, w, h = cv.boundingRect(approx)
        aspectratio = float(w) / float(h)
        if aspectratio >= 0.95 and aspectratio < 1.05:
            cv.putText(img, 'Square', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        else:
            cv.putText(img, 'Rectangle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 5:
        cv.putText(img, 'Pentagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    elif len(approx) == 10:
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
    # Si no es ninguna de estas, debe ser un circulo
    else:
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv.imshow('shape', img)
cv.waitKey(0)
cv.destroyAllWindows()
