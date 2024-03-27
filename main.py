import os
from tkinter import *
from pytube import YouTube

# Create an executable file using pyinstaller
# pyinstaller --onefile --windowed main.py

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Youtube Video Downloader")
root.configure(bg='#AACDE2')

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold', bg='#AACDE2').place(x=90,y=30)
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold', bg='#AACDE2').place(x=190,y=90)
link_enter = Entry(root, width = 70, textvariable = link).place(x=32, y=120)

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    # Set the download path to the Downloads folder
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    video.download(download_path)
    Label(root, text = 'DOWNLOADED', font = 'arial 15', bg='#AACDE2').place(x=180,y=240)

Button(root, text = 'DOWNLOAD', font = 'arial 15 bold', bg = 'pale violet red', padx = 2, command = Downloader).place(x=180, y=180)

root.mainloop()
