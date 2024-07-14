from moviepy.editor import *

def videomke(img):
    clips = [ImageClip(m).set_duration(0.05)
        for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("test.mp4", fps=24)



if __name__== "__main__":
    add = "swap"
    videomke(add)