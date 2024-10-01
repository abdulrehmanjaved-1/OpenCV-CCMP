import cv2 as cv
import numpy as np

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Boston',img)

#Image tranformation function (mvoing image)
def translate(img, x, y): #x,y is how much to move from x and y axis
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimentions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimentions)

# -x --> Left moved image if we put this 
# x --> Right 
# y --> Down
# -y --> Up

translated = translate(img, 100, 100)
cv.imshow('Translate', translated)


# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimentions = (width,height)

    return cv.warpAffine(img, rotMat, dimentions)    

rotated = rotate(img,-45)
cv.imshow('Rotated', rotated)

rotated_rotated=rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

# Resizing
resized  = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

# Flipping (1 mean horizontal, -1 mean vertical, 0 mean both)
flip = cv.flip(img, 1)
cv.imshow('Flip', flip)

cv.waitKey(0)