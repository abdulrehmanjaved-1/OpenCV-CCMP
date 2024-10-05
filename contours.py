import cv2 as cv
import numpy as np


img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('cats', img)

# blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

#covert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur the image
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# find the edges of the image using canny (edge cascading)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# instead of passing canny as an argument, we can pass thresholded image (which is a binary converted image)
# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #below 125 will be black and above will be white
# cv.imshow('Thresh', thresh)

# find the contours 
# contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# print(f'{len(contours)} contour(s) found!')
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contour(s) found!')

# draw contours on blank image to visualize
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

cv.waitKey(0)