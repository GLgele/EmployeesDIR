import sys, os
import dill as pickle
import easygui as gui

#类定义
class Employee(object):
    #__slots__ = ["name","number","comment","email","sex","salary","edu"]
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
        global retval
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
    
    #员工显示
    def show(self):
        print("姓名:", self.name)
        print("性别:", self.sex)
        print("电话号码:", self.number)
        print("备注:", self.comment)
        print("邮箱:", self.email)
        print("学历:", self.edu)
        print("薪水:",self.salary)
        


    #def showname(self):
        #print(self.name,end = "")

#信息导入
def load_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "rb")
        employees = pickle.load(file_data)
        file_data.close()
        gui.msgbox("文件已加载","文件加载","确认")

    except OSError as err:
        #print("文件打开失败！错误代码:")
        #print(err)
        #input("\n按回车继续...")
        gui.exceptionbox()

#信息导出
def save_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        gui.msgbox("文件已保存","文件保存","确认")

    except OSError as err:
        #print("文件打开失败！错误代码：")
        #print(err)
        #input("\n按回车继续...")
        gui.exceptionbox()

global retval
retval = 0
employees = []
choice = 0
#global retval

#if len(sys.argv) == 1:
#    print("No filename specified - starting with empty data")
#    input("Hit enter to continue...")
#else:
#    load_data(sys.argv[1])

#load_data()

'''
while choice != 9:                  
    if sys.platform == "win32":     #清屏
        os.system("cls")
    else:
        os.system("clear")

    #界面显示
    print("========== 员工目录管理系统 2.2 ==========\n")
    print("==========    汉化by：GL哥勒    ==========\n")
    print(" 1. 查看所有的员工")
    print(" 2. 添加员工")
    print(" 3. 删除员工")
    print(" 4. 查找员工")
    print(" 5. 保存员工目录")
    print(" 6. 加载员工目录")
    print(" 7. 修改员工信息")
    print(" 8. 删除所有员工")
    print(" 9. 退出系统")


    choice = int(input("\n请选择操作: "))

    if choice == 1:
        for x in range(0, len(employees)):
            print("\n员工序号:", x + 1)
            employees[x].show()
        input("\n按回车继续...")

    elif choice == 2:
        name = input("\n请输入员工名称: ")
        sex = input("请输入员工性别:")
        number = input("请输入员工电话: ")
        comment = input("请输入员工备注: ")
        email = input("请输入员工邮箱: ")
        edu = input("请输入员工学历:")
        salary = input("请输入员工薪水:")
        employees.append(Employee(name,sex,number,comment,email,edu,salary))
        input("\n员工已添加，按回车继续...")

    elif choice == 3:
        number = int(input("\n请输入员工序号（输入0删除最后一个员工）: "))
        if number > len(employees):
            input("错误：没有这个序号！按回车继续...")
        else:
            del employees[number - 1]
            input("\n员工已删除，按回车继续...")

    elif choice == 4:
        print("\n支持部分查询，如：输入au查找所有 名称 或 电话号码 或 备注 或 邮箱 等信息中含有au的人")
        search_term = input("请输入员工名称 或 电话号码 或 备注 或 邮箱或其它信息: ")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            if result == 1:
                print("\n员工序号:", x + 1)
                employees[x].show()
            elif result == 0:
                print("\n没有找到含有该信息的员工！")
        input("按回车继续...")

    elif choice == 5:
        filename = input("\n输入文件名（将保存在同一目录）（建议保存为Employees.txt): ")
        #if filename == "" or filename == " ":
        #    save_data()
        save_data(filename)

    elif choice == 6:
        filename = input("\n输入文件名（请把文件放在同一目录下）（建议保存为Employees.txt): ")
        #if filename == "" or filename == " ":
        #    load_data()
        load_data(filename)
    elif choice == 7:
        search_term = input("请输入员工姓名")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            x = x+1
        if result == 1:
            print("员工序号：",x)
            #print("员工姓名：")
            #Employee.showname(x)
            print("请选择操作：")
            print(" 1. 修改姓名")
            print(" 2. 修改性别")
            print(" 3. 修改电话")
            print(" 4. 修改备注")
            print(" 5. 修改邮箱")
            print(" 6. 修改学历")
            print(" 7. 修改薪水")
            print(" 8. 离开")
            retval = int(input("请选择操作："))
            if retval == 8:
                input("\n按回车继续...")
            elif retval <8:
                employees[x-1].setinfo()
            else:
                print("错误的操作！")
                input("\n按回车继续...")
        elif result == 0:
            print("\n没有找到含有该信息的员工！")
    elif choice == 8:
        print("1. 确定\n 0. 返回")
        i = input("确定吗？")
        if i != 0:
            for x in range(0, len(employees)):
                del employees[x]
            input("已删除，按回车继续...")
        else:
            input("按回车继续...")
    elif choice == 9:
        sys.exit(0)
    else:
        print("错误的操作！")
        input("\n按回车继续...")
        continue

'''

