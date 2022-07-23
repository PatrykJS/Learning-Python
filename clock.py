from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("An Time Describer :)")
root.geometry("298x60")
root.resizable(False, False)

def time():
    string = strftime("%H:%M:%S %p")
    label.config(text=string)
    label.after(1000, time)


label = Label(root, font=("times new roman", 42), background="black", foreground="white")
label.pack(anchor=CENTER)
time()
root.mainloop()
