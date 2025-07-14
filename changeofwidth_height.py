from tkinter import*
root=Tk()
root.geometry("300x200")

def update():
    print(f"width is {width.get()} and height is {height.get()}")
    root.geometry(f"{width.get()}x{height.get()}")                   #koi space nhi hoga chiye ....

    
Label(root,text="width").grid(row=1,column=1)
Label(root,text="height").grid(row=2,column=1)

width=StringVar()
height=StringVar()

widthentry=Entry(root,textvariable=width).grid(row=1,column=2)
heightentry=Entry(root,textvariable=height).grid(row=2,column=2)

Button(text="apply",bg="green",command=update).grid()
root.mainloop()