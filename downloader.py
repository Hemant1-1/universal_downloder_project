import yt_dlp
import os

def download_video(url):
    try:
        # डाउनलोड सेटिंग्स (Download settings)
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'downloaded_video.%(ext)s',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("Downloading started...")
            ydl.download([url])
            print("Download completed!")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    link = input("Enter the video URL: ")
    download_video(link)
