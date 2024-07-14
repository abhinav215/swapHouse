from moviepy.editor import VideoFileClip
import sys
import os


def solve(name,dirr):
    ff = "final"
    path = os.path.join(ff,dirr) 
    print(path)
    os.mkdir(path)
    time = VideoFileClip(name).duration
    start = 0
    # gap = 9.8
    gap = 180
    end = start+gap
    i = 0
    while start<time:
        print(start,min(end,time))
        clip = VideoFileClip(name).subclip(start,min(end,time))
        clip.write_videofile(path+"/test"+str(i)+".mp4")
        start +=gap
        end+=gap
        i+=1

def customSplit(start,name,dirr,lt):
    ff = "final"
    path = os.path.join(ff,dirr) 
    print(path)
    try:
        os.mkdir(path)
    except:
        pass
    time = VideoFileClip(name).duration
    print(time)
    i=1
    for end in lt:
        print(start,min(end,time))
        clip = VideoFileClip(name).subclip(start,min(end,time))
        clip.write_videofile(path+"/test"+str(i)+".mp4")
        start=end
        i+=1


# name = r"videoSplit\video6208493419573022761.mp4"
# dirr = "others"
# start = 0
# lt = [4,sys.maxsize]
# customSplit(start,name,dirr,lt)

name = r"VideoComplete\ab3e2e72f47636f1084a0b1a7b7d68e74f8584739b4a7e593655412f9410c2d9.mp4"
dirr = "besttt"
solve(name,dirr)
