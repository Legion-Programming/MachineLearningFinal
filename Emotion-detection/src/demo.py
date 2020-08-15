from tkinter import *
from moviepy.editor import *
import webbrowser
import tkinter
import emotions as em
from src.data.emotionsModules import *


window = Tk()
window.geometry("920x1060")
window.title("Ad Me In")

label1 = Label(window, text="Welcome to Ad Me In", fg='blue', bg='yellow', relief="solid",
               font=("ariel", 16, "bold")).pack()
video_start = False

def helloCallBack():
    if video_start == True:
        print(emotions)

B = tkinter.Button(window, text="hello", command=helloCallBack)
B.pack()
window.mainloop()
#b = Button(window, text="Click here to start the demo", fg='blue', bg='yellow', relief="solid", command= callback)
#b.pack()
#window.mainloop()

# video_name = "./demoVideos/K-Fee_Auto_Commercial.mp4"  # This is your video file path
# video = imageio.get_reader(video_name)

def callback():
    print("click")
    play_video()



def play_video():
    # !/usr/bin/env python3
    a_website = "https://www.youtube.com/watch?v=SoUx2NAnIFE"

    # Open url in a new window of the default browser, if possible
    webbrowser.open_new(a_website)

    # Open url in a new page (“tab”) of the default browser, if possible
    webbrowser.open_new_tab(a_website)

    webbrowser.open(a_website, 1)  # Equivalent to: webbrowser.open_new(a_website)

