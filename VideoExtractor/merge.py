from moviepy.editor import *


def merge(naam,parent):
    lt2 = []
    ll = os.listdir(parent)
    print(len(ll))
    for i in range(len(ll)):
        videoName = parent+"/video"+str(i)+".ts"
        print(videoName)
        clip1 = VideoFileClip(videoName)
        lt2.append(clip1)
    final_clip = concatenate_videoclips(lt2)
    final_clip.write_videofile(naam+".mp4")


if __name__ == '__main__':
    naam = "AJLee"
    zz = r"AJ Lee"
    merge(naam,zz)