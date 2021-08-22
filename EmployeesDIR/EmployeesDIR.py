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

def modifyInfo_(id,win,_name,_sex,_number,_comment,_email,_edu,_salary):
    win.destroy()
    general.employees.insert(id+1,general.Employee(_name.get(),_sex.get(),_number.get(),_comment.get(),_email.get(),_edu.get(),_salary.get()))
    del general.employees[id]

def modifyInfo(id):
    langList = general.transInit()
    _name = tkinter.StringVar()
    _sex = tkinter.StringVar()
    _number = tkinter.StringVar()
    _comment = tkinter.StringVar()
    _email = tkinter.StringVar()
    _edu = tkinter.StringVar()
    _salary = tkinter.StringVar()

    modify_win = tkinter.Tk()
    modify_win.title(title)
    modify_win.geometry("450x250")

    name_label = tkinter.Label(modify_win,text=general.trans("Name",langList)+": ").grid(column=1,row=1)
    name_entry = tkinter.Entry(modify_win,textvariable = _name)
    name_entry.insert(0,general.employees[id].name)
    name_entry.grid(column=2,row=1)
    sex_label = tkinter.Label(modify_win,text=general.trans("Sex",langList)+": ").grid(column=1,row=2)
    sex_entry = tkinter.Entry(modify_win,textvariable = _sex)
    sex_entry.insert(0,general.employees[id].sex)
    sex_entry.grid(column=2,row=2)
    number_label = tkinter.Label(modify_win,text=general.trans("Number",langList)+": ").grid(column=1,row=3)
    number_entry = tkinter.Entry(modify_win,textvariable = _number)
    number_entry.insert(0,general.employees[id].number)
    number_entry.grid(column=2,row=3)
    comment_label = tkinter.Label(modify_win,text=general.trans("Comment",langList)+": ").grid(column=1,row=4)
    comment_entry = tkinter.Entry(modify_win,textvariable = _comment)
    comment_entry.insert(0,general.employees[id].comment)
    comment_entry.grid(column=2,row=4)
    email_label = tkinter.Label(modify_win,text=general.trans("Email",langList)+": ").grid(column=1,row=5)
    email_entry = tkinter.Entry(modify_win,textvariable = _email)
    email_entry.insert(0,general.employees[id].email)
    email_entry.grid(column=2,row=5)
    edu_label = tkinter.Label(modify_win,text=general.trans("Edu",langList)+": ").grid(column=1,row=6)
    edu_entry = tkinter.Entry(modify_win,textvariable = _edu)
    edu_entry.insert(0,general.employees[id].edu)
    edu_entry.grid(column=2,row=6)
    salary_label = tkinter.Label(modify_win,text=general.trans("Salary",langList)+": ").grid(column=1,row=7)
    salary_entry = tkinter.Entry(modify_win,textvariable = _salary)
    salary_entry.insert(0,general.employees[id].salary)
    salary_entry.grid(column=2,row=7)

    cancel_button = tkinter.Button(modify_win,text=general.trans("Cancel",langList),command=modify_win.destroy)
    modify_button = tkinter.Button(modify_win,text=general.trans("Modify",langList),command=lambda : modifyInfo_(id = id,win = modify_win,_name=_name,_sex=_sex,_number=_number,_comment=_comment,_email=_email,_edu=_edu,_salary=_salary))
    cancel_button.grid(column=1,row=8)
    modify_button.grid(column=2,row=8)

    modify_win.mainloop()

def selectEmployee(box):
    result = -1
    langList = general.transInit()
    for x in range(0,len(general.employees)):
        if general.employees[x].name == box.get(box.curselection()):
            result = x
            break
    detail_win = tkinter.Tk()
    detail_win.title(title)
    detail_win.geometry("450x250")
    name_label = tkinter.Label(detail_win,text=general.trans("Name",langList)+": "+box.get(box.curselection()))
    sex_label = tkinter.Label(detail_win,text=general.trans("Sex",langList)+": "+general.employees[result].sex)
    number_label = tkinter.Label(detail_win,text=general.trans("Number",langList)+": "+general.employees[result].number)
    comment_label = tkinter.Label(detail_win,text=general.trans("Comment",langList)+": "+general.employees[result].comment)
    email_label = tkinter.Label(detail_win,text=general.trans("Email",langList)+": "+general.employees[result].email)
    edu_label = tkinter.Label(detail_win,text=general.trans("Edu",langList)+": "+general.employees[result].edu)
    salary_label = tkinter.Label(detail_win,text=general.trans("Salary",langList)+": "+general.employees[result].salary)
    ok_button = tkinter.Button(detail_win,text="OK",command=detail_win.destroy)
    modify_button = tkinter.Button(detail_win,text=general.trans("Modify",langList),command=lambda : modifyInfo(id = x))

    name_label.pack()
    sex_label.pack()
    number_label.pack()
    comment_label.pack()
    email_label.pack()
    edu_label.pack()
    salary_label.pack()
    ok_button.pack()
    modify_button.pack()

def viewAll():
    langList = general.transInit()
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
    nameList = general.flush_namelist()
    for i in nameList:
        namelist_box.insert(tkinter.END,i)
    sb.config(command=namelist_box.yview) #设置Scrollbar组件的command选项为该组件的yview()方法

    select_button = tkinter.Button(view_all_win,text=general.trans("Select",langList),command=lambda : selectEmployee(box = namelist_box))
    select_button.pack()

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
    file_menu.add_command(label=general.trans("Load",langList),command=lambda : general.load_data_window(box = "namelist_box",list=namelist))
    file_menu.add_command(label=general.trans("Exit",langList),command=general.onClosing)
    view_menu.add_command(label=general.trans("View All",langList),command=viewAll)

    '''
    sb = tkinter.Scrollbar(root_win)    #垂直滚动条组件
    sb.pack(side=tkinter.RIGHT,fill=tkinter.Y)  #设置垂直滚动条显示的位置
    namelist_box = tkinter.Listbox(root_win,height=25,yscrollcommand=sb.set)    #Listbox组件添加Scrollbar组件的set()方法
    #for i in range(1000):
	#    namelist_box.insert(tkinter.END,i)
    namelist_box.pack(side=tkinter.LEFT,fill=tkinter.BOTH)
    #namelist_box.grid(column=1,row=1)
    nameList = general.flush_namelist()
    for i in nameList:
        namelist_box.insert(tkinter.END,i)
    sb.config(command=namelist_box.yview) #设置Scrollbar组件的command选项为该组件的yview()方法
    '''
    '''
    select_button = tkinter.Button(root_win,text=general.trans("Select",langList),command=lambda : selectEmployee(box = namelist_box))
    select_button.pack()
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
