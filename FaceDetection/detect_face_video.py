import cv2
import requests

URL = "http://192.168.205.115"

face_cascade = cv2.CascadeClassifier(
    './FaceDetection/haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(1)
cap = cv2.VideoCapture("http://192.168.205.62/stream")

cv2.namedWindow("Frame", cv2.WINDOW_AUTOSIZE)
(x, y, width, height) = cv2.getWindowImageRect("Frame")

center = int(width/2)

while True:
    # Read the frame
    _, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        x_medium = int((x+x+w)/2)
        y_medium = int((y+y+h)/2)
        # requests.get(url=URL,
        #              params={'led': str(int((x_medium/width)*180))})
        print(int((x_medium/width)*180))

    # Display
    cv2.imshow('Frame', frame)

    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
