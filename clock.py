from tkinter import *
from time import *
from tkinter import colorchooser
import datetime


def date():
    date1 = strftime("%x")
    label1.config(text=date1)


def time():
    string = strftime("%H:%M:%S")
    label.config(text=string)
    label.after(1000, time)


def click1():
    colour1 = colorchooser.askcolor()
    label.config(background=str(colour1[1]))
    root.config(background=str(colour1[1]))
    label1.config(background=str(colour1[1]))


def click2():
    colour2 = colorchooser.askcolor()
    label.config(foreground=str(colour2[1]))
    label1.config(foreground=str(colour2[1]))


root = Tk()
logo = PhotoImage(file="Icon.png")
root.iconphoto(True, logo)
root.title("An Time Describer :)")
root.config(background="black")
root.resizable(False, False)


label1 = Label(root,
               font=("Digital dream", 15),
               background="black",
               foreground="yellow"
               )

label1.pack(anchor=N)
date()


label = Label(root,
              font=("Digital dream", 42),
              borderwidth=20,
              background="black",
              foreground="yellow",
              )
label.pack(anchor=CENTER)
time()


button1 = Button(root,
                 text="Change background colour",
                 command=click1,
                 font=("Digital dream fat", 8),
                 background="black",
                 foreground="white",
                 border=1
                 )
button1.pack(side=LEFT)


button2 = Button(root,
                 text="Change digits colour",
                 command=click2,
                 font=("Digital dream fat", 8),
                 background="black",
                 foreground="white",
                 border=1

                 )
button2.pack(side=RIGHT)


root.mainloop()
