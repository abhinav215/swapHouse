
import cv2
from moviepy.editor import *
import numpy as np
import os
import glob
import matplotlib.pyplot as plt
import insightface
from insightface.app import FaceAnalysis
from insightface.data import get_image as ins_get_image

app = FaceAnalysis(name="buffalo_l")
app.prepare(ctx_id=0, det_size=(640,640))


swapper = insightface.model_zoo.get_model("inswapper_128.onnx",download=False,download_zip=False)

def swapFxn(facePath,bodyImage):
    faceImage = cv2.imread(facePath)
    faceImgFace = app.get(faceImage)[0]
    body = app.get(bodyImage)
    if len(body)==0:
        return 
    bodyImgFace = body[0]
    
    res = bodyImage.copy()
    res = swapper.get(res,bodyImgFace,faceImgFace,paste_back=True)
    return res

def getFrames(vid, rate=0.05, frameName='frame'):
    ans = []
    vidcap = cv2.VideoCapture(vid)
    clip = VideoFileClip(vid)

    seconds = clip.duration
    print('duration: ' + str(seconds))
    
    count = 0
    frame = 0
    
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,frame*1000)      
        success,image = vidcap.read()

        ## Stop when last frame is identified
        # print(frame,seconds)
        if frame > seconds or not success:
            break

        # print('extracting frame ' + frameName + '-%d.png' % count)
        # name = output + '/' + frameName + '-%d.png' % count # save frame as PNG file
        # cv2.imwrite(name, image)
        ans.append(image)
        frame += rate
        count += 1
    return ans

def extract_audio_moviepy(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

def videomke(add):
    l = len(os.listdir(add))
    img = []
    for i in range(l):
        img.append(f"{add}/frame-{i}.png")

    clips = [ImageClip(m).set_duration(0.05)
        for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("test.mp4", fps=24)




vid = "1.mp4"
character = "faces/abhinav.jpg"
tempAudio = "output_audio.mp3"
tempVideo = "test.mp4"

output = "frames"
framesList = getFrames(vid)
print(len(framesList),"Frame Done","________________________")
extract_audio_moviepy(vid, tempAudio)
print("Audio extracted","________________________")
EditiedFrameList = []
cnt = 0
for ele in framesList:
    swapFxn(character,ele)
    if cnt%10==0:
        print(cnt)
    cnt+=1
print("Swap extracted","________________________")
videomke(EditiedFrameList)