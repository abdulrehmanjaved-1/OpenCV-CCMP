import cv2 as cv
import numpy as np


img = cv.imread('./resources/Photos/park.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)


# Split color channels
b, g, r = cv.split(img)


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# show 
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Merge
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# 

cv.waitKey(0)