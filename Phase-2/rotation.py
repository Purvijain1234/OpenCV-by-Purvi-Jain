import cv2 as cv

# read
img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image Loaded Successfully.")
    
# rotation
(h, w) = img.shape[:2]
center = (w//2, h//2)
M = cv.getRotationMatrix2D(center, 90, 1.0)
rotated = cv.warpAffine(img, M, (w, h))

# show
cv.imshow("Original ", img)
cv.imshow("Rotated", rotated)
cv.waitKey(0)
cv.destroyAllWindows