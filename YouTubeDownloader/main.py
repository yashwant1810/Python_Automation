import ssl
from pytube import YouTube
import argparse

# Disable SSL certificate verification ( run if ssl errors are thrown)
#ssl._create_default_https_context = ssl._create_unverified_context

save_dir_video = "./Videos"
save_dir_audio = "./Audio"

def VideoDownloader(url):
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()

    try:
        stream.download(save_dir_video)
    except Exception as e:
        print(f"Couldn't download video: {e}")

    print("Video was downloaded successfully")

def AudioDownloader(url):
    video = YouTube(url)
    audio = video.streams.filter(only_audio=True).first()

    try:
        audio.download(save_dir_audio)
    except Exception as e:
        print(f"Couldn't download audio: {e}")

    print("Audio was downloaded successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", required=True)
    parser.add_argument("-a", "--audio", required=False, action=argparse.BooleanOptionalAction)
    args = vars(parser.parse_args())

    if args["audio"]:
        AudioDownloader(args["video"])
    else:
        VideoDownloader(args["video"])