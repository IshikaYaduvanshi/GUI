#use of grid:---

from tkinter import *
root=Tk()
root.geometry("234x200")
user=Label(root,text="username")
psswrd=Label(root,text="password")
user.grid(row=2 ,column=2)
psswrd.grid(row=1,column=3)
root.mainloop()


#use of entry:--

from tkinter import *
root=Tk()
root.geometry("209x234")

def display():
    print(f"the username is {userentry.get()} \n and the password is {pssentry.get()}")  #get is use for sub,it and and display on the terminal screen

user=Label(root,text="username")
pss=Label(root,text="paasword")

user.grid()
pss.grid()

uservalue=StringVar()
pssvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
pssentry=Entry(root,textvariable=pssvalue)

userentry.grid(row=0,column=1)        #use of row  and column
pssentry.grid(row=1,column=1)

a=Button(text="submit" ,bg="yellow" ,command=display )
a.grid()
root.mainloop() 