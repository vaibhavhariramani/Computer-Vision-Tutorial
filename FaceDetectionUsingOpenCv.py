## importing libraries
import cv2

## Load the cascade
face_cascade = cv2.cascadeClassifier('haarcascade_frontalface_default.xml')

## Read the input image
img = cv2.imread('test.jpg')

## Convert the image into grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

## Detect faces
faces = face_cascade.detectMultiscale(gray,1.1,4)

## Draw rectangle around the face
for(x,y,w,h) in faces:
  cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
  
## Show the output
cv2.imshow('output.jpg',img)
cv2.waitkey()
