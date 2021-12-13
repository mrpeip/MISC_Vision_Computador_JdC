import cv2 as cv
#Creamos una clase VideoCapture para grabar video
vcap = cv.VideoCapture(0)
"""
Los distintos codec de video que hay se pueden mirar aquí:
https://www.fourcc.org/codecs.php#letter_x
"""
fourcc = cv.VideoWriter_fourcc(*'XVID')
"""
Para almacenar el video llamamos a otra clase de OpenCV que se encarga de ello, a esta clase hay que pasarle
como parametros el nombre y formato del archivo, la codificacion fourcc, es decir, el codec que hemos delcarado en la
varible "fourcc" que tenemos antes. Despues le pasamos los fps que queremos y el tamaño, que se saca de las funciones
cv.CAP_PROP_FRAME_WITH y HEIGTH 
 """
vout = cv.VideoWriter('output.avi',fourcc,20.0,(640,480))

#Hacemos un bucle infinito para ir grabando sin parar frame a frame. Para ello podemos usar un while True, o podemos
#Usar un método de la clase VideoCapture que nos dice si la cámara está encendida (que es lo que muestro)
while(vcap.isOpened() == True):
    #vcap.read() devuelve True/False en función de si el frame está disponible, y lo almacenará en "ret". Si es True
    #Guardará el frame en la variable "frame"
    ret, frame = vcap.read()
    if ret == True:
        #Podemos extraer varios datos de la clase VideCapture que creamos usando la funcion "get", como por ejemplo:
        #Sacamos el ancho del frame:
        print(vcap.get(cv.CAP_PROP_FRAME_WIDTH))
        #La altura del frame
        print(vcap.get(cv.CAP_PROP_FRAME_HEIGHT))
        #Y los frames del video
        print(vcap.get(cv.CAP_PROP_POS_FRAMES))
        """ Todas las funciones que podemos hacer con el .get están en la siguiente URL:
        https://docs.opencv.org/4.0.0/d4/d15/group__videoio__flags__base.html#gaeb8dd9c89c10a5c63c139bf7c4f5704d
        """
        #Vamos a cambiar la imagen de color a gris
        #Para ello llamamos a la funcion cvtColor que nos deja cambiar la imagen ("frame") al color que digamos, !!USANDO UN METODO DE CV2!!
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        #Mostramos los frames
        cv.imshow('Frame',gray)

        #Guardamos el resultado con la clase VideoWriter, para cada frame
        vout.write(gray)

        #Si pulsamos "q" vamos a salirnos del loop
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
#Una vez fuera del loop, decimos que pare de grabar
vcap.release()
vout.release()
cv.destroyAllWindows()