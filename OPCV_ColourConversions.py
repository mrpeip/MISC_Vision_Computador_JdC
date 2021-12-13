import cv2 as cv

# Lectura de la imagen
img = cv.imread('Image&Video/colour.png')

# Canal rojo
red = img[:, :, 2]
# Canal verde
green = img[:, :, 1]
# Canal azul
blue = img[:, :, 0]

cv.imshow('Original', img)
cv.imshow('Rojo', red)
cv.imshow('Verde', green)
cv.imshow('Azul', blue)
cv.waitKey(0)
cv.destroyAllWindows()

# Conversión a HSV y extracción de parámetros
img_HSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
hue, sat, val = cv.split(img_HSV)
cv.imshow('Original', img)
cv.imshow('Hue', hue)
cv.imshow('Saturation', sat)
cv.imshow('Value', val)
cv.waitKey(0)
cv.destroyAllWindows()

# Conversión a HSI y extracción de parámetros
img_HSI = cv.cvtColor(img, cv.COLOR_BGR2HLS)
hue, sat, inten = cv.split(img_HSV)
cv.imshow('Original', img)
cv.imshow('Hue', hue)
cv.imshow('Saturation', sat)
cv.imshow('Intensity', inten)
cv.waitKey(0)
cv.destroyAllWindows()

#Comparativa entre HSV y HSI
cv.imshow('HSV', img_HSV)
cv.imshow('HSI', img_HSI)
cv.waitKey(0)
cv.destroyAllWindows()