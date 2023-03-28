from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Icons')
root.iconbitmap('mcme.ico')



my_img = ImageTk.PhotoImage(Image.open("me.png").resize((300, 300)))
myLabel = Label(image=my_img,)
myLabel.pack()



btn_quit = Button(root, text="Exit Program", command=root.quit)
btn_quit.pack()

root.mainloop()