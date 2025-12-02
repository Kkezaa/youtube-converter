
"""
A script that takes a YouTube video URL and converts it into a mp4 or mp3 file.
"""
from pytubefix import YouTube
from pathlib import Path

url = input("Insert the video URL you want: ")

choice = input("Enter the desired format:  'mp3' for audio or 'mp4' for video : ").lower()

def download(url, choice):

    """
    This function takes a url as a argument and stores is into a variable,
    to later download a video or audio from.
    """

    path_mp3 = "/home/kkezaa/projects/Youtube_Converter/Audios"

    path_mp4 = "/home/kkezaa/projects/Youtube_Converter/Videos"

    try:

        yt = YouTube(url)

    except Exception as e:

        print(f"Error: Invalid or Deleted URL, try again. {e}") # Catches error if URL is invalid
        return

    if choice == "mp4": 

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=path_mp4) 
        print("Video successfuly downloaded !")

    elif choice == "mp3":

        stream = yt.streams.filter(only_audio=True).first()
        file = stream.download(output_path=path_mp3)
        file_path = Path(file)
        mp3_file = file_path.with_suffix(".mp3")
        file_path.rename(mp3_file)
        
        print("Audio successfuly downloaded !")

    else:
        print("Error: Please enter a valid format !")


download(url, choice)

