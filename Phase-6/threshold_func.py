# Canny Edge Detection
import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

ret, thresh_img = cv.threshold(gray, 120, 255, cv.THRESH_BINARY)

cv.imshow("Original", img)
cv.imshow("Gray", gray)
cv.imshow("Threshold image", thresh_img)

cv.waitKey(0)
cv.destroyAllWindows()