import tkinter

from general import *

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
