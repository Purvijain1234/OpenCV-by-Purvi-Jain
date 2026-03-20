import cv2 as cv

# Read
img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image Loaded Successfully.")
    
# Crop
cropped = img[100:200 , 100:300] #[y1:y2, x1:x2]

# show
cv.imshow("Image", img)
cv.imshow("Cropped image", cropped)

cv.waitKey(0)
cv.destroyAllWindows