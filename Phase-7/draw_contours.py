import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\shape.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# draw contours
for contour in contours:
    cv.drawContours(img, contours, -1, (0,0,255), 3)

cv.imshow("Contours", img)
cv.waitKey(0)
cv.destroyAllWindows()