import cv2 as cv
from matplotlib import pyplot as plt
"""
Matplotlib da bastantes ventajas frente a la manera que OpenCV muestra imagenes, como poder guardarlas,
ampliar, ver coordenadas directamente, etc
"""

img  = cv.imread('Image&Video/lena.jpg',0)
cv.imshow('img',img)

#Es importante darse cuenta de que OpenCV lee la imagen en formato BGR mientras que Matplotlib lo hace en
#RGB, por tanto es necesario convertir la imagen para que Matplotlib lo muestre bien
img2 = cv.cvtColor(img,cv.COLOR_BGR2RGB)
plt.imshow(img2)
#Con xticks o yticks puede configurar los ejes, si dejo el array en blanco sale sin ejes
plt.xticks([]),plt.yticks([])

"""
Vamos a juntar varias imagenes en una única ventana de matplotlib
"""

#Media
th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)

#Media Gaussiana
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)

#Definimos las imagenes que vamos a mostrar y los titulos como arrays
images = [img,th2,th3]
titles = ['Original','Mean_C','Gauss']

#Vamos a fusionar las imagenes con un bucle for
for i in range(3):
    #Los argumentos para subplot son: nºfilas, nºcolumnas, índice de la imagen
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()



cv.waitKey(0)
cv.destroyAllWindows()