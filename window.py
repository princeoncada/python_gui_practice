from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Windows')
root.iconbitmap('images/mcme.ico')

img1 = ImageTk.PhotoImage(Image.open('images/1.png').resize((300, 300)))
img2 = ImageTk.PhotoImage(Image.open('images/2.png').resize((300, 300)))
img3 = ImageTk.PhotoImage(Image.open('images/3.png').resize((300, 300)))
img4 = ImageTk.PhotoImage(Image.open('images/4.png').resize((300, 300)))
img5 = ImageTk.PhotoImage(Image.open('images/5.png').resize((300, 300)))

image_list = [img1, img2, img3, img4, img5]

def open(num):
    global image_list
    top = Toplevel()
    top.title('Image Window')
    top.iconbitmap('images/mcme.ico')
    Label(top, image=image_list[num]).pack()
    btn2 = Button(top, text='close window', command=top.destroy)
    btn2.pack()

btn1 = Button(root, text='Open Image 1 Window', command=lambda: open(0))
btn2 = Button(root, text='Open Image 2 Window', command=lambda: open(1))
btn3 = Button(root, text='Open Image 3 Window', command=lambda: open(2))
btn4 = Button(root, text='Open Image 4 Window', command=lambda: open(3))
btn5 = Button(root, text='Open Image 5 Window', command=lambda: open(4))

btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()

root.mainloop()