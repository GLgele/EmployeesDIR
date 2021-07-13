import sys,os

from general import *
from login import *

logInit()
login_window()
exceptionBox("test")

'''
global root_win
root_win = tkinter.Tk()
root_win.title(title)
root_win.geometry("640x480")

main_menu = tkinter.Menu(root_win)
root_win.config(menu = main_menu)

file_menu = tkinter.Menu(main_menu)
main_menu.add_cascade(label = "File",menu = file_menu)

root_win.mainloop()
'''
