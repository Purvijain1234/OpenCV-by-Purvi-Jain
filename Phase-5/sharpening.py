import cv2 as cv
import numpy as np

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

 
# Sharpening kernel (kernel means 3x3 matrix)
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

sharpened = cv.filter2D(img, -1, kernel)

cv.imshow("Sharpened", sharpened)
cv.waitKey(0)
cv.destroyAllWindows()