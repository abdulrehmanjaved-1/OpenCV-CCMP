import cv2 as cv

img = cv.imread('resources/Photos/cats.jpg')

cv.imshow('cats', img)

#covert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

cv.waitKey(0)