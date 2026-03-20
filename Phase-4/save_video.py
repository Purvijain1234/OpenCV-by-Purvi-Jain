import cv2 as cv

camera = cv.VideoCapture(0)

frame_width = int(camera.get(cv.CAP_PROP_FRAME_WIDTH))
frame_height = int(camera.get(cv.CAP_PROP_FRAME_HEIGHT))

codec = cv.VideoWriter_fourcc(*'XVID')
recorded = cv.VideoWriter("VideoSave.avi", codec, 20, (frame_width, frame_height))

while True:
  success, image = camera.read()
  
  if not success:
    break
  
  recorded.write(image)
  cv.imshow("Recording Live", image)
  
  # Press 'q' to exit
  if cv.waitKey(1) & 0xFF == ord('q'):
    break

camera.release()
recorded.release()
cv.destroyAllWindows()