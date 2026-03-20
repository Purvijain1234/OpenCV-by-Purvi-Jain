import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

# Bilateral filter: (image, diameter, sigmaColor, sigmaSpace)
smooth = cv.bilateralFilter(img, 9, 75, 75)


cv.imshow("Bilateral Filter", smooth)
cv.waitKey(0)
cv.destroyAllWindows()
