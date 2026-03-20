import cv2 as cv

# Open webcam (0 = default camera, 1 = external webcam)
capture = cv.VideoCapture(0)

while True:
  ret, frame = capture.read()
  
  if not ret:
      print("Error: Not found.")
      break
    
  cv.imshow("Webcam ", frame)
    
# Press 'q' to exit
  if cv.waitKey(1) & 0xFF == ord('q'):
    print("Quitting....")
    break

capture.release()
cv.destroyAllWindows()

