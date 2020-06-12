import cv2

face_cascade = cv2.CascadeClassifier(r'C:\Users\Dell\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(r'C:\Users\Dell\haarcascade_eye.xml')
cascade_smile = cv2.CascadeClassifier(r'C:\Users\Dell\haarcascade_smile.xml')

def detect(gray, frame):
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2) 
        roi_gray = gray [y:y+h, x:x+w] #region of interest
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale( roi_gray , 1.1, 3)
        for (ex, ey, ew, eh) in eyes:
                #to draw the rectangle
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 0, 255 ), 2) 
                
        smile = cascade_smile.detectMultiScale(roi_gray, 1.7, 22) 
        for (x_smile, y_smile, w_smile, h_smile) in smile:
            cv2.rectangle(roi_color,(x_smile, y_smile),(x_smile+w_smile, y_smile+h_smile), (0, 255, 0), 2)
        
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

