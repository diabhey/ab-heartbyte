import time
import cv2
import threading
import argparse
from flask import Flask, render_template, Response

# initialize the output frame and a lock used to ensure thread-safe
# exchanges of the output frames (useful when multiple browsers/tabs
# are viewing the stream)
outputFrame = None
lock = threading.Lock()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def video_read():
    global cap, outputFrame, lock
    print("Calling video read")
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):
      # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
            frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            with lock:
                outputFrame = frame.copy()

def generate():
	# grab global references to the output frame and lock variables
	# global outputFrame, lock
	# loop over frames from the output stream
	while True:
		# wait until the lock is acquired
		with lock:
			# check if the output frame is available, otherwise skip
			# the iteration of the loop
			if outputFrame is None:
				continue
			# encode the frame in JPEG format
			(flag, encodedImage) = cv2.imencode(".jpg", outputFrame)
			# ensure the frame was successfully encoded
			if not flag:
				continue
		# yield the output frame in the byte format
		yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
			bytearray(encodedImage) + b'\r\n')                   

@app.route('/video_feed')
def video_feed():
    return Response(generate(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')            
    
if __name__ == '__main__':
    # args = argparse.ArgumentError()
    # args.add_argument("--ip",type=str, required=True)

    thread = threading.Thread(target=video_read)
    thread.daemon = True
    thread.start()

    # start the application
    app.run(threaded=True, debug=True)






