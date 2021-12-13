import cv2 as cv
import numpy as np
from matplotlib import  pyplot as plt
"""
Vamos a detectar las lineas de una carretera. Primero lo haremos con una imagen estática, y luego con un vídeo
"""
road = cv.imread('Image&Video/road.jpg')
#Pasamos la imagen de BGR a RGB porque vamos a trabajar con Matplotlib
road = cv.cvtColor(road, cv.COLOR_BGR2RGB)

"""
Debemos definir nuestra ROI (Region of Interest) ya que no nos interesa detectar todas las lineas, solo la del carril
"""
#Vamos a ver la forma de la imagen
print(road.shape)
#Nos devuelve un tuple "(630, 1200, 3)" con la altura, la anchura, y los canales
height = road.shape[0]
width = road.shape[1]
#Sacamos a partir de los valores de la imagen definimos la ROI. Vamos a coger un triagulo en la zona
#  derecha de la imagen. Los puntos que cojo son: bottom-un poco menos del centro (en matplotlib la altura empieza
#  en el max), centro y bottom-right. ESTAMOS BUSCANDO SACAR EL CARRIL DERECHO, POR ESO ESOS NUMEROS (2.5)
ROI_vertices = [(width/2.5, height),(width/2,height/2),(width,height)]
"""
--------------- VER CODIGO MAS ABAJO, ESTO LO HAGO PARA ELIMINAR LOS BORDES DE LA ROI DE CANNY ------------
Al usar la imagen original para sacar los bordes mediante Canny, me va a detectar el triangulo de la ROI como un 
borde, con el fin de evitar eso, vamos a aplicar Canny a la imagen original sin ROI para luego detectar el ROI en Canny
en lugar de en la imagen original
"""
#Comenzamos pasando la imagen a gris
grey_road = cv.cvtColor(road, cv.COLOR_BGR2GRAY)
#A la imagen en gris le aplicamos Canny para sacar los borders
canny_road_edges = cv.Canny(grey_road, 100, 200)


#Vamos a definir una funcion para ocultar todo lo que no sea nuestra ROI, o sea, sacar la ROI y ocultar el resto
def ROI(img,vertices):
    #Comenzamos definiendo una matriz de ceros de tamaño igual a la altura y anchura de la imagen. Esta matriz
    #de ceros se va a encargar de ocultar (poner en negro) todo lo que NO nos interese
    mask = np.zeros_like(img)
    """
    #Sacamos los canales de la imagen
    channel_count = img.shape[2]
    #Creamos una mascara que coincida con los colores
    match_mask_colour = (255,)*channel_count
    ESTE CODIGO YA NO APLICA PORQUE AHORA TRABAJAMOS CON EL RESULTADO DEL CANNY DE LA IMAGEN, NO CON LA IMAGEN
    RGB ORIGINAL. ENTONCES NO HAY CANALES, PORQUE ES BLANCO Y NEGRO
    """
    #Creamos una máscara que coincida con los grises
    match_mask_colour = 255
    #Vamos a rellenar el polígono que forma la ROI
    cv.fillPoly(mask, vertices, match_mask_colour)
    #Vamos a devolver la imagen sólo donde la imagen coincida con la máscara que representa nuestra ROI
    # (O sea se, vamos a devolver la imagen solo con lo que nos interesa
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

"""
Ahora aplicamos la función a nuestra imagen
"""
cropped_road = ROI(canny_road_edges,np.array([ROI_vertices], np.int32))

"""
Ahora vamos usar Hough para detectar las lineas en nuestra ROI.
"""
"""
#Comenzamos pasando la imagen a gris
grey_cropped_road = cv.cvtColor(cropped_road, cv.COLOR_BGR2GRAY)
#A la imagen en gris le aplicamos Canny para sacar los borders
#canny_edges = cv.Canny(grey_cropped_road, 100, 200)
ESTE CODIGO YA NO APLICA, PORQUE AHORA APLICAMOS LA ROI AL CANNY DE LA IMAGEN ORIGINAL, EN VEZ DE APLICAR EL ROI
A LA IMAGEN ORIGINAL Y LUEGO CANNY, PORQUE MARCA EL TRIANGULO DE LA ROI COMO UN BORDE Y ESO NO NOS INTERESA
"""

#Hay que toquetear un poco los parámetros para ajustar
lines = cv.HoughLinesP(cropped_road,rho=6,theta=np.pi/60,threshold=150,lines=np.array([]), minLineLength= 40, maxLineGap= 25)

#Vamos a crear otra función que se encargará de dibujar las lineas de Hough
def draw_lines(img, lines):
    #Copio la imagen (para no modificar)
    img_copy = np.copy(img)
    #Ahora voy a crear una imagen vacía que tenga las mismas dimensiones que la original, para eso uso shape
    #y saco la altura, la anchura y los canales.
    blank_image = np.zeros((img_copy.shape[0], img_copy.shape[1], img_copy.shape[2]), dtype= np.uint8)
    #Ahora vamos a hacer un loop alrededor de los vectores de linea
    for line in lines:
        #Y para cada linea, la dibujamos en la matriz de lineas, porque luego las vamos a unir
        for x1,y1,x2,y2 in line:
            cv.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=5)
    #Unimos las lineas que hemos dibujado con la imagen original
    img = cv.addWeighted(img,0.8,blank_image, beta=1,gamma=0)
    return img

"""
Ahora dibujamos las lineas en la imagen usando la funcion que hemos definido
"""
road_with_lines = draw_lines(road,lines)
#Cargamos la imagen con matplotlib
plt.imshow(road_with_lines)
plt.show()

