import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")

# Draw circle: (img, center, radius, color, thickness)
cv.circle(img, (350, 350), 100, (255, 255, 255), 3)

# Filled
cv.circle(img, (100, 100), 50, (0, 255, 255), -1)


cv.imshow("Circle", img)
cv.waitKey(0)
cv.destroyAllWindows()