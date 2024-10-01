import cv2 as cv

img = cv.imread('resources/Photos/park.jpg')
cv.imshow('Boston',img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('L*a*b', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
# cv.imshow('BGR', bgr)

# Lab to BGR
bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('BGR', bgr)

# RGB to BGR
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow('BGR', bgr)

# note by default OpenCV reads images in BGR format and matplotlib reads images in RGB format
# which means if we provide rgb image to matplotlib then it will show the proper image as expected and provided
#macth up, and if we provide rgb to OpenCV then it will show the image in BGR format(so inversion)

cv.waitKey(0)