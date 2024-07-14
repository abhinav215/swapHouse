from moviepy.editor import *

def padding(count):
    count += 100000
    ss = str(count)
    return ss[1:]

def videomke(add):
    l = len(os.listdir(add))
    img = []
    for i in range(l):
        img.append(f"{add}/frame{padding(i)}.png")

    clips = [ImageClip(m).set_duration(0.05)
        for m in img]

    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("test.mp4", fps=24)



if __name__== "__main__":
    add = "swap"
    videomke(add)