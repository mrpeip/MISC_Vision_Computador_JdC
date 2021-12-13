import cv2 as cv
import numpy as np

vcap = cv.VideoCapture('Image&Video/vtest.avi')
# Tomo dos fotogramas del video
ret, frame1 = vcap.read()
ret, frame2 = vcap.read()

while vcap.isOpened():
    # Calcula la diferencia absoluta entre dos fotogramas
    diff = cv.absdiff(frame1, frame2)
    # Pasamos la diferencia a gris, porque vamos a trabajar con contornos, y se hace más fácil en gris
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # Aplicamos un blur
    blur = cv.GaussianBlur(gray, (5, 5), 0)
    # Sacamos el umbral (Podemos usar Canny)
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    dilated = cv.dilate(thresh, None, iterations=3)
    # Sacamos el contorno
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Vamos a dibujar el
    for contour in contours:
        # Guardamos las coordenadas de los contornos, y se los ponemos a un rectangulo
        (x, y, w, h) = cv.boundingRect(contour)
        # Ahora sacamos el area del contorno, porque si el area es menor que cierto valor no será una persona
        if cv.contourArea(contour) < 700:
            continue
        else:
            cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(frame1, 'Status: {}'.format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
    # Mostramos el resultado de los contornos sobre frame 1
    cv.imshow('feed', frame1)

    # Actualizamos los frames, el 1 pasa a ser el dos y el 2 se vuelve a leer
    frame1 = frame2
    ret, frame2 = vcap.read()

    if cv.waitKey(40) == 27:
        break

cv.destroyAllWindows()
vcap.release()
