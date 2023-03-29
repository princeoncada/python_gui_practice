from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Frames')
root.iconbitmap('images/mcme.ico')

frame = LabelFrame(root, text='This is my Frame...', padx=50, pady=50, labelanchor=N)
frame.pack(padx=50, pady=50)

b = Button(frame, text="Button 1")
b2 = Button(frame, text="Button 2")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)

root.mainloop()