import random
import string
from tkinter import *
from tkinter import messagebox
from tkinter import Tk

root = Tk()
password = ''

def back():
    pass


def copy():
    pass


def easy_pass():
    global password
    if password == '':
        for x in range(8):
            password = password + random.choice(
                string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
            print(password)
    else:
        password = ''

    frame_2 = Frame(frame, bg='green')
    frame_2.place(relwidth=1, relheight=1)

    easy_text = Label(frame_2, text="Your generated password is\n", bg='orange', fg='white')
    easy_text.pack()
    easy_text = Text(frame_2, height=30, width=70)

    back_button = Button(frame, text='Back', bg='white', command=back)
    back_button.place(x=50, y=100, width=100, height=50)

    copy_button = Button(frame, text='Copy', bg='white')
    copy_button.place(x=200, y=100, width=100, height=50)


def medium_pass():
    global password
    if password == '':
        for x in range(16):
            password = password + random.choice(
                string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
        messagebox.showinfo(title='Generated password', message=password)
    else:
        password = ''


def strong_pass():
    global password
    if password == '':
        for x in range(32):
            password = password + random.choice(
                string.ascii_uppercase + string.punctuation + string.ascii_lowercase + string.digits)
        messagebox.showinfo(title='Generated password', message=password)
    else:
        password = ''


root['bg'] = '#fafafa'
root.title('PassGenerator_3.0')
root.geometry('350x250')

# root.resizable(width=False, height=False)
frame = Frame(root, bg='pink')
frame.place(relwidth=1, relheight=1)

text = Label(frame, text="Please choose type of passcode", bg='pink')

Easy_but = Button(frame, text='Easy', bg='green', command=easy_pass)
Medium_but = Button(frame, text='Medium', bg='yellow', command=medium_pass)
Strong_but = Button(frame, text='Strong', bg='red', command=strong_pass)

text.place(x=70, y=0)
Easy_but.place(x=40, y=30, width=75, height=75)
Medium_but.place(x=136, y=30, width=75, height=75)
Strong_but.place(x=232, y=30, width=75, height=75)

root.mainloop()