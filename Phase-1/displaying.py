import cv2

image = cv2.imread(r"C:\Programming\Open CV\Image1.png")

if image is not None:
    cv2.imshow("Image Showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Coudn't load the image.")