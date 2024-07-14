import os
import cv2
import moviepy.editor

def padding(count):
    count += 100000
    ss = str(count)
    return ss[1:]

def getFrames(vid, output, rate=0.05, frameName='frame'):
    vidcap = cv2.VideoCapture(vid)
    clip = moviepy.editor.VideoFileClip(vid)

    seconds = clip.duration
    print('duration: ' + str(seconds))
    
    count = 0
    frame = 0
    
    if not os.path.isdir(output):
        os.mkdir(output)
    
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,frame*1000)      
        success,image = vidcap.read()

        ## Stop when last frame is identified
        print(frame,seconds)
        if frame > seconds or not success:
            break

        print('extracting frame ' + frameName + padding(count)+".png")
        name = output + '/' + frameName + padding(count)+".png" # save frame as PNG file
        cv2.imwrite(name, image)
        frame += rate
        count += 1



if __name__== "__main__":
    vid = "1.mp4"
    output="frames"
    getFrames(vid, output)