import cv2 as cv

# function to rescale images/videos
def rescaleFrame(frame, scale=0.75): #video wil get resized by .75 percent
    #for images, videos, live videos
    width = int(frame.shape[1] * scale) #1 means width
    height = int(frame.shape[0] * scale) #0 means height

    dimentions=(width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

#let's use this function now:

capture=cv.VideoCapture('./resources/Videos/dog.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame, .70) #can pass any scalling factor

#     cv.imshow('resized_video', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()    

#there is another capture.set method which is only for live video for example webcam:
def changeRes(width, height):
    #live video
    capture.set(3,width) #3 mean width
    capture.set(4,height) #4 mean height

#let's resize big image now:
image=cv.imread('./resources/Photos/cat_large.jpg')

resized_image= rescaleFrame(image, .5)

cv.imshow('resized_cat', resized_image)

cv.waitKey(0)