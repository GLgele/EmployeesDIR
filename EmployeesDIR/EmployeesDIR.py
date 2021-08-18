import sys,os
import tkinter

import general
#from login import *
#from root import *

global employees
global title
global namelist
general.employees = []
retval = 0
title = "EmployeesDIR - 3.0"
namelist = []
saveFlag = 0

def login():
    logOut("loginButton pushed.")
    logOut("User: %s\nPassword: %s"%(user.get(),pwd.get()))
    emptyLabel3 = tkinter.Label(login_win,text = "").grid(column = 2,row = 5)
    if user.get() == "admin" and pwd.get() == "admin":
        logOut("Admin Logged in.")
        login_win.destroy()
    else:
        emptyLabel3 = tkinter.Label(login_win,text = trans("Wrong username or password!",langList),fg = "red").grid(column = 2,row = 5)
         
def login_window():
    global login_win
    global user
    global pwd
    global langList
    langList = transInit()
    login_win = tkinter.Tk()
    login_win.title(title)
    login_win.geometry("400x250")
    user = tkinter.StringVar()
    pwd = tkinter.StringVar()
    emptyTabel1 = tkinter.Label(login_win,text = "\n             ").grid(column = 0,row = 0)
    login_label = tkinter.Label(login_win,text = trans("UserLogin",langList)).grid(column = 1,row = 1)
    user_label = tkinter.Label(login_win,text = trans("User:",langList)).grid(column = 1,row = 2)
    user_entry = tkinter.Entry(login_win,width = 24,textvariable = user).grid(column = 2,row = 2)
    pwd_label = tkinter.Label(login_win,text = trans("Password:",langList)).grid(column = 1,row = 3)
    pwd_entry = tkinter.Entry(login_win,width = 24,textvariable = pwd,show = '*').grid(column = 2,row = 3)
    emptyTabel2 = tkinter.Label(login_win,text = "\n\n\n").grid(column = 0,row = 4)
    cancelButton = tkinter.Button(login_win,text = trans("Cancel",langList),command = safeExit).grid(column = 1,row = 4)
    loginButton = tkinter.Button(login_win,text = trans("Login",langList),command = login,).grid(column = 2,row = 4)
    login_win.mainloop()

def flush_namelist():
    global employees
    global namelist
    global saveFlag
    saveFlag = 1
    namelist = []
    for i in range(0,len(general.employees)):
        info = general.employees[i]
        namelist.append(info.name)
    return namelist

def viewAll():
    view_all_win = tkinter.Tk()
    view_all_win.title(general.fileName)
    view_all_win.geometry("600x400")
    sb = tkinter.Scrollbar(view_all_win)    #垂直滚动条组件
    sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #设置垂直滚动条显示的位置
    namelist_box = tkinter.Listbox(view_all_win,height=25,yscrollcommand=sb.set)    #Listbox组件添加Scrollbar组件的set()方法
    '''for i in range(1000):
        namelist_box.insert(tkinter.END,i)'''
    namelist_box.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
    #namelist_box.grid(column=1,row=1)
    nameList = flush_namelist()
    for i in nameList:
        namelist_box.insert(tkinter.END,i)
    sb.config(command=namelist_box.yview) #设置Scrollbar组件的command选项为该组件的yview()方法


def root_window():
    global namelist
    root_win = tkinter.Tk()
    root_win.title(title)
    root_win.geometry("640x480")
    langList = general.transInit()

    main_menu = tkinter.Menu(root_win)
    root_win.config(menu = main_menu)
    file_menu = tkinter.Menu(main_menu,tearoff=False)
    view_menu = tkinter.Menu(main_menu,tearoff=False)
    main_menu.add_cascade(label = general.trans("File",langList),menu = file_menu)
    main_menu.add_cascade(label = general.trans("View",langList),menu = view_menu)

    file_menu.add_command(label=general.trans("Save",langList),command=general.save_data_window)
    file_menu.add_command(label=general.trans("Load",langList),command=general.load_data_window)
    file_menu.add_command(label=general.trans("Exit",langList),command=general.onClosing)
    view_menu.add_command(label=general.trans("View All",langList),command=viewAll)



    '''
    #sb = tkinter.Scrollbar(root_win)    #垂直滚动条组件
    #sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #设置垂直滚动条显示的位置
    namelist_box = tkinter.Listbox(root_win,height=25)    #Listbox组件添加Scrollbar组件的set()方法
    for i in range(1000):
	    namelist_box.insert(tkinter.END,i)
    #namelist_box.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
    namelist_box.grid(column=1,row=1)
    #sb.config(command=namelist_box.yview) #设置Scrollbar组件的command选项为该组件的yview()方法
    '''

    root_win.protocol("WM_DELETE_WINDOW", general.onClosing)
    root_win.mainloop()

general.logInit()
#login_window()
#exceptionBox("test")
root_window()

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
