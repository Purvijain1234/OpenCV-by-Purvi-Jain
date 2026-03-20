import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

median = cv.medianBlur(img, 5)  # Kernel size must be odd

cv.imshow("Original", img)
cv.imshow("Median Blur", median)
cv.waitKey(0)
cv.destroyAllWindows()