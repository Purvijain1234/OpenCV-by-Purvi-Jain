import cv2 as cv

# Read
img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image Loaded Successfully.")
    
# Resize
resize = cv.resize(img, (300,300))

# Show
cv.imshow("Image", img)
cv.imshow("Resize", resize)

cv.waitKey(0)
cv.destroyAllWindows