students = []
courses = []
Number_Std = 0
Number_courses = 0

#Input number of students in a class
def  setNumberOfStudent():   
    x = input("enter number of students: ")
    print("number of students in class " + x)
    x = int(x)
    return x

# Input number of courses
def  setNumberOfCourses():   
    x = input("enter number of Courses: ")
    print("number of courses in class " + x)
    x = int(x)
    return x

#Input student information: id,name,DoB
def setStdInfo():
    for i in range(0,Number_Std,1):
        n = str(i + 1)
        print("Student " + n)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        s = {"id":id, "name":name, "dob":dob}
        students.append(s)

# Input course information: id,name
def setCourseInfo():
    for i in range(0,Number_courses,1):
        n = str(i + 1)
        print("course " + n)
        id = input("Enter courses ID: ")
        name = input("Enter courses name: ")
        s = {"id":id, "name":name}
        courses.append(s)

# List students
def listStudent():
    for i in range(0,Number_Std,1):
        n = i + 1
        print("Student "+str(n))
        print(students[i])

# List courses 
def listCourse():
    for i in range(0,Number_courses,1):
        n = i + 1
        print(str(n) + ".")
        print(courses[i])

# Select a course, input marks for student in this course
def markStd():
    print("------------------------")
    print("choose courses to mark...")
    listCourse()
    x = int(input())
    NameCourses = courses[x-1]["name"]
    for i in range(0,Number_Std,1):
        n = i + 1
        Mark = input("Enter mark of student " + str(n)+ " ")
        students[i][NameCourses] = Mark

# Show student marks for a given course
def showMark():
    print("------------------------")
    print("Choose courses to see mark...")
    listCourse()
    x = int(input())
    NameCourses = courses[x-1]["name"]
    for i in range(0,Number_Std,1):
        name = students[i]["name"]
        point = students[i][NameCourses]
        print(name+" "+point)

print("""
1. Input number of students in a class
2. Input student information: id,name,DoB
3. Input number of courses
4. Input course information: id,name
5. Select a course, input marks for student in this course
6.  List courses 
7.  List students
8. Show student marks for a given course
9. exit
""")

i = ''
while True:
    try:
            i = int(input('Enter your choice: '))
    except:
            print('Wrong input. Please enter a number ...')
    if i == 1:
        Number_Std = setNumberOfStudent()
    elif i == 2:
        setStdInfo()
    elif i == 3:
        Number_courses = setNumberOfCourses()
    elif i == 4:
        setCourseInfo()
    elif i == 5:
        markStd()
    elif i == 6:
        listCourse()
    elif i == 7:
        listStudent()
    elif i == 8:
        showMark()
    elif i == 9:
        exit()
    else: print('Invalid choice. Please enter a number between 1 and 9.')


# Number_Std = setNumberOfStudent()
# setStdInfo()
# Number_courses = setNumberOfCourses()
# print(Number_courses)
# setCourseInfo()
# listCourse()
# markStd()
# showMark()