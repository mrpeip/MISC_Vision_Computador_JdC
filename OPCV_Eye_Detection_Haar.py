import cv2 as cv
import numpy as np
"""
Debo descargar el xml de los ojos
"""
eye_cascade = cv.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

vcap = cv.VideoCapture(0)
while vcap.isOpened():
    _,frame = vcap.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    #Nos interesa detectar una cara antes de detectar los ojos, o sea que ampliamos sobre el método anterior
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=10)
    #Para cada cara nos interesa detectar los ojos, por tanto los detectaremos para cada cara
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #De la imagen principal, sacamos la cara detectada (conocemos el rectangulo, por lo que podemos indexar para
        #(sacar la zona de interes)
        ROI_gray = grey[y:y+h,x:x+w]
        #La sacamos tambien en color
        ROI_colour = frame[y:y+h,x:x+w]
        #Llamamos a la clase de cascadas que detecta ojos y le pasamos la imagen en escala de gris
        eyes = eye_cascade.detectMultiScale(ROI_gray)
        #Ahora, para cada ojo detectado, le ponemos un rectangulo, igual que antes
        for (e_x,e_y,e_w,e_h) in eyes:
            cv.rectangle(ROI_colour, (e_x,e_y),(e_x+e_w,e_y+e_h),(0,0,255),2)

    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vcap.release()
cv.destroyAllWindows()
