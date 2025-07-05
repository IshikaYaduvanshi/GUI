from tkinter import *
from PIL import Image ,ImageTk
root=Tk()
root.geometry("723x623")
image=Image.open("tkinter/shiv.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
root.mainloop()
