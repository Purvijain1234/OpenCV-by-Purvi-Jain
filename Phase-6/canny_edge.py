# Canny Edge Detection
import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Canny: (image, threshold1, threshold2)
edge = cv.Canny(gray, 50, 150 )

cv.imshow("Original", img)
cv.imshow("Gray", gray)
cv.imshow("Canny Edges", edge)
cv.waitKey(0)
cv.destroyAllWindows()