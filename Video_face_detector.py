import cv2

# Load some pre-trained data on face frontals from Opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose an image to detect faces
webcam = cv2.VideoCapture('Videos/FaceDetection.mp4')
#webcam = cv2.VideoCapture(0)

# Set resolutions of frame.
# convert from float to integer.
frame_width = int(webcam.get(3))
frame_height = int(webcam.get(4))

result = cv2.VideoWriter('Videos/output.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (frame_width,frame_height))

# Iterate over frames
while True:
    #Read the current frame
    successful_frame_read, frame = webcam.read()

    # Must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    result.write(frame)
    cv2.imshow('Face Detection', frame)
    cv2.waitKey(1)

    # Stop if Q key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object
webcam.release()
cv2.destroyAllWindows()

print("Code completed")