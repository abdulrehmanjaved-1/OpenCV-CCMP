import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('resources/Photos/cats.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')



# convert it to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# lets draw a circle for mask
circle =cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
cv.imshow('Circle', circle)

# lets craw a mask now
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256]) # 0 means grayscale (only one channel)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

cv.waitKey(0)