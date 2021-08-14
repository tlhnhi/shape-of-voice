import keyboard #pip install keyboard
from camera import VideoCamera
from flask import Flask, render_template, Response, stream_with_context, request
import cv2
from sign_to_text import Sign2Text
from time import sleep
import ffmpeg
import speech_recognition as sr

app = Flask(__name__)
# camera = cv2.VideoCapture(0)
Sign2Text_model = Sign2Text(cnn_model_path='./InceptionV3_5epochs.h5', knn_model_path='./knn_model.sav')
frame = None
start_point = (50, 50)
width = 300
height = 300
end_point = (start_point[0] + width, start_point[1] + height)
color = (255, 0, 0)
thickness = 2

def gen_frames(camera):
    global frame
    while True:
        success, frame = camera.read()  # read the camera frame
        frame = cv2.flip(frame, 1)
        frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
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
        img = frame[start_point[1]:start_point[1] + height, start_point[0]:start_point[0] + width, :]
        pred_class, prob = Sign2Text_model.predict(img)
        if pred_class != None:
            if not prev or prev != pred_class:
                prev = pred_class
                yield pred_class
    

@app.route('/', methods=['GET'])
def index():
    return render_template('layout.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/text_feed')
def text_feed():
    return Response(stream_with_context(sign2text()))

@app.route('/test_mic')
def test():
    return render_template('test_mic.html')

@app.route('/speech2text', methods=['POST'])
def speech2text():
    file = request.files['file']
    inp_file = 'upload/uploaded_record.wav'
    file.save(inp_file)

    out_file = "./upload/uploaded_record_conv.wav"
    ffmpeg.input(inp_file).output(out_file, ar=16000, ac=1, ab=256000).overwrite_output().run()
    r = sr.Recognizer()
    with sr.AudioFile(out_file) as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio,language="vi-VI")
            return text
        except:
            return "Xin lỗi! tôi không nhận được voice!"

if __name__ == '__main__':
    app.run(host='localhost', debug=True)