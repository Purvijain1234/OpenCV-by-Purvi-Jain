import cv2

image = cv2.imread(r"C:\Programming\Open CV\Image1.png")

if image is None:
    print("Error: Image not found.")
else:
    print("Image loaded successfully.")