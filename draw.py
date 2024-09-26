import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8') #3 is for 3 channels what it means is RGB

# cv.imshow("Blank", blank)

# 1. paint the image a certain color
# blank[:]= 255,0,255 #: means all pixels 
# cv.imshow("Blank", blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (255,255,255), thickness=-1)
cv.imshow("Blank", blank)


# 3. Draw A circle
cv.circle(blank, (255,255), 40, (255,0,0), thickness=-1)
cv.imshow("Blank", blank)

# 4. Draw a line
cv.line(blank, (255,300), (499,200), (0,0,255), thickness=5)
cv.imshow("Blank", blank)

# 5. write text
cv.putText(blank, "Helo I am Abdulrehman Javed!!", (0,400), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,0,0), 2)
cv.imshow("Blank", blank)


cv.waitKey(0)

