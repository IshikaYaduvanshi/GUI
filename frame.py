from  tkinter import *
root=Tk()
root.geometry("765x654")
f1=Frame(root,bg="red",borderwidth=6)   #command for frame
l1=Label(f1,text="project")
l1.pack()
f1.pack(side=LEFT)                     #position where the frame will palce

root.mainloop()


