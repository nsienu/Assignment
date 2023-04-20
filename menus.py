from grade import Grade
from load import Load
students = []
teacher = []
def addRecord2():
    while True:
        print()
        id = input('Enter IdNo.: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        department = input('Enter Department: ')
        position =  input('Enter Position: ')
        subject = input('Enter Subject: ')

        teach = Load(subject)
        teach.id = id
        teach.last_name = lastName
        teach.first_name = firstName
        teach.middle_name = middleName
        teach.type = type 
        teach.department = department
        teach.position = position

        teacher.append(teach)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu()
        
def addRecords1():
    while True:
        print()
        id = input('Enter id: ')
        lastName = input('Enter last name: ')
        firstName = input('Enter first name: ')
        middleName = input('Enter middle name: ')
        type = input('Enter type: ')
        course = input('Enter Course: ')
        year = input('Enter year: ')
        section = input('Enter section: ')
        print('----------------------------')
        filipino = input('Grade filipino: ')
        math = input('Grade math: ')
        science = input('Grade science: ')
        english = input('Grade english: ')

        stud = Grade(filipino, math, science, english)
        stud.id = id
        stud.last_name = lastName
        stud.first_name = firstName
        stud.middle_name = middleName
        stud.type = type
        stud.course = course
        stud.year = year
        stud.section = section

        students.append(stud)

        print()
        ans = input('Enter another? [y/n]: ')

        if (ans != 'y'):
            break

    menu() 

def deleteRecord1():
    i = int(input('Enter index: '))
    students.pop(i)
    menu()

def deleteRecord2():
    i = int(input('Enter index: '))
    teacher.pop(i)
    menu()

def searchRecord1():
    i = int(input('Enter index: '))
    print(f'{i} \t {students[i].getName()} \t | {students[i].getYrCourseSec()} \t | {students[i].getAverage()}')
    
    menu()

def searchRecord2():
    i = int(input('Enter index: '))
    print(f'{i} \t {teacher[i].getName()} \t | {teacher[i].getDepartment()} \t | {teacher[i].getPosition()} \t | {teacher[i].getProfsubject}')

    menu()

def displayRecords1():
    print()
    print('---------------------------------------------------------------------------------------')
    i = 0
    for s in students:

        print(f'{i} \t | {s.getName()} \t | {s.getYrCourseSec()} \t | {s.getAverage()}')
        i += 1
    print('---------------------------------------------------------------------------------------')

def displayRecords2():
    print()
    print('---------------------------------------------------------------------------------------')
    i = 0
    for t in teacher:

        print(f'{i} \t | {t.getName()} \t | {t.getDepartment()} \t | {t.getPosition()} \t | {t.getProfsubject()}')
        i += 1
    print('---------------------------------------------------------------------------------------')


def menu():
    print()
    print()
    print('Are you a teacher or student?')
    print('Type "S" for students and Type "T" for Teacher Type "SKIP" for other function')
    print()
    choice = input('Enter the answer: ')
    if (choice == 'S'):
        kidds()
    elif (choice == 'T'):
        Prof()
    elif (choice =='SKIP'):
        skip()

def skip():
    while True:
        print()
        print('X - display All           Z - delete all')
        print()
        choice = input('Enter a function: ')
        print()
        if (choice == 'X'):
            print('STUDENT LIST')
            displayRecords1()
            print()
            print('TEACHER LIST')
            displayRecords2()
            print()
            menu()
        elif (choice == 'Z'):
            students.clear()
            teacher.clear()
            menu()
def kidds():    
    while True:
        print()
        print('::Menu::')
        print('D - delete student        S - search student')
        print('A - add student           M - display student')
        print()
        choice = input('Enter a function: ')
        if (choice == 'D'):
            deleteRecord1()
        elif (choice == 'A'):
            addRecords1()
        elif(choice == 'S'):
            searchRecord1()
        elif (choice == 'M'):
            displayRecords1()
            menu()

        print()

def Prof():
    while True:
        print()
        print('::Menu::')
        print('G - delete teacher        C - search teacher')
        print('F - add teacher           N - display teacher')
        print()
        choice = input('Enter a function: ')
        if (choice == 'G'):
            deleteRecord2()
        elif (choice == 'F'):
            addRecord2()
        elif(choice == 'C'):
            searchRecord2()
        elif (choice == 'N'):
            displayRecords2()
            menu()

print()
menu()