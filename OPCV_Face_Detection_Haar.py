import cv2 as cv
import numpy as np

"""
El clasificador en cascada Haar es una herramienta de machine learning. Una función de cascada es entrenada para
un montón de imagenes "positivas" y "negativas". Esto funciona primero entrenando al clasificador con un par de cientos
de imágenes del objeto a detectar (caras, coches, etc) escalados al mismo tamaño (20x20,100x100 etc); estas son las 
imágenes positivas. Se añaden también imágenes arbitrareas (que no tengan el objeto a detectar) de otras cosas 
escaladas a ese tamaño (que son las imágenes negativas). Es decir, lo más importante es entrenar al clasificador 
para lo que se quiera detectar. 
El clasificador devuelve un 1 si cree que lo que se le ha pasado es una cara y 0 si no.
"""

#OpenCV incluye un "trainer" y un detector.
"""
En el github de OpenCV se pueden encontrar archivos XML con clasificadores entrenados:
https://github.com/opencv/opencv/tree/master/data/haarcascades
"""
#Llamo a la clase del clasificador y le paso el xml ya entrenado para caras
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

#Cargo una imagen de una cara:
img = cv.imread('Image&Video/Faces.jpg')
#La paso a gris
grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#Vamos a usar un metodo del clasificador para detectar si hay una cara. Los parámetros que se usan son:
"""
faces = Vector de rectángulos donde cada rectángulo contiene el objeto detectado.
image = Matriz de tipo CV_8U de la imagen a detectar
scaleFactor = Factor que indica cuanto se reduce el tamaño de la imagen en cada escalado.
minNeihgbours = Parametros que especifica cuantos vecinos debe tener cada rectangulo candidato para ser considerado
"""
faces = face_cascade.detectMultiScale(grey,scaleFactor=1.1, minNeighbors=4)
#Debemos sacar los rectángulos que ha detectado y almacenado en faces
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

cv.imshow('Faces',img)
cv.waitKey(0)
cv.destroyAllWindows()

"""
De manera adiccional esto se puede realizar sobre un video:
"""
vcap = cv.VideoCapture(0)
while vcap.isOpened():
    _,frame = vcap.read()
    grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=6)
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
    cv.imshow('Video', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vcap.release()
cv.destroyAllWindows()
