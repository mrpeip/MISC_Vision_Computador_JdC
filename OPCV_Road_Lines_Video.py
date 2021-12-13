import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

"""
Se va a usar un código practicamente igual al anterior, pero más estructurado, las funciones irán arriba del todo
y el codigo principal se definirá en una funcion
"""
def ROI(img,vertices):
    #Comenzamos definiendo una matriz de ceros de tamaño igual a la altura y anchura de la imagen. Esta matriz
    #de ceros se va a encargar de ocultar (poner en negro) todo lo que NO nos interese
    mask = np.zeros_like(img)
    #Creamos una máscara que coincida con los grises
    match_mask_colour = 255
    #Vamos a rellenar el polígono que forma la ROI
    cv.fillPoly(mask, vertices, match_mask_colour)
    #Vamos a devolver la imagen sólo donde la imagen coincida con la máscara que representa nuestra ROI
    # (O sea se, vamos a devolver la imagen solo con lo que nos interesa
    masked_image = cv.bitwise_and(img, mask)
    return masked_image

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

def line_detection(frame):
    print(frame.shape)
    # Nos devuelve un tuple "(630, 1200, 3)" con la altura, la anchura, y los canales
    height = frame.shape[0]
    width = frame.shape[1]
    # Sacamos a partir de los valores de la imagen definimos la ROI. Vamos a coger un triagulo en la zona
    #  derecha de la imagen. Los puntos que cojo son: bottom-un poco menos del centro (en matplotlib la altura empieza
    #  en el max), centro y bottom-right. ESTAMOS BUSCANDO SACAR EL CARRIL DERECHO, POR ESO ESOS NUMEROS (2.5)
    ROI_vertices = [(0, height), (width / 2, height / 2), (width, height)]
    # Comenzamos pasando la imagen a gris
    grey_road = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # A la imagen en gris le aplicamos Canny para sacar los borders
    canny_road_edges = cv.Canny(grey_road, 100, 120)
    cropped_road = ROI(canny_road_edges, np.array([ROI_vertices], np.int32))
    # Hay que toquetear un poco los parámetros para ajustar
    lines = cv.HoughLinesP(cropped_road, rho=2, theta=np.pi / 180, threshold=50, lines=np.array([]), minLineLength=40,
                           maxLineGap=100)
    road_with_lines = draw_lines(frame, lines)
    return road_with_lines

#Cargo el video
road_vcap = cv.VideoCapture('road.mp4')

#Vamos a comprobar si el frame está disponible
while(road_vcap.isOpened()):
    ret, frame = road_vcap.read()
    #Aplico la detección de lineas
    
    frame = line_detection(frame)
    print(frame)
    cv.imshow('Road',frame)
    if cv.waitKey(1) & 0xff == ord('q'):
        break

road_vcap.release()
cv.destroyAllWindows()