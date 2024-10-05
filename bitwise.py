import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1) #copy makes a copy of the image
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1) #-1 is for filled circle, 255 is white and 0 is black

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# bitwise AND (includes intersection which means common only)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR (includes union which means common and non intersecting both)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR (includes non common only)
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# we can minuse one image from another eg: bitwise_or - bitwise_xor = bitwise_and

# bitwise NOT (inverses the image)
bitwise_not = cv.bitwise_not(circle) # takes only one source image makes white to black and black to white
cv.imshow('Bitwise NOT', bitwise_not)

cv.waitKey(0)
