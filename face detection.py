# Face recognition

#importing the libraries
import cv2
#importing the cascades as objects
face_cascade = cv2.CascadeClassifier(r'C:\Users\Dell\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Dell\haarcascade_eye.xml')

def detect(gray, frame):
    #getting the cordinates and width , height of the rectangle
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #faces are tuples of x,y coordinates width and height
    
    for (x, y, w, h) in faces:
        #to draw the rectangle
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) 
        roi_gray = gray[y:y+h, x:x+w] #region of interest
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
            #to draw the rectangle
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 0, 255 ), 2) 
            
        
    return frame

#doing the face recognition using webcam
video_capture = cv2.VideoCapture(0)

while True:
    # here _ refer to the part we don't want to store value of 
    _, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canvas = detect(gray, frame)
    cv2.imshow('Video Title', canvas)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
