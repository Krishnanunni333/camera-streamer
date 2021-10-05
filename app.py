from flask import Flask, render_template, Response
import cv2
import time

app = Flask(__name__)

camera = cv2.VideoCapture(0)

frame_width = int(video.get(3))
frame_height = int(video.get(4))
size = (frame_width, frame_height)

filename = "cctv-{}-tracker.avi".format(time.strftime("%Y%m%d-%H%M%S"))
result = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'MJPG'), 10, size)

def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
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


if __name__ == '__main__':
    #app.debug = True
    app.run(host="0.0.0.0", threaded=True)
