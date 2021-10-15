from __future__ import unicode_literals
import youtube_dl
import os
from moviepy.editor import *
from time import sleep  # Maybe throttle the requests to youtube-dl
from flask import send_from_directory, abort, render_template
from flask import Flask
import flask
import time


app = Flask(__name__)


app.config["CLIENT_MUSIC"] = "./client/music"
app.config["CLIENT_VIDEOS"] = "./client/videos"


@app.route('/post-music/<music_name>')
def post_music(music_name):
    print(music_name)
    if music_name == "9bZkp7q19f0":
        return "YOU DARE WATCH ASIAN PROPAGANDA FROM OUR SERVERS?\n YOU ARE FUNNY! \n PLEASE FACE WALL"
    file_name = "./client/videos/" + music_name + ".mp4"
    ydl_opts = {'outtmpl': file_name}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + music_name])
    video = VideoFileClip(os.path.join(file_name))
    audio_file_name = "./client/music/" + music_name + ".mp3"
    video.audio.write_audiofile(os.path.join(audio_file_name))
    pathToRedirect = "/get-music/" + music_name + ".mp3"
    #os.remove("./client/videos/" + music_name + ".mp4")
    return flask.redirect(pathToRedirect)

@app.route('/post-video/<video_name>')
def post_video(video_name):
    print(video_name)
    if video_name == "9bZkp7q19f0":
        return "YOU DARE WATCH ASIAN PROPAGANDA FROM OUR SERVERS?\n YOU ARE FUNNY! \n PLEASE FACE WALL"
    file_name = "./client/videos/" + video_name + ".mp4"
    ydl_opts = {'outtmpl': file_name}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + video_name])
    pathToRedirect = "/get-video/" + video_name + ".mp4"
    #os.remove("./client/videos/" + video_name + ".mp4")
    return flask.redirect(pathToRedirect)

@app.route('/get-video/<video_name>')
def get_video(video_name):
    try:
        return send_from_directory(app.config["CLIENT_VIDEOS"], path=video_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


@app.route('/get-music/<music_name>')
def get_song(music_name):
    try:
        return send_from_directory(app.config["CLIENT_MUSIC"], path=music_name, as_attachment=True)
    except FileNotFoundError:
        abort(404)


