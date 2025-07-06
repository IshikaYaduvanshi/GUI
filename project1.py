from tkinter import *
root=Tk()
root.geometry("234x300")        
root.title("ishika")
def helo():
    print("Hello")
def wel():
    print("welcome to my GUI")
def name():
    print("i am ishika here ")
def sub():
    print("i like python")
b1=Button(text="hello",bg="yellow",command=helo)
b2=Button(text="welcome",bg="yellow", command=wel)
b3=Button(text="name",bg="yellow",command=name)
b4=Button(text="like",bg="yellow",command=sub)
b1.pack(side=LEFT ,anchor="nw")
b2.pack(side=LEFT,anchor="nw")
b3.pack(side=LEFT,anchor="nw")
b4.pack(side=LEFT,anchor="nw" )

root.mainloop()