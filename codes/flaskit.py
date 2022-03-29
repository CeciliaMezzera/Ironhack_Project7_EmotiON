from flask import Flask, redirect, url_for
from flask import render_template, request
import argparse
import torch

import sys
import os
from main import detect
from emo_music import music_first_emotions
from emo_music import music_second_emotions
from write_emotion import write_two_emotions

import _thread


app = Flask(__name__)


@app.route("/")  

def home():
    return render_template("index.html")


@app.route('/test')
def do_something():
    parser = argparse.ArgumentParser()
#     parser.add_argument('--source', type=str, default='0', help='source')  # file/folder, 0 for webcam
#     parser.add_argument('--img-size', type=int, default=512, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.5, help='face confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.45, help='IOU threshold for NMS')
    parser.add_argument('--device', default='', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
    # parser.add_argument('--hide-img', action='store_true', help='hide results')
    save = parser.add_mutually_exclusive_group()
#     save.add_argument('--output-path', default="output.mp4", help='save location')
    save.add_argument('--no-save', action='store_true', help='do not save images/videos')
    parser.add_argument('--agnostic-nms', action='store_true', help='class-agnostic NMS')
    parser.add_argument('--augment', action='store_true', help='augmented inference')
    parser.add_argument('--line-thickness', default=2, type=int, help='bounding box thickness (pixels)')
#     parser.add_argument('--hide-conf', default=False, action='store_true', help='hide confidences')
#     parser.add_argument('--show-fps', default=False, action='store_true', help='print fps to console')
    opt = parser.parse_args()
#     with torch.no_grad():

    def plot():
        os.system('python Plot.py')

    # Use thread to run camera and plot simoultaneously
    _thread.start_new_thread(plot,())

    # Run the funtion
    detect(source='0', view_img = 'store_true', imgsz = 512, nosave = 'store_true', show_conf=False, save_path = 'output.mp4', show_fps = True)
    
    return render_template('index.html')

# Video function
@app.route('/video')
def video():
    global video_name
    video_name = 'video_your_emotions.gif'

    return render_template('index.html', video= video_name)


# Write function
@app.route('/write')
def write():
    text1, text2 = write_two_emotions()

    return render_template('index.html', video= video_name, text1 = text1, text2=text2)


@app.route('/music_one')
def play_music_one():
    music_first_emotions()

    return ("nothing")

@app.route('/music_two')
def play_music_two():
    music_second_emotions()

    return ("nothing")


if __name__ == "__main__":
    app.run(debug=True, port=2251)