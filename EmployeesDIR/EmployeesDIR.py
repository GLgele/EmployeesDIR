import sys, os
import dill as pickle

class Employee(object):
    def __init__(self, passed_name, passed_number, passed_comment,passed_email):
        self.name = passed_name
        self.number = passed_number
        self.comment = passed_comment
        self.email = passed_email

    def find(self, search_term):
        if self.name.lower().find(search_term.lower()) != -1:
            return 1
        elif self.number.lower().find(search_term.lower()) != -1:
            return 1
        elif self.comment.lower().find(search_term.lower()) != -1:
            return 1
        elif self.email.lower().find(search_term.lower()) != -1:
            return 1
        else:
            return 0

        def setinfo(self):
            global retval
            if retval == 1:
                self.name = input("请输入姓名")
            elif retval == 2:
                self.number = input("请输入电话号码")
            elif retval == 3:
                self.comment == input("请输入备注")
            elif retval == 4:
                self.email == input("请输入邮箱")

    def show(self):
        print("姓名:", self.name)
        print("电话号码:", self.number)
        print("备注:", self.comment)
        print("邮箱:", self.email)


    #def showname(self):
        #print(self.name,end = "")

def load_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "rb")
        employees = pickle.load(file_data)
        file_data.close()
        input("\n文件已加载，按回车继续...")

    except OSError as err:
        print("文件打开失败！错误代码:")
        print(err)
        input("\n按回车继续...")

def save_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        input("\n文件已保存，按回车继续...")

    except OSError as err:
        print("文件打开失败！错误代码：")
        print(err)
        input("\n按回车继续...")

employees = []
choice = 0
#global retval

#if len(sys.argv) == 1:
#    print("No filename specified - starting with empty data")
#    input("Hit enter to continue...")
#else:
#    load_data(sys.argv[1])

load_data()
while choice != 8:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("========== 员工目录管理系统 2.1 ==========\n")
    print("==========    汉化by：GL哥勒    ==========\n")
    print(" 1. 查看所有的员工")
    print(" 2. 添加员工")
    print(" 3. 删除员工")
    print(" 4. 查找员工")
    print(" 5. 保存员工目录")
    print(" 6. 加载员工目录")
    print(" 7. 修改员工信息")
    print(" 8. 退出系统")


    choice = int(input("\n请选择操作: "))

    if choice == 1:
        for x in range(0, len(employees)):
            print("\n员工序号:", x + 1)
            employees[x].show()
        input("\n按回车继续...")

    elif choice == 2:
        name = input("\n请输入员工名称: ")
        number = input("请输入员工电话: ")
        comment = input("请输入员工备注: ")
        email = input("请输入员工邮箱: ")
        employees.append(Employee(name, number, comment, email))
        input("\n员工已添加，按回车继续...")

    elif choice == 3:
        number = int(input("\n请输入员工序号（输入0删除最后一个员工）: "))
        if number > len(employees):
            input("错误：没有这个序号！按回车继续...")
        else:
            del employees[number - 1]
            input("\n员工已删除，按回车继续...")

    elif choice == 4:
        print("\n支持部分查询，如：输入au查找所有 名称 或 电话号码 或 备注 或 邮箱 含有au的人")
        search_term = input("请输入员工名称 或 电话号码 或 备注 或 邮箱: ")
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
            print(" 2. 修改电话")
            print(" 3. 修改备注")
            print(" 4. 修改邮箱")
            print(" 5. 离开")
            retval = int(input("请选择操作："))
            if retval == 5:
                input("\n按回车继续...")
            elif retval <5:
                employees[x-1].setinfo()
            else:
                print("错误的操作！")
                input("\n按回车继续...")
        elif result == 0:
            print("\n没有找到含有该信息的员工！")
    elif choice == 8:
        sys.exit(0)
    else:
        print("错误的操作！")
        input("\n按回车继续...")
        continue