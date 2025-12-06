"""
A script that takes a YouTube video URL and converts it into a mp4 or mp3 file.
"""


from tkinter import *
from pytubefix import YouTube
from pathlib import Path


### Script ###

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

        return False, f"Error : Invalid URL {e}"

    try:

        if choice == "mp4":

            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=path_mp4)
            return True, "Video downloaded successfuly"


        elif choice == "mp3":

            stream = yt.streams.filter(only_audio=True).first()
            file = stream.download(output_path=path_mp3)
            file_path = Path(file)
            mp3_file = file_path.with_suffix(".mp3")
            file_path.rename(mp3_file)
        
            return True, "Audio downloaded successfuly !"

    except Exception as e:

        return False, f"Download failed {e}"





def Convert_Clicked():

    """
    This function defines the logic when the Convert button is pressed 
    and links it to the download function.
    """

    Convert.config(state="disabled")

    url = Url_Entry.get().strip()

    select_mp3 = mp3_var.get()
    select_mp4 = mp4_var.get()

    if not url:
        status_label.config(text="Enter a Valid YouTube URL",fg = "red")
        return

    if not (select_mp3 or select_mp4):
        status_label.config(text="Select one of the two options !", fg = "red")
        return

    status_label.config(text="Downloading File... ", fg = "green")
    status_label.update_idletasks()


    if select_mp3:
        success, message = download(url, "mp3")
        if success:
            status_label.config(text="MP3: " + message, fg="green")
        else:
            status_label.config(text="MP3: " + message, fg = "red")

    if select_mp4:
        success, message = download(url, "mp4")

        if success:
            status_label.config(text="MP4: " + message, fg="green")
        else:
            status_label.config(text="MP4: " + message, fg = "red")

    Convert.config(state="normal")

def checkbox_state():
    """
    This function checks whether the MP3 or MP4 checkox is checked
    and disables the other one.
    """
    if mp3_var.get() == True:
        mp4_check.config(state="disabled")
        mp3_check.config(state="normal")
        
    elif mp4_var.get() == True:
        mp3_check.config(state="disabled")
        mp4_check.config(state="normal")
    else:
        mp3_check.config(state="normal")
        mp4_check.config(state="normal")


### GUI ###

gui = Tk()
gui.geometry("700x700")
gui.title("Youtube to MP3 and MP4 Coverter")

Yt_label = Label(gui,text="Youtube to MP3 and MP4 Converter",fg = "Red",font=("Popins",25,"bold")) # Title
Yt_label.place(relx = 0.5, rely = 0.2, anchor="center")

Url_Entry = Entry() # URL entry text box
Url_Entry.config()
Url_Entry.place(width = 370 , height= 30 , relx = 0.2, rely= 0.6)

Convert = Button(gui, text="Convert",bg = "red",font=("Popins",10,"bold"), command = Convert_Clicked) #Convert Button
Convert.place(width = 90, height = 55, relx = 0.74, rely = 0.585)

mp3_var = BooleanVar()
mp4_var = BooleanVar()

mp3_check = Checkbutton(gui, text = "MP3",font=("Popins",10,"bold"), variable = mp3_var, command = checkbox_state) # MP3 Checkbox
mp3_check.place(relx = 0.3, rely = 0.4)


mp4_check = Checkbutton(gui, text = "MP4",font=("Popins",10,"bold"), variable = mp4_var, command = checkbox_state) #MP4 Checkbox
mp4_check.place(relx = 0.56, rely = 0.4)

status_label = Label(gui, text="", fg= "black", font=("Popins", 10))
status_label.place(relx = 0.5, rely = 0.75, anchor = "center")



gui.mainloop()


#Todo

# Make a more appealing GUI