while choice != 9:
    choice = gui.indexbox("请选择操作","EmployeesDIR - 2.3",("查看所有员工","添加员工","删除员工","查找员工","保存员工目录","读取员工目录","修改员工信息","删除所有员工","退出系统")) + 1
    if choice == 1:
        for x in range(0, len(employees)):
            gui.msgbox(employees[x].__dict__,"查看员工","确认")
        #    print("\n员工序号:", x + 1)
        #    employees[x].show()
        #input("\n按回车继续...")
    elif choice == 2:
        name = gui.enterbox("\n请输入员工名称: ","新增员工")
        sex = gui.enterbox("请输入员工性别: ","新增员工")
        number = gui.enterbox("请输入员工电话: ","新增员工")
        comment = gui.enterbox("请输入员工备注: ","新增员工")
        email = gui.enterbox("请输入员工邮箱: ","新增员工")
        edu = gui.enterbox("请输入员工学历: ","新增员工")
        salary = gui.enterbox("请输入员工薪水: ","新增员工")
        employees.append(Employee(name,sex,number,comment,email,edu,salary))
        #input("\n员工已添加，按回车继续...")

    elif choice == 3:
        number = int(gui.enterbox("\n请输入员工序号（输入0删除最后一个员工）: ","删除员工"))
        if number > len(employees):
            gui.msgbox("错误：没有这个序号！","删除员工","确认")
        else:
            del employees[number - 1]
            gui.msgbox("\n员工已删除","删除员工","确认")

    elif choice == 4:
        search_term = gui.enterbox("\n支持部分查询，如：输入au查找所有 名称 或 电话号码 或 备注 或 邮箱 等信息中含有au的人 \n 请输入员工名称 或 电话号码 或 备注 或 邮箱或其它信息: ","员工查找")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            if result == 1:
                #print("\n员工序号:", x + 1)
                #employees[x].show()
                gui.msgbox(employees[x].__dict__,"查找员工","确认")
                continue
            elif result == 0:
                gui.msgbox("\n没有找到含有该信息的员工！","查找员工","确认")
        #input("按回车继续...")

    elif choice == 5:
        #filename = input("\n输入文件名（将保存在同一目录）（建议保存为Employees.txt): ")
        filename = gui.filesavebox("请选择要保存的文件","文件保存","","*.txt")
        #if filename == "" or filename == " ":
        #    save_data()
        save_data(filename)

    elif choice == 6:
        filename = gui.fileopenbox("请选择要加载的文件","文件加载","","*.txt")
        #filename = input("\n输入文件名（请把文件放在同一目录下）（建议保存为Employees.txt): ")
        #if filename == "" or filename == " ":
        #    load_data()
        load_data(filename)
    elif choice == 7:
        search_term = gui.enterbox("请输入员工姓名","员工信息修改")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            x = x+1
        if result == 1:
            #print("员工序号：",x)
            #print("员工姓名：")
            #Employee.showname(x)
            #print("请选择操作：")
            #print(" 1. 修改姓名")
            #print(" 2. 修改性别")
            #print(" 3. 修改电话")
            #print(" 4. 修改备注")
            #print(" 5. 修改邮箱")
            #print(" 6. 修改学历")
            #print(" 7. 修改薪水")
            #print(" 8. 离开")
            retval = int(gui.indexbox("请选择操作","员工信息修改",("修改姓名","修改性别","修改电话","修改备注","修改邮箱","修改学历","修改薪水","离开")) + 1)
            #if retval == 8:
                #input("\n按回车继续...")
            if retval <8:
                employees[x-1].setinfo()
            #else:
            #    print("错误的操作！")
            #    input("\n按回车继续...")
        elif result == 0:
            gui.msgbox("没有找到含有该信息的员工！","员工信息修改","确认")
    elif choice == 8:
        #print("1. 确定\n 0. 返回")
        #i = input("确定吗？")
        i = gui.indexbox("确定吗？","员工信息修改",("确认","返回"))
        if i == 0:
            for x in range(0, len(employees)):
                del employees[x-1]
                x = x + 1
            gui.msgbox("已删除","员工信息修改","确认")
        #else:
            #input("按回车继续...")
    elif choice == 9:
        sys.exit(0)
    #else:
        #print("错误的操作！")
        #input("\n按回车继续...")
        #continue
