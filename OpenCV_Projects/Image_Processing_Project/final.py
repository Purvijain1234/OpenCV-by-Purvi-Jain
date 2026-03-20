import cv2 as cv
import numpy as np

# Load Image
img = cv.imread(r"C:\Programming\Open CV\Image.png")
img = cv.resize(img, (500, 300))

if img is None:
    print("Error: Image not found.")
    exit()
else:
    print("Image Loaded Successfully!")

def show_image(window, image):
    cv.imshow(window, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

def menu():
    print("\n---------- Image Processing Menu ----------")
    print("1. Show Image Information")
    print("2. Convert to Grayscale")
    print("3. Resize Image")
    print("4. Crop Image")
    print("5. Flip Image")
    print("6. Rotate Image")
    print("7. Blur (Gaussian)")
    print("8. Sharpen Image")
    print("9. Edge Detection (Canny)")
    print("10. Exit")
    choice = int(input("Enter your choice: "))
    return choice

while True:
    choice = menu()
    
    if choice == 1:
        h, w, c = img.shape
        print(f"Height: {h}, Width: {w}, Channels: {c}")
        show_image("Original", img)

    elif choice == 2:
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        show_image("Grayscale", gray)

    elif choice == 3:
        resized = cv.resize(img, (400, 200))
        show_image("Resized", resized)

    elif choice == 4:
        cropped = img[100:300, 100:400]
        show_image("Cropped", cropped)

    elif choice == 5:
        flip_h = cv.flip(img, 1)
        flip_v = cv.flip(img, 0)
        flip_b = cv.flip(img, -1)
        cv.imshow("Flip Horizontal", flip_h)
        cv.imshow("Flip Vertical", flip_v)
        cv.imshow("Flip Both", flip_b)
        cv.waitKey(0)
        cv.destroyAllWindows()

    elif choice == 6:
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv.getRotationMatrix2D(center, 90, 1.0)
        rotated = cv.warpAffine(img, M, (w, h))
        show_image("Rotated", rotated)

    elif choice == 7:
        gaussian = cv.GaussianBlur(img, (7, 7), 0)
        show_image("Gaussian Blur", gaussian)

    elif choice == 8:
        kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])
        sharpened = cv.filter2D(img, -1, kernel)
        show_image("Sharpened", sharpened)

    elif choice == 9:
        edges = cv.Canny(img, 100, 200)
        show_image("Edges", edges)

    elif choice == 10:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
