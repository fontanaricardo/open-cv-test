# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV 
import cv2
import numpy as np
import os
 
FILE_OUTPUT = 'output.avi'

# Checks and deletes the output file
# You cant have a existing file or it will through an error
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)

# capture frames from a video
cap = cv2.VideoCapture('21.mp4')

# Get current width of frame
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
# Get current height of frame
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
 
# Trained XML classifiers describes some features of some object we want to detect
pedestrians_cascade = cv2.CascadeClassifier('cars.xml')

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'X264')
out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (int(width),int(height)))
 
# loop runs if capturing has been initialized.
while True:
    # reads frames from a video
    ret, frames = cap.read()
     
    # convert to gray scale of each frames
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    # Detects pedestrians of different sizes in the input image
    pedestrians = pedestrians_cascade.detectMultiScale(gray, 1.1, 1)
     
    # To draw a rectangle in each pedestrians
    for (x,y,w,h) in pedestrians:
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)
        
    out.Write(frames)
   # Display frames in a window 
   # cv2.imshow('video2', frames)
     
    # Wait for Esc key to stop
    # if cv2.waitKey(33) == 27:
    break
 
# De-allocate any associated memory usage
# cv2.destroyAllWindows()