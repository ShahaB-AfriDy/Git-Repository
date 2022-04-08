from tkinter import *
from datetime import datetime


win = Tk()

win.title("Equal != equal")
win.geometry("500x400")
win.config(background='steelblue')
label = Label(win,bg='steelblue',font=('Arial',50,'bold'))
label.pack(pady=145)

def Clock():
    Now = datetime.now().strftime('%I:%M:%S %p')
    label.configure(text=Now,fg='black')
    label.after(1000,Clock)

Clock()
win.mainloop()