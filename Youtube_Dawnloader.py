#Warning!!!
#The sound of the videos is of very good quality but the graphics are of very poor quality.

from tkinter import *
from pytube import YouTube

window = Tk()

window.configure(bg='red')
window.title('YOUTUBE VIDEO DOWNLOADER')

window.geometry('500x400')
window.resizable(False,False)

Label(window, text='Youtube Video Downloader', font='Times 20 bold', bg='red',fg='white').place(x=85,y=30)

link = StringVar()

Label(window, text='Paste Link Here:', font='Times 15 bold', bg='red',fg='white').place(x=160,y=90)

link_entry = Entry(window, width=70, textvariable= link).place(x=32,y=120)

def download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(window, text='DOWNLOADED', font='Times 15', fg='white', bg='red').place(x=178, y=240)

Button(window,text = 'DOWNLOAD', font = 'Times 15 bold' ,bg = 'white',fg='red', padx = 2, command=download).place(x=180 ,y = 180)

window.mainloop()