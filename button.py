from tkinter import *
root=Tk()
root.geometry("655x333")       
def tell():                                # to call the command
    name=input("enter your name:")
    print(name)
frame=Frame(root,borderwidth=6,bg="red",relief=SUNKEN)  
frame.pack(side=LEFT)
b1=Button(text="OK" , bg="yellow"  )
b2=Button(text="tell me ur name" , bg="yellow" ,command=tell )
b1.pack(side=LEFT ,anchor="nw",padx=6)
b2.pack(side=LEFT ,anchor="nw")
root.mainloop()
