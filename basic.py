import cv2 as cv

#currently this is an BGR image with 3 color channels
img = cv.imread('./resources/Photos/park.jpg') 
cv.imshow('Park', img)

#converting it to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale", gray)

# Blur
blur= cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade # 125 and 175 are thresholds, 125 is lower and 175 is higher, values above higher threshholds are considered strong edges, below 125 will be non-edges.
canny =cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

#Dilating the image #grows the white area (foreground) of edged (structured element) image.
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

#Eroding (its just undo back to edge cascade point, cancelling the dilate effect in most cases)
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

#resizing #interpolation is about managing qaulity cubic is high but slow, linear and area is low qual.
resized= cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized high qualtiy cubic", resized)
resized= cv.resize(img, (500,500), interpolation=cv.INTER_LANCZOS4)
cv.imshow("More high than cubic even", resized)

#croping
croped= img[50:200, 200:400] #directly access pixels
cv.imshow("croped", croped)

cv.waitKey(0)