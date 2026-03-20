import cv2 as cv

img = cv.imread(r"C:\Programming\Open CV\shape.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

_, thresh = cv.threshold(gray, 240, 255, cv.THRESH_BINARY)

# Find contours
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# detection
for contour in contours:
  approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour , True), True)
  corners = len(approx)
  
  if corners == 3:
    shape_name = "Triangle"
    
  elif corners == 4:
    shape_name = "Rectangle"
    
  elif corners == 5:
    shape_name = "Pentagon"
    
  elif corners > 5:
    shape_name = "Circle"

  else:
    shape_name = "Unknown"
    
cv.drawContours(img, [approx], 0, (0,0,255), 2)
x = approx.ravel()[0]
y = approx.ravel()[1] 
cv.putText(img, shape_name, (x,y), cv.FONT_HERSHEY_COMPLEX, 0.6 , (255,0,0), 2)   


cv.imshow("Contours", img)
cv.waitKey(0)
cv.destroyAllWindows()