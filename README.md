# Computer Vision with OpenCV - by Purvi Jain

A structured, phase-by-phase repository for learning **Computer Vision using OpenCV** in Python — from basic image operations to real-world projects like Face Detection, Sketchify, and Image Processing.

---

## 📁 Repository Structure

```
computer-vision-by-purvi-jain/
│
├── Phase-1/                          # Basic Image Operations
│   ├── dimension.py
│   ├── displaying.py
│   ├── grayscale.py
│   ├── loading.py
│   └── saving.py
│
├── Phase-2/                          # Image Transformations
│   ├── Crop.py
│   ├── Flip.py
│   ├── resize.py
│   └── rotation.py
│
├── Phase-3/                          # Drawing on Images
│   ├── circle.py
│   ├── line.py
│   ├── rectangle.py
│   └── text.py
│
├── Phase-4/                          # Video Operations
│   ├── gray_video.py
│   ├── save_video.py
│   └── video_capture.py
│
├── Phase-5/                          # Image Filtering & Blurring
│   ├── bilateral.py
│   ├── equalized.py
│   ├── gaussian_blur.py
│   ├── median_blur.py
│   └── sharpening.py
│
├── Phase-6/                          # Edge Detection & Thresholding
│   ├── bitwise.py
│   ├── canny_edge.py
│   └── threshold_func.py
│
├── Phase-7/                          # Contours
│   ├── contours.py
│   ├── detection.py
│   └── draw_contours.py
│
├── OpenCV_Projects/
│   ├── Face_Detection/
│   ├── Image_Processing_Project/
│   └── Sketchify/
│
├── requirement.txt
└── README.md
```

---

## 📚 Contents Overview

### 🔹 Phase 1 — Basic Image Operations
Getting started with OpenCV — loading, displaying, and saving images.

| File | Description |
|------|-------------|
| `OpencvImageOperations.py` | Overview of core OpenCV image operations |
| `loading.py` | Load an image using `cv2.imread()` |
| `displaying.py` | Display images using `cv2.imshow()` |
| `saving.py` | Save processed images using `cv2.imwrite()` |
| `grayscale.py` | Convert images to grayscale |
| `dimension.py` | Get image shape, size, and data type |

---

### 🔹 Phase 2 — Image Transformations
Geometric transformations applied to images.

| File | Description |
|------|-------------|
| `Crop.py` | Crop a region of interest from an image |
| `Flip.py` | Flip images horizontally, vertically, or both |
| `resize.py` | Resize images to custom dimensions |
| `rotation.py` | Rotate images by a given angle |

---

### 🔹 Phase 3 — Drawing on Images
Drawing shapes and text directly on images using OpenCV.

| File | Description |
|------|-------------|
| `line.py` | Draw lines on images |
| `rectangle.py` | Draw rectangles |
| `circle.py` | Draw circles |
| `text.py` | Put text on images using `cv2.putText()` |

---

### 🔹 Phase 4 — Video Operations
Working with video streams and saving video output.

| File | Description |
|------|-------------|
| `video_capture.py` | Capture live video from webcam |
| `gray_video.py` | Convert live video feed to grayscale |
| `save_video.py` | Record and save video to a file |

---

### 🔹 Phase 5 — Image Filtering & Blurring
Noise removal and image enhancement using various filters.

| File | Description |
|------|-------------|
| `gaussian_blur.py` | Apply Gaussian blur to smooth images |
| `median_blur.py` | Median filter for salt-and-pepper noise |
| `bilateral.py` | Edge-preserving bilateral filter |
| `sharpening.py` | Sharpen images using kernel convolution |
| `equalized.py` | Histogram equalization for contrast enhancement |

---

### 🔹 Phase 6 — Edge Detection & Thresholding
Detecting edges and applying binary thresholding techniques.

| File | Description |
|------|-------------|
| `canny_edge.py` | Canny edge detection algorithm |
| `threshold_func.py` | Simple, adaptive & Otsu thresholding |
| `bitwise.py` | Bitwise operations (AND, OR, NOT, XOR) on images |

---

### 🔹 Phase 7 — Contours
Finding and drawing contours for shape analysis and object detection.

| File | Description |
|------|-------------|
| `contours.py` | Find contours using `cv2.findContours()` |
| `draw_contours.py` | Draw detected contours on images |
| `detection.py` | Object detection using contour analysis |

---

### 🔹 OpenCV Projects
End-to-end computer vision projects applying all the above concepts.

| Project | Description | Status |
|---------|-------------|--------|
| 👤 `Face_Detection` | Detects faces in images/video using Haar Cascades | ✅ Complete |
| 🖼️ `Image_Processing_Project` | A combined image processing pipeline | ✅ Complete |
| ✏️ `Sketchify` | Converts a photo into a pencil sketch effect | ✅ Complete |
| 🔜 More projects... | Object Tracking, Background Subtraction, and more | 🚧 Coming Soon |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Purvijain1234/OpenCV-by-Purvi-Jain.git
cd OpenCV-by-Purvi-Jain
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate        # On Mac/Linux
venv\Scripts\activate           # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

---

## 🛠️ Requirements

```
opencv-python
numpy
matplotlib
```

> Install all at once: `pip install -r requirement.txt`

---

## 🗺️ Learning Path

Follow this phase-by-phase order for the best learning experience:

```
Phase-1 → Phase-2 → Phase-3 → Phase-4 → Phase-5 → Phase-6 → Phase-7 → Projects
```

Each phase builds on the previous one, giving you a strong OpenCV foundation before tackling real projects.

---

## 🚀 Future Plans

- [ ] Phase-8: Morphological Operations
- [ ] Phase-9: Feature Detection (SIFT, ORB)
- [ ] Phase-10: Object Tracking
- [ ] More Projects (Background Subtraction, Lane Detection, Motion Detection)

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or suggestions
- Submit a pull request with new phases or projects
- Star ⭐ the repo if you find it helpful!

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---
