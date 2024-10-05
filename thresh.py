import cv2 as cv

#thresholding is binarization of an image

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 10, 255, cv.THRESH_BINARY) # above 150 will be white and below will be black and 255 means set to 255 if its grater than threshold
cv.imshow('Simple Threshold', thresh)

# there is also inverse way like to set greater than threshold values to white and less than threshold to black
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', thresh_inv)

# adaptive thresholding (this is for opencv finds the best threshold by kernel window and using weight calc or mean of it as discussed)
# it is a way of thresholding that uses the median of neighbourhood area
adaptive_threshold = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 3) # 11 is blocksize/kernel and 3 is C
cv.imshow('Adaptive Threshold', adaptive_threshold)

cv.waitKey(0)