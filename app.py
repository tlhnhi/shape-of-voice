from camera import VideoCamera
from flask import Flask, render_template, Response, stream_with_context
import cv2
from sign_to_text import Sign2Text
from time import sleep

app = Flask(__name__)
camera = cv2.VideoCapture(0)
Sign2Text_model = Sign2Text('InceptionV3_5epochs.h5', None)
frame = None

def gen_frames(camera):
    global frame
    while True:
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            _, buffer = cv2.imencode('.jpg', frame)
            frame_bytes = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')  # concat frame one by one and show result

def sign2text():
    global frame
    prev = None
    while True:
        sleep(0.2)
        if frame is None:
            continue
        start_point = (200, 200)
        width = 500
        height = 500
        end_point = (start_point[0] + width, start_point[1] + height)
        color = (255, 0, 0)
        thickness = 2
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
        img = frame[start_point[1]:start_point[1] + height, start_point[0]:start_point[0] + width, :]
        pred_class, prob = Sign2Text_model.predict_cnn(img)
        if prob > 0.9:
            if not prev or prev != pred_class:
                prev = pred_class
                yield pred_class
    

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/text_feed')
def text_feed():
    return Response(stream_with_context(sign2text()))

if __name__ == '__main__':
    app.run(host='localhost', debug=True)