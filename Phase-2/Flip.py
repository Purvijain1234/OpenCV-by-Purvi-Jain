import cv2 as cv

# Read
img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image Loaded Successfully.")

# Flip
flip_h = cv.flip(img, 1)
flip_v = cv.flip(img, 0)
flip_b = cv.flip(img , -1)


# Show
cv.imshow("Image", img)
cv.imshow("Flip Horizontal ", flip_h)
cv.imshow("Flip Vertical ", flip_v)
cv.imshow("Flip both", flip_b)

cv.waitKey(0)
cv.destroyAllWindows