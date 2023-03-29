from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Buttons')
root.iconbitmap('images/mcme.ico')

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Mushrooms", "Mushrooms"),
    ("Onion", "Onion")
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, topping in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=topping, command=lambda: clicked(pizza.get())).pack(anchor=W)

def clicked(value):
    global myLabel
    myLabel.pack_forget()
    myLabel = Label(root, text=value)
    myLabel.pack()

myLabel = Label(root, text=pizza.get())
myLabel.pack()

root.mainloop()