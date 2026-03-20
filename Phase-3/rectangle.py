import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")

# Draw rectangle: (img, pt1, pt2, color(BGR), thickness)
cv.rectangle(img, (100, 100), (300, 300), (0, 0, 255), 3)

# For filled rectangle use thickness = -1
cv.rectangle(img, (350, 100), (450, 200), (255, 0, 0), -1)

cv.imshow("Rectangle", img)
cv.waitKey(0)
cv.destroyAllWindows()