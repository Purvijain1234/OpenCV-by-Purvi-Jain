import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

# Gaussian Blur: (image, kernel_size, sigmaX)
gaussian = cv.GaussianBlur(img, (7, 7), 0)

cv.imshow("Original", img)
cv.imshow("Gaussian Blur", gaussian)
cv.waitKey(0)
cv.destroyAllWindows()