import cv2 as cv
import numpy as np

img = cv.imread('resources/Photos/cats 2.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8') #size of mask has to be of same size of image
cv.imshow('Blank', blank)

# # create mask (circle)
# mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
# cv.imshow('Mask', mask)

# # create mask (rectangle)
# mask = cv.rectangle(blank, (img.shape[1]//2, img.shape[0]//2), (img.shape[1]//2 + 100, img.shape[0]//2 + 100), 255, -1)
# cv.imshow('Mask', mask)

# create mask (weired shape)
circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
cv.imshow('Rectangle', rectangle)
weired_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('Weired Shape', weired_shape)

# cv.imshow('Mask', weired_shape)
# mask the image
masked = cv.bitwise_and(img, img, mask=weired_shape)
cv.imshow('Weired Shape Masked image', masked) #remember profile images are same thing just masking and doing operations



cv.waitKey(0)