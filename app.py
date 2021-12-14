from flask import Flask, render_template, Response
import cv2
app=Flask(__name__)
video = cv2.VideoCapture('Videos/tomhiddleston.mp4')

# Set resolutions of frame.
# convert from float to integer.
frame_width = int(video.get(3))
frame_height = int(video.get(4))

result = cv2.VideoWriter('Videos/output.avi',
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, (frame_width,frame_height))

def gen_frames():
    while True:
        success, frame = video.read()  # read the camera frame
        if not success:
            break
        else:
            detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            faces=detector.detectMultiScale(frame)
             #Draw the rectangle around each face
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 10)
            result.write(frame)

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__=='__main__':
    app.run(debug=True)