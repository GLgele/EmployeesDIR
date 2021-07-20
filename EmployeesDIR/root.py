import tkinter

from general import *

def root_window():
    root_win = tkinter.Tk()
    root_win.title(title)
    root_win.geometry("640x480")
    langList = transInit()

    main_menu = tkinter.Menu(root_win)
    root_win.config(menu = main_menu)
    file_menu = tkinter.Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label = trans("File",langList),menu = file_menu)

    file_menu.add_command(label=trans("Save",langList),command=save_data_window)
    file_menu.add_command(label=trans("Load",langList),command=load_data_window)
    file_menu.add_command(label=trans("Exit",langList),command=onClosing)

    root_win.protocol("WM_DELETE_WINDOW", onClosing)
    root_win.mainloop()