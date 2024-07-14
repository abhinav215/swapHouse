import os
from framesMaker import getFrames
# from audioExtract import extract_audio_moviepy
from swapFirstToFirst import swapFxn
from VideoMaker import videomke
# from addingAudio import audioAdder

vid = "videos/1 (3).mp4"
character = "faces/abhinav.jpg"
tempAudio = "output_audio.mp3"
tempVideo = "test.mp4"



# output = "frames"
# getFrames(vid, output)
# print("getFrames done")
# extract_audio_moviepy(vid, tempAudio)
# print("extract_audio_moviepy done")
lt = os.listdir("frames")
swapFrames = []
for file in lt:
    fullName = "frames/"+file
    outputAddress= "swap/"+file
    print(fullName)
    xx = swapFxn(character,fullName,outputAddress)
    swapFrames.append(xx)
print("swapFxn done")
videomke(swapFrames)
print("videomke done")
# audioAdder(tempVideo,tempAudio)
# print("audioAdder done")
