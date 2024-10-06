import cv2 as cv

img = cv.imread('resources/Photos/group 1.jpg')
cv.imshow('Persons', img)

# convert it to grayscale as face detection does not involve color
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Persons', gray)

# let's read the haar cascade classifier xml file
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# detect faces (inc minNeighbors is for increasing accuracy but dec will increase sensitivity to noise)
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)
print(f'Number of faces found = {len(faces_rect)}')

# draw rectangles around the faces
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)