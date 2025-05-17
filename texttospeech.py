import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3

root = Tk()
root.title("TEXT TO SPEECH")
root.geometry("900x950+100+100")
root.resizable(TRUE, TRUE)
root.configure(bg="#F5F5DC")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END)
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    if speed == 'FAST':
        engine.setProperty('rate', 250)
    elif speed == 'SLOW':
        engine.setProperty('rate', 125)
    else:
        engine.setProperty('rate', 175)

    engine.say(text)
    engine.runAndWait()

def download():
    text = text_area.get(1.0, END)
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    if speed == 'FAST':
        engine.setProperty('rate', 250)
    elif speed == 'SLOW':
        engine.setProperty('rate', 125)
    else:
        engine.setProperty('rate', 175)

    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
    if file_path:
        engine.save_to_file(text, file_path)
        engine.runAndWait()

image_icon = PhotoImage(file="C:/Users/divya/Desktop/voice/spk.png")
root.iconphoto(False, image_icon)

Top_frame = Frame(root, bg="#F5F5DC", width=2000, height=1000)
Top_frame.place(x=0, y=0)
Label(root, text="Enter the text to convert into speech:", font="arial 14", bg="#F5F5DC", fg="black").place(x=10, y=115)

Logo = PhotoImage(file="C:/Users/divya/Desktop/voice/file.png")
Label(Top_frame, image=Logo, bg="#F5F5DC").place(x=10, y=10)

Label(Top_frame, text="TEXT TO SPEECH", font="arial 20", bg="#F5F5DC", fg="black").place(x=200, y=50)

text_area = Text(root, font="Robote 20", bg="#F5F5DC", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=500, height=250)

Label(root, text="SPEED", font="arial 15 bold", bg="#F5F5DC").place(x=760, y=160)

speed_combobox = Combobox(root, values=['FAST', 'NORMAL', 'SLOW'], font="arial 14", state='r', width=8)
speed_combobox.place(x=730, y=200)
speed_combobox.set('NORMAL')

imageicon = PhotoImage(file="C:/Users/divya/Desktop/voice/person.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=155, bg="#F5F5DC", font="arial 14", command=speaknow)
btn.place(x=555, y=280)

imageicon2 = PhotoImage(file="C:/Users/divya/Desktop/voice/download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=150, bg="#F5F5DC", font="arial 14", command=download)
save.place(x=750, y=280)

root.mainloop()
