import cv2 as cv
from timeit import default_timer as timer

img = cv.imread('Image&Video/aero1.jpg')
# Ampliar la imagen de 640x480 a 1280x720

# Interpolación por vecino más cercano
start = timer()
nearest = cv.resize(img, (1280, 720), interpolation=cv.INTER_NEAREST)
end = timer()
print(end - start)
# Interpolación lineal
start = timer()
lineal = cv.resize(img, (1280, 720), interpolation=cv.INTER_LINEAR)
end = timer()
print(end - start)
# Interpolación bicúbica
start = timer()
cubic = cv.resize(img, (1280, 720), interpolation=cv.INTER_CUBIC)
end = timer()
print(end - start)

# Mostrar imágenes
cv.imshow('Vecino', nearest)
cv.imshow('Lineal', lineal)
cv.imshow('Bicúbica', cubic)

# Cerrar ventanas
cv.waitKey(0)
cv.destroyAllWindows()

# Reducir la imagen de 640x480 a 128x128

# Interpolación por vecino más cercano
start = timer()
nearest = cv.resize(img, (256, 256), interpolation=cv.INTER_NEAREST)
end = timer()
print(end - start)
# Interpolación lineal
start = timer()
lineal = cv.resize(img, (256, 256), interpolation=cv.INTER_LINEAR)
end = timer()
print(end - start)
# Interpolación bicúbica
start = timer()
cubic = cv.resize(img, (256, 256), interpolation=cv.INTER_CUBIC)
end = timer()
print(end - start)

# Mostrar imágenes
cv.imshow('Vecino', nearest)
cv.imshow('Lineal', lineal)
cv.imshow('Bicúbica', cubic)

# Cerrar ventanas
cv.waitKey(0)
cv.destroyAllWindows()