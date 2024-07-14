from moviepy.editor import VideoFileClip

def extract_audio_moviepy(video_path, output_audio_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_audio_path)

if __name__== "__main__":
    extract_audio_moviepy("videos/1 (3).mp4", "output_audio.mp3")