import cv2

# Load some pre-trained data on face frontals from Opencv (haar cascade algorithm)
trained_face_data = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Choose an image to detect faces
img = cv2.imread('Images/TOM1.jpg')

# Must convert to grayscale
grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)

# Draw rectangle around the faces
length = len(face_coordinates)
for i in range(length):
    (x,y,w,h) = face_coordinates[i]
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
#cv2.rectangle(img, (328, 218), (323+328, 323+218), (0,255,0), 2)

cv2.imshow('Face Detection', img)
cv2.waitKey()

print("Code completed")