import cv2 as cv

# smoothinf to reduce the noice in image is one of the things why we blur.


img=cv.imread('./resources/Photos/cats.jpg')
cv.imshow('Cats',img)

# Averaging 
average=cv.blur(img, (7,7)) #inc the kernel for more blur
cv.imshow('Average Blur', average)

# Guassian Blur (less blur than average but better and natural) 
guass=cv.GaussianBlur(img, (7,7), 0) #0 is sigma which means standard deviation, and standard deviation means mathematically the width of the kernel may be.
cv.imshow('Guassian Blur', guass)

# Median Blur(better than average and guassian  blur method and good for noice reduction to substantial level)0
median=cv.medianBlur(img, 7) # 7 is same like tuple of 7,7
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral =cv.bilateralFilter(img, 10, 35, 25) # 10 is diameter, 35 is sigma color, 25 is sigma space(larger sigma space means true center will influnece bt far spaced pixels in image as well, large sigma color means consider more colors in neighber if there)
cv.imshow('Bilateral Blur', bilateral)


cv.waitKey(0)