import cv2 as cv

img = cv.imread('Image&Video/starry_night.jpg')

rot = cv.rotate(img,cv.ROTATE_90_CLOCKWISE)

cv.imshow('90º',rot)
cv.waitKey(0)
cv.destroyAllWindows()