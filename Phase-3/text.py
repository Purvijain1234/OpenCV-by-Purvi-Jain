import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\Image1.png")

if img is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")


text = "I am Purvi Jain"

# Put text: (img, text, org(x,y), font, fontScale, color, thickness)
cv.putText(img, text, (130,40), cv.FONT_HERSHEY_SIMPLEX , 1.2, (255, 0, 0) , 2)

cv.imshow("Text", img)
cv.waitKey(0)
cv.destroyAllWindows()