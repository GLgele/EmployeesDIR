import sys, os
import dill as pickle

class Employee(object):
    def __init__(self, passed_name, passed_number, passed_comment):
        self.name = passed_name
        self.number = passed_number
        self.comment = passed_comment

    def find(self, search_term):
        if self.name.lower().find(search_term.lower()) != -1:
            return 1
        elif self.number.lower().find(search_term.lower()) != -1:
            return 1
        elif self.comment.lower().find(search_term.lower()) != -1:
            return 1
        else:
            return 0

    def show(self):
        print("姓名:", self.name)
        print("电话号码:", self.number)
        print("备注:", self.comment)

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
        sys.exit(1)

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

#if len(sys.argv) == 1:
#    print("No filename specified - starting with empty data")
#    input("Hit enter to continue...")
#else:
#    load_data(sys.argv[1])

load_data()
while choice != 7:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("========== 员工目录管理系统 2.0 ==========\n")
    print("==========    汉化by：GL哥勒    ==========\n")
    print(" 1. 查看所有的员工")
    print(" 2. 添加员工")
    print(" 3. 删除员工")
    print(" 4. 查找员工")
    print(" 5. 保存员工目录")
    print(" 6. 加载员工目录")
    print(" 7. 退出系统")

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
        employees.append(Employee(name, number, comment))
        input("\n员工已添加，按回车继续...")

    elif choice == 3:
        number = int(input("\n请输入员工序号（输入0删除最后一个员工）: "))
        if number > len(employees):
            input("错误：没有这个序号！按回车继续...")
        else:
            del employees[number - 1]
            input("\n员工已删除，按回车继续...")

    elif choice == 4:
        search_term = input("\n请输入员工名称或电话号码或备注: ")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            if result == 1:
                print("\n员工序号:", x + 1)
                employees[x].show()
        input("\n按回车继续...")

    elif choice == 5:
        filename = input("\n输入文件名（将保存在同一目录）（不输入将自动保存）: ")
        save_data(filename)

    elif choice == 6:
        filename = input("\n输入文件名（请把文件放在同一目录下）（不输入将读取自动保存的数据）: ")
        load_data(filename)
