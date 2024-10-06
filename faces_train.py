import os
import cv2 as cv
import numpy as np

from face_detect import haar_cascade

# list of people which we will use to train opencv recognizer model on
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
Dir = r'C:\Users\IT-Support\Desktop\opencv\resources\Faces\train'
# to detect faces we use cascade classifier
haar_cascade = cv.CascadeClassifier('haar_face.xml')

features = []
labels = []

# let's create function for preparing training data
def create_train():
    for person in people:
        path = os.path.join(Dir, person) # path of each person folder
        label = people.index(person) # index of each person

        for img in os.listdir(path): # list of images in each person folder
            img_path = os.path.join(path, img) # path of each image

            img_array = cv.imread(img_path) # convert image to array
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY) # convert image to grayscale

            # detect faces in this image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w] # region of interest
                features.append(faces_roi)
                labels.append(label)

# run the function
create_train()
# print(f'Length of features = {len(features)}')
# print(f'Length of labels = {len(labels)}')


features = np.array(features, dtype='object')
labels = np.array(labels)
# instantiate the model
face_recognizer = cv.face.LBPHFaceRecognizer_create()
# train the model
face_recognizer.train(features, labels)
# lets save this model
face_recognizer.save('face_trained.yml')
print('Training done!!!')
# save the features and labels
np.save('features.npy', features)
np.save('labels.npy', labels)

