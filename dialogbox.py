from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Dialog Boxes')
root.iconbitmap('images/mcme.ico')

my_label = Label(root)
my_image = Label(root)

def open():
    global my_label, my_image, img
    root.filename = filedialog.askopenfilename(initialdir='images', title='Select A File', filetypes=(('png files', '*.png'),('all files', '*.*')))
    
    my_label.pack_forget()
    my_image.pack_forget()
    
    my_label = Label(root, text=root.filename)
    img = ImageTk.PhotoImage(Image.open(root.filename).resize((300, 400)))
    my_image = Label(root, image=img)

    
    my_label.pack()
    my_image.pack()

my_btn = Button(root, text='Open File...', command=open)
my_btn.pack()

root.mainloop()
