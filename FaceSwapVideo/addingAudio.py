from moviepy.editor import VideoFileClip, AudioFileClip, CompositeAudioClip

def audioAdder(videoPath,audioPath):
    videoclip = VideoFileClip(videoPath)
    audioclip = AudioFileClip(audioPath)

    new_audioclip = CompositeAudioClip([audioclip])

    videoclip.audio = new_audioclip

    videoclip.write_videofile("new_filename.mp4")


if __name__=="__main__":
    videoPath = "test.mp4"
    audioPath = "output_audio.mp3"
    audioAdder(videoPath,audioPath)
