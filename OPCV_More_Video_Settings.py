import cv2 as cv
import datetime
#Partiendo de el ejemplo de captura de imagen de antes
vcap = cv.VideoCapture(0)
#NOTA: Cada propiedad (lo de CAP_PROP...) tiene asignado un número para mas sencillez
print(vcap.get(cv.CAP_PROP_FRAME_HEIGHT))
print(vcap.get(cv.CAP_PROP_FRAME_WIDTH))
#Podemos modificar parámetros del video, aqui vamos a cambiar el ancho(3) y el alto(4) y mostrarlos (pero hay muchos más)
vcap.set(3,1208)
vcap.set(4,720)
print(vcap.get(3))
print(vcap.get(4))
"""
Vamos a añadir texto e imágenes a un video, se usan los mismos parámetros que en el ejemplo de imáagenes
"""
while(vcap.isOpened()):
    ret,frame = vcap.read()
    if ret == True:
        #Mostramos el alto y en ancho del video
        font = cv.FONT_HERSHEY_COMPLEX_SMALL
        text = 'Ancho: '+str(vcap.get(3)) + ' '+'Alto: '+str(vcap.get(4))
        cv.putText(frame,text,(10,50),font,1,(255,255,255),3)
        #Ahora vamos a mostrar la fecha y hora en el video
        date_t = str(datetime.datetime.now())
        cv.putText(frame,date_t,(255,255),font,2,(255,255,255),2)
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow('frame',frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
vcap.release()
cv.destroyAllWindows()
