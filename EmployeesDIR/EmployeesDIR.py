import sys,os
import tkinter
import json
import configparser
import dill as pickle

class Employee(object):

    #初始化
    def __init__(self, passed_name,passed_sex,passed_number, passed_comment,passed_email,passed_edu,passed_salary):
        self.name = passed_name
        self.sex = passed_sex
        self.number = passed_number
        self.comment = passed_comment
        self.email = passed_email
        self.edu = passed_edu
        self.salary = passed_salary

    #寻找
    def find(self, search_term):
        if self.name.lower().find(search_term.lower()) != -1:
            return 1
        elif self.number.lower().find(search_term.lower()) != -1:
            return 1
        elif self.comment.lower().find(search_term.lower()) != -1:
            return 1
        elif self.email.lower().find(search_term.lower()) != -1:
            return 1
        elif self.sex.lower().find(search_term.lower()) != -1:
            return 1
        elif self.salary.lower().find(search_term.lower()) != -1:
            return 1
        elif self.edu.lower().find(search_term.lower()) != -1:
            return 1
        else:
            return 0

    #信息修改
    def setinfo(self):
        '''
        if retval == 1:
            self.name = gui.enterbox("请输入姓名: ","员工信息修改")
        elif retval == 2:
            self.sex = gui.enterbox("请输入性别: ","员工信息修改")
        elif retval == 3:
            self.number = gui.enterbox("请输入电话号码: ","员工信息修改")
        elif retval == 4:
            self.comment = gui.enterbox("请输入备注: ","员工信息修改")
        elif retval == 5:
            self.email = gui.enterbox("请输入邮箱: ","员工信息修改")
        elif retval == 6:
            self.edu = gui.enterbox("请输入学历: ","员工信息修改")
        elif retval == 7:
            self.salary = gui.enterbox("请输入薪水: ","员工信息修改")
        '''
        pass
    
    #员工显示
    def show(self):
        print("姓名:", self.name)
        print("性别:", self.sex)
        print("电话号码:", self.number)
        print("备注:", self.comment)
        print("邮箱:", self.email)
        print("学历:", self.edu)
        print("薪水:",self.salary)
        

#信息导入
def load_data(filename = "Employees.txt"):
    try:
        file_data = open(filename, "rb")
        employees = pickle.load(file_data)
        file_data.close()
        #gui.msgbox("文件已加载","文件加载","确认")

    except BaseException as err:
        #gui.exceptionbox(err,title)
        pass

#信息导出
def save_data(filename = "Employees.txt"):
    try:
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        #gui.msgbox("文件已保存","文件保存","确认")

    except BaseException as err:
        #gui.exceptionbox(err,title)
        pass

#翻译
def trans(stri):
    temps = ""
    try:
        temps = langList[0][str(stri)]
    except BaseException:
        temps = stri
    return temps

global employees
global title
global retval
global langList
employees = []
title = "EmployeesDIR - 3.0"
retval = 0

conf = configparser.ConfigParser()
conf.read("config.ini",encoding="utf-8")
tlang = conf.items("language")
tlang = tlang[0][1]
try:
    langFile = open("language/"+str(tlang)+".json","r")
    lang = "language/"+str(tlang)+".json"
    langFile.close()
except BaseException as err:
    lang = "language/en_us.json"
    print("Error:Unknown language file!\n",err)
print("Using language:",tlang)

langFile = open(lang,"r")
langList = json.load(langFile)
langFile.close()

login_win = tkinter.Tk()
login_win.title(title)
login_win.geometry("400x200")
user = tkinter.StringVar()
pwd = tkinter.StringVar()
login_label = tkinter.Label(login_win,text = trans("UserLogin")).grid(column = 1,row = 1)
user_label = tkinter.Label(login_win,text = trans("User:")).grid(column = 1,row = 2)
user_entry = tkinter.Entry(login_win,width = 24,textvariable = user).grid(column = 2,row = 2)
pwd_label = tkinter.Label(login_win,text = trans("Password:")).grid(column = 1,row = 3)
pwd_entry = tkinter.Entry(login_win,width = 24,textvariable = pwd,show = '*').grid(column = 2,row = 3)





login_win.mainloop()

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
