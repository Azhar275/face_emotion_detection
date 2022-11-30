from flask import Flask, render_template, Response, request, redirect, session, url_for
import cv2
from flask_bootstrap import Bootstrap5

import videotester

app = Flask(__name__)
bootstrap = Bootstrap5(app)


@app.route('/')
def coba():
    return render_template('coba.html')


@app.route('/video')
def video():
    return Response(videotester.generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
