import cv2 as cv
#Read an image in grayscale (0)
img = cv.imread('Image&Video/lena.jpg',0)
cv.imshow('image',img)
#If you press Esc it closes without saving, if you press "s" it saves the image
key = cv.waitKey(0)
if key == 27:
    cv.destroyAllWindows()
elif key == ord('s'):
    #Write the grayscale image
    cv.imwrite('lena_gray.png',img)
    cv.destroyAllWindows()
