import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import Tk


password = ''

root = Tk()

def easy_pass():
    global password
    for x in range(8):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    messagebox.showinfo(title='Generated password', message=password)


def medium_pass():
    global password
    for x in range(16):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    messagebox.showinfo(title='Generated password', message=password)

def strong_pass():
    global password
    for x in range(32):
        password = password + random.choice(string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
    messagebox.showinfo(title='Generated password', message=password)

root['bg'] = '#fafafa'
root.title ('PassGenerator_3.0')
root.geometry ('350x150')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=150, width=350)
canvas.pack()

frame = Frame(root, bg='pink')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Please choose type of passcode', bg='red', font=20)

Easy_but = Button(frame, text='Easy', bg='green', command=easy_pass)
Medium_but = Button(frame, text='Medium', bg='yellow', command=medium_pass)
Strong_but = Button(frame, text='Strong', bg='red', command=strong_pass)

Easy_but.place(x=40, y=30, width=75, height=75)
Medium_but.place(x=136, y=30, width=75, height=75)
Strong_but.place(x=232, y=30, width=75, height=75)

root.mainloop()