from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("SoftUni Python Clock")

def clock():
    tick = strftime("%H:%M:%S %p")
    label.config(text=tick)
    label.after(1000, clock)  # Fixed: removed "ms=" or you could use "ms=1000"

label = Label(root, font=("sans", 100), background="LightBlue1", foreground="AntiqueWhite4")
label.pack(anchor="center")
clock()
mainloop()