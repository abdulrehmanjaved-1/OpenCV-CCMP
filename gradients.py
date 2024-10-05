import cv2 as cv
import numpy as np

img=cv.imread('resources/Photos/park.jpg')
cv.imshow('Boston',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian (less common)
lap = cv.Laplacian(gray, cv.CV_64F) #cv.CV_64F means 64 bit floating point bcz it can be negative
lap = np.uint8(np.absolute(lap)) #as lap can be negative value too as change in intensities into whote and black are negative and post9ove slopes, that's why making it absolute.
cv.imshow('Laplacian', lap)

# Sobel (sobel computes gradients in both x and y direction)
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely) #merging the two gradients

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel', combined_sobel)

# Canny Edge Detection (this is more being used for edge detection and it is a multi-stage edge detection algorithm which also uses sobel gradients)
canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)