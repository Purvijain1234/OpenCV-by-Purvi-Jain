import cv2

image = cv2.imread(r"C:\Programming\Open CV\Image1.png")

if image is not None:
    h, w, c = image.shape
    print(f"Image Loaded :\nHeight: {h}\nWidth: {w} \nChannels: {c}")
else:
    print("Error: Image not Found")