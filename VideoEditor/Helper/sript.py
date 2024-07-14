from moviepy.editor import *
import os
import sys


sys.stdout = open(r'Helper\output.txt', 'w') 

def duration(name):
    clip = VideoFileClip(name)
    time = clip.duration
    print(name,"=>",time)


def compress(name):
    clip = VideoFileClip(name)
    clip_resized = clip.resize(height=360) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
    clip_resized.write_videofile("movie_resized.mp4")

def width(name):
    clip = VideoFileClip(name)
    width = clip.w
    height = clip.h
    fact = 2/3
    # print(int(width*fact),int(height*fact))
    print(int(width),int(height))

def listDuration(path):
    ll = os.listdir(path)
    for filename in ll:
        fullFileName = os.path.join(path,filename)
        # print(fullFileName)
        duration(fullFileName)

# name = r"VideoComplete\video6100634279530728696.mp4"
# duration(name)
        
listDuration(r"final\carFuck")

# width(name)
# compress(name)