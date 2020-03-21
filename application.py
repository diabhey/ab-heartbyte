import cv2
import face_recognition
from flask import Flask, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def gen():
    video = cv2.VideoCapture(0)
    while(video.isOpened()):
        ret, frame = video.read()
        if ret == True:
            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
            # face_locations = face_recognition.face_locations(frame, model="cnn")
            # encodings = face_recognition.face_encodings(frame, face_locations)
            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'b'Content-Type: frame/jpeg\r\n\r\n' + frame + b'\r\n')                

            if cv2.waitKey(1) & 0xFF == ord('q'):
                   break
        else:
            break           

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')            
    
if __name__ == '__main__':
    app.run(debug=True)


