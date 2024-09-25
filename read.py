import cv2 as cv

# img= cv.imread('./resources/Photos/cat.jpg') #this method takes path of an image and returns image as a matrix of pixels

# cv.imshow('Cat', img)

# cv.waitKey(0) # if we dont use this the image will not be shown but got rendered. 0 means any key with infinte time.

# # Resolution Name	Width (pixels)	Height (pixels)	Notes
# # HD (720p)	1280	720	Standard HD
# # Full HD (1080p)	1920	1080	High-definition
# # 2K	2048	1080	Cinema resolution
# # 4K	3840	2160	Ultra-high-definition
# # 8K	7680	4320	Extremely detailed

# # note: we also care about DPI/PPI, with high DPI image will be smaller and vise versa.

#let's do read vidoes now:

# capture = cv.VideoCapture(0) #integer means refernce to the webcam or any other video source camera connected to your computer.
capture = cv.VideoCapture('./resources/Videos/dog.mp4') #or just pass already read video path,
#at this point we have just an instance of video capture object

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame) #video frame is same as image frame at specific time

    if cv.waitKey(20) & 0xFF==ord('d'): #this means if we press d on keyboard then video will stop.
        break

capture.release()
cv.destroyAllWindows()

#(-215:Assertion failed) error mean video is not read properly on the path, it can be due to media not found
#or frame finished.
