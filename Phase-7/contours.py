import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\shape.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

print("Number of contours found:", len(contours))

cv.imshow("Threshold", thresh)
# cv.imshow("Contours", img)
cv.waitKey(0)
cv.destroyAllWindows()