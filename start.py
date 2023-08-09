import cv2 
image = cv2.imread('C:\project 1\dhoni.jpg')
gray_filter = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gray_filter)
blur = cv2.GaussianBlur(invert, (21,21),0)
invertedblur = cv2.bitwise_not(blur)

sketch_filter = cv2.divide(gray_filter, invertedblur,scale=256.0)
cv2.imwrite("PRINT.jpg",sketch_filter)
cv2.imshow(sketch_filter)