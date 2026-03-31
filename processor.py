from moviepy.editor import VideoFileClip

def extract_audio(video_file, output_audio):
    try:
        # वीडियो फाइल को लोड करना (Load the video file)
        video = VideoFileClip(video_file)
        
        # ऑडियो को अलग करना और सेव करना (Extract and save audio)
        video.audio.write_audiofile(output_audio)
        print(f"Audio successfully extracted to {output_audio}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # मान लेते हैं कि वीडियो का नाम 'downloaded_video.mp4' है
    # Assuming the video name is 'downloaded_video.mp4'
    extract_audio("downloaded_video.mp4", "output_audio.wav")
