import cv2 as cv

capture = cv.VideoCapture(0)

while True:
  ret, frame = capture.read()
  
  if not ret:
    break
  
  #Convert to grayscale
  gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
  
  cv.imshow("Gray Video", gray)
  
  if cv.waitKey(1) & 0xFF == ord('q'):
      break

capture.release()
cv.destroyAllWindows()