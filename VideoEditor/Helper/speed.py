

from moviepy.editor import *
import os

def speed(name,spd):
    clip = VideoFileClip(name)
    time = clip.duration
    print(time)
    newClip = clip.fx( vfx.speedx, spd)
    time = newClip.duration
    print(time)
    newClip.write_videofile("fast1"+".mp4")


name = r"final\besttt\test1.mp4"
spd = 1.2
speed(name,spd)