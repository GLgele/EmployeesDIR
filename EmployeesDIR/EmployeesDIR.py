import sys, os
import dill as pickle

# "Employee" Class definition
class Employee(object):
    
#init
    def __init__(self, passed_name, passed_number, passed_comment,passed_email,passed_sex,passed_salary,passed_edu):
        self.name = passed_name
        self.number = passed_number
        self.comment = passed_comment
        self.email = passed_email
        self.sex = passed_sex
        self.salary = passed_salary
        self.edu = passed_edu

# "FIND" Function
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
        elif self.edu.lower().find(seatch_term.lower()) != -1:
            return 1
        else:
            return 0

# "INFOSET" Function
    def setinfo(self):
        global retval
        if retval == 1:
            self.name = input("Please input name: ")
        elif retval == 2:
            self.sex = input("Please input sex: ")
        elif retval == 3:
            self.number = input("Please input number: ")
        elif retval == 4:
            self.commet = input("Please input commet: ")
        elif retval == 5:
            self.email = input("Please input email: ")
        elif retval == 6:
            self.edu = input("Please input education: ")
        elif retval == 7:
            self.salary = input("Please input salary: ")
    
# "SHOW EMPLOYEES" Function
    def show(self):
        print("Name:", self.name)
        print("Sex", self.sex)
        print("Number:", self.number)
        print("Commet:", self.comment)
        print("Eemail:", self.email)
        print("Education", self.edu)
        print("Salary",self.salary)
        


    #def showname(self):
        #print(self.name,end = "")

# "FILE LOAD" Function
def load_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "rb")
        employees = pickle.load(file_data)
        file_data.close()
        input("\nFile loaded.Hit enter to continue...")

    except OSError as err:
        print("File couldn't be loaded:")
        print(err)
        input("\nHit enter to continue...")

# "FILE SAVE" Function
def save_data(filename = "Employees.txt"):
    try:
        global employees
        file_data = open(filename, "wb")
        pickle.dump(employees, file_data)
        file_data.close()
        input("\nFile saved.Hit enter to continue...")

    except OSError as err:
        print("File couldn't be opened：")
        print(err)
        input("\nHit enter to continue...")

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

load_data()
while choice != 9:
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")

    print("===== Employee Directory Manager 2.2 =====\n")
    print("======= English language by GLgele =======\n")
    print(" 1. List employees")
    print(" 2. Add employee")
    print(" 3. Delete employee")
    print(" 4. Search employees")
    print(" 5. Save data")
    print(" 6. Load data")
    print(" 7. Set employee's info")
    print(" 8. Detele all Employees")
    print(" 9. Quit")


    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        for x in range(0, len(employees)):
            print("\nEmployee number:", x + 1)
            employees[x].show()
        input("\nHit enter to continue...")

    elif choice == 2:
        name = input("\nEnter employee name: ")
        sex = input("Enter employee sex")
        number = input("Enter employee number: ")
        comment = input("Enter employee commet: ")
        email = input("Enter employee email: ")
        edu = input("Enter employee education")
        salary = input("Enter employee salary")
        employees.append(Employee(name, sex,number, comment, email,edu,salary))
        input("\nEmployee added.Hit enter to continue...")

    elif choice == 3:
        number = int(input("\nEnter employee number to remove: "))
        if number > len(employees):
            input("No such employee! Hit enter to continue...")
        else:
            del employees[number - 1]
            input("\Employee removed.Hit enter to continue...")

    elif choice == 4:
        #print("\nEnter a name, number or comment or somthing else")
        search_term = input("\nEnter a name, number or comment or somthing else: ")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            if result == 1:
                print("\nEmployee number:", x + 1)
                employees[x].show()
            #elif result == 0:
            #   print("\nHit enter to continue...")
        input("Hit enter to continue...")

    elif choice == 5:
        filename = input("\nEnter a filename: ")
        #if filename == "" or filename == " ":
        #    save_data()
        save_data(filename)

    elif choice == 6:
        filename = input("\nEnter a filename: ")
        #if filename == "" or filename == " ":
        #    load_data()
        load_data(filename)
    elif choice == 7:
        search_term = input("Please input employee's name")
        for x in range(0, len(employees)):
            result = employees[x].find(search_term)
            x = x+1
        if result == 1:
            print("Employee number：",x)
            #print("员工姓名：")
            #Employee.showname(x)
            print("Choices：")
            print(" 1. Reset name")
            print(" 2. Reset sex")
            print(" 3. Reset number")
            print(" 4. Reset commet")
            print(" 5. Reset email")
            print(" 6. Reset education")
            print(" 7. Reset salary")
            print(" 8. Quit")
            retval = int(input("Enter your choice："))
            if retval == 8:
                input("\nHit enter to countinue...")
            elif retval <8:
                employees[x-1].setinfo()
            else:
                print("Wrong choice!")
                input("\nHit enter to countinue...")
        elif result == 0:
            print("\nNo such employee!")
    elif choice == 8:
        print("1. Yes\n 0. NO")
        i = input("Are you sure?")
        if i != 0:
            for x in range(0, len(employees)):
                del employees[x]
            input("Emloyees deteled.Hit enter to coutinue...")
        else:
            input("Hit enter to conitnue...")
    elif choice == 9:
        sys.exit(0)
    else:
        print("Wrong choice!")
        input("\nHit enter to cotinue...")
        continue
