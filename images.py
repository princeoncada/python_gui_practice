from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')
root.iconbitmap('images/mcme.ico')

cur_img = 0

img1 = ImageTk.PhotoImage(Image.open("images/1.png").resize((500, 500)))
img2 = ImageTk.PhotoImage(Image.open("images/2.png").resize((500, 500)))
img3 = ImageTk.PhotoImage(Image.open("images/3.png").resize((500, 500)))
img4 = ImageTk.PhotoImage(Image.open("images/4.png").resize((500, 500)))
img5 = ImageTk.PhotoImage(Image.open("images/5.png").resize((500, 500)))

image_list = [img1, img2, img3, img4, img5]

my_label = Label(image=image_list[cur_img])
my_label.grid(row=0, column=0, columnspan=3)

def check():
    global cur_img
    
    status = Label(root, text=f"Image {cur_img+1} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E, padx=10, pady=5)
    
    if(cur_img == 0):
        button_back = Button(root, text="<<", command=lambda: back(), state=DISABLED)
    else:
        button_back = Button(root, text="<<", command=lambda: back())
        
    if(cur_img == 4):
        button_forward = Button(root, text=">>", command=lambda: forward(), state=DISABLED)
    else:
        button_forward = Button(root, text=">>", command=lambda: forward())
        
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2, pady=10)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
    
def forward():
    global my_label
    global cur_img
    
    if cur_img < 4:
        cur_img = cur_img + 1
        my_label.grid_forget()
        my_label = Label(image=image_list[cur_img])
        my_label.grid(row=0, column=0, columnspan=3)
        check()

def back():
    global my_label
    global cur_img
    
    if cur_img > 0:
        cur_img = cur_img - 1
        my_label.grid_forget()
        my_label = Label(image=image_list[cur_img])
        my_label.grid(row=0, column=0, columnspan=3)
        check()

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.grid(row=1, column=1)
check()

root.mainloop()