import cv2

# ---------IMAGE OPERATIONS---------

# loading
def load_image(path):
    img = cv2.imread(path)
    return image

# display 
def display(Window_name, image):
    cv2.imshow(Window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# saving
def save_image(filename, image):
    cv2.imwrite(filename, image)
    print(f"Image saved as '{filename}'")

# dimension
def dimensions(image):
     h, w, c = image.shape
     print(f"Image Dimension: \nHeight : {h} \nWidth : {w} \nChannels : {c}")

# grayscale
def to_grayscale(image):
     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     display("Grayscale Image", gray)
     return gray


# ---------MAIN PROGRAM---------

path = r"C:\Programming\Open CV\Image.png" # path to the image
image = cv2.imread(r"Phase 1\Image.png") # read the image

choose = int(input(
        "Choose an option:\n"
        "1. Load Image\n"
        "2. Display Image\n"
        "3. Save Image\n"
        "4. Image Dimensions\n"
        "5. Convert to Grayscale\n"
    ))

if choose == 1:
    img = load_image(path)
    print("Image Loaded")
elif choose == 2:
    display("Image", image)
elif choose == 3:
    save_image("saved_image.png", image)
    print("Image Saved as 'saved_image.png'")
elif choose == 4:
    dimensions(image)
elif choose == 5:
    gray_image = to_grayscale(image)
else:
    print("Invalid Option")
