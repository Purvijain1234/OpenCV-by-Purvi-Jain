import cv2 as cv
import numpy as np

# Create two shapes
img1 = np.zeros((300,300), dtype="uint8")
img2 = np.zeros((300,300), dtype="uint8")

cv.rectangle(img1, (50,50), (250,250), 255, -1)
cv.circle(img2, (150,150), 100, 255, -1)

# Bitwise operations
bit_and = cv.bitwise_and(img1, img2)
bit_or  = cv.bitwise_or(img1, img2)
bit_xor = cv.bitwise_xor(img1, img2)
bit_not = cv.bitwise_not(img1)

cv.imshow("Rectangle", img1)
cv.imshow("Circle", img2)
cv.imshow("AND", bit_and)
cv.imshow("OR", bit_or)
cv.imshow("XOR", bit_xor)
cv.imshow("NOT (Rectangle)", bit_not)

cv.waitKey(0)
cv.destroyAllWindows()
