import cv2 as cv

# Load Haar Cascade classifiers
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')
smile_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_smile.xml')

capture = cv.VideoCapture(0)

while True:
  ret, frame = capture.read()
  
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

# Detect faces
  faces = face_cascade.detectMultiScale(gray, 1.3, 5)

  for (x, y, w, h) in faces:
    cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  # Blue face box

# Show result
  cv.imshow("Webcam Face Detection", frame)
  
  if cv.waitKey(1) & 0xFF == ord('q'):
    break
  
capture.release()
cv.destroyAllWindows()