#Import the library
from tkinter import *
from tkinter import ttk

#Create an instance of tkinter frame
win= Tk()

#Set the window geometry
win.geometry("750x200")

#Create a Label
Label(win, text= "Tkinter is a GUI Library in Python", font=('Helvetica 15 bold')).pack(pady=20)

#Define a function to reset the window size
def reset_win():
   win.wm_geometry("750x250")
   button.destroy()

#Create a Button to Hide/ Reveal the Main Window
button= ttk.Button(win, text="RESET" ,command= reset_win)
button.pack(pady=50)

win.mainloop()