from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Message Boxes')
root.iconbitmap('images/mcme.ico')


def popup():
    response = messagebox.askretrycancel('This is my Popup!', 'Hello, world!')
    if response == 1:
        Label(root, text='you clicked retry').pack()
    else:
        Label(root, text='you clicked cancel').pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()