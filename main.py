import cv2

print(cv2.__version__)

# capture frames from a video
cap = cv2.VideoCapture('21.mp4')

pedestrians_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')

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

    # Display frames in a window 
    cv2.imshow('video2', frames)
     
    # Wait for Esc key to stop
    if cv2.waitKey(33) == 27:
        break
 
# De-allocate any associated memory usage
cv2.destroyAllWindows()