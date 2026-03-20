import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")

# Draw line: (img, pt1, pt2, color(BGR), thickness)
cv.line(img, (50, 50), (400, 50), (255, 0, 0), 3)


cv.imshow("Line", img)
cv.waitKey(0)
cv.destroyAllWindows()