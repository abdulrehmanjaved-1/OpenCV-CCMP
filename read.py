import cv2 as cv

img= cv.imread('./resources/Photos/cat.jpg') #this method takes path of an image and returns image as a matrix of pixels

cv.imshow('Cat', img)

cv.waitKey(0) # if we dont use this the image will not be shown but got rendered. 0 means any key with infinte time.

