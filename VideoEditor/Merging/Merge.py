from moviepy.editor import *


def solve(lt,parent,naam):
    lt2 = []
    for ele in lt:
        lol = r"/test"+ele
        print(parent+lol+".mp4")
        clip1 = VideoFileClip(parent+lol+".mp4")
        lt2.append(clip1)
    final_clip = concatenate_videoclips(lt2)
    final_clip.write_videofile(naam+".mp4")


lt = ["1","2"]
zz = r"final\others\others"
naam = "othesVid39u20948"
solve(lt,zz,naam)