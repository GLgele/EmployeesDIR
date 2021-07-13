import dill as pickle
import tkinter
import configparser
import json
import sys,os
import time

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
        exceptionBox(err)

#信息导出
def save_data(filename = "Employees.txt"):
    try:
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        #gui.msgbox("文件已保存","文件保存","确认")

    except BaseException as err:
        #gui.exceptionbox(err,title)
        exceptionBox(err)

def exceptionBox(msg):
    exp_win = tkinter.Tk()
    exp_win.title(title)
    exp_win.geometry("400x600")
    exp_text = tkinter.Text(exp_win,width=60,height=35)
    exp_text.insert(tkinter.INSERT,"Error!Here's the report:\n"+msg)
    exp_text.grid(column=1,row=1)
    ok_button = tkinter.Button(exp_win,text="OK",command=exp_win.destroy)
    ok_button.grid(column=1,row=3)
    exp_win.mainloop()

def logInit():
    try:
        log = open("latest.log","w")
        log.close()
    except BaseException as err:
        print(ntime,"Can't init log functions!",err)
        exceptionBox("Can't init log functions!\n"+err)

def logOut(*msg):
    ntime = time.strftime("[%H:%M:%S]:", time.localtime()) 
    try:
        log = open("latest.log","a")
    except BaseException as err:
        print(ntime,"Can't init log functions!",err)
        exceptionBox("Can't init log functions!\n"+err)
    stri = str(msg)
    stri = stri.replace("(","")
    stri = stri.replace(")","")
    stri = stri.replace("'","")
    stri = stri.replace(","," ")
    stri = stri.replace("\\n","\n")
    print(ntime,stri)
    log.write(ntime+stri+"\n")
    log.close()

def transInit():
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
        logOut("Error:Unknown language file!\n",err)
        exceptionBox("Unknown languagefile!\n"+err)
    logOut("Using language:",tlang)

    langFile = open(lang,"r")
    langList = json.load(langFile)
    langFile.close()
    return langList

#翻译
def trans(stri,langList):
    temps = ""
    try:
        temps = langList[0][str(stri)]
    except BaseException as err:
        temps = stri
        logOut("Load langList failed:",err)
        exceptionBox("Load langlist failed:\n"+err)
    return temps

def safeExit():
    logOut("Safe exit.")
    sys.exit(0)

global employees
global title
global retval
#global langList
'''
global user
global pwd
''''''
user = tkinter.StringVar()
pwd = tkinter.StringVar()'''
employees = []
retval = 0
title = "EmployeesDIR - 3.0"
