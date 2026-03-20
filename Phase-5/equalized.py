import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
equalized = cv.equalizeHist(gray)

cv.imshow("Gray", gray)
cv.imshow("Equalized", equalized)
cv.waitKey(0)
cv.destroyAllWindows()
