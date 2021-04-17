from tkinter import *
import time

root = Tk()
root.title('Saat')


def clock():
    text = time.strftime('%H:%M:%S')
    label.config(text=text)
    label.after(1000, clock)


label = Label(root, font=("ds-digital", 100), background="blue", foreground="white")
label.pack(anchor="center")

clock()

mainloop()
