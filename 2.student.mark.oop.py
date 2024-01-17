Number_Std = 0
Number_courses = 0

class student:
    def __init__(self,__id,__name,__Dob):
        self.__id = __id
        self.__name = __name
        self.__Dob = __Dob
        self.__mark = {}
    
    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getDob(self):
        return self.__Dob
    
    def setId(self,__id):
        self.__id = __id

    def setName(self,__name):
        self.__name = __name
    
    def setDob(self, Dob):
        self.__Dob = Dob

    def setMark(self,courseId,mark):
        self.__mark[courseId] = mark

    def getMark(self,courseId):
        return self.__mark[courseId]

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"
    
class course:
    def __init__(self,__id,__name):
        self.__id = __id
        self.__name = __name
        self.students = []

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def setId(self,__id):
        self.__id = __id

    def setname(self,__name):
        self.__name = __name
    
    def addStudent(self,student):
        self.students.append(student)

    def getStudent(self):
        return self.students
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
    
class studentMana:
    def __init__(self):
        self.__students = []
        self.__courses = []


    def addStudent(self, student):
        self.__students.append(student)

    def addCourse(self, course):
        self.__courses.append(course)

    def listCourses(self):
        print("List of courses:")
        for i in range(0,Number_Std,1):
            name = self.__courses[i].getName()
            Id = self.__courses[i].getId()
            print("name: " + name + " id: " + Id)
    
    def listStudents(self):
        print("List of students:")
        for i in range(0,Number_Std,1):
            name = self.__students[i].getName()
            Id = self.__students[i].getId()
            Dob = self.__students[i].getDob()
            print("name: " + name + " id: " + Id + " dob: " + Dob)

    def setMark(self,i,x,Mark):
        self.__students[i].setMark(x,Mark)

    def showMark(self, courseId):
        print(f"Student marks for course {courseId}:")
        for student in self.__students:
            mark = student.getMark(courseId)
            name = student.getName()
            if mark is not None:
                print(f"{name}: {mark}")

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
def setStdInfo(studentMana):
    for i in range(0,Number_Std,1):
        n = str(i + 1)
        print("Student " + n)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        s = student(id,name,dob)
        studentMana.addStudent(s)

# Input course information: id,name
def setCourseInfo(studentMana):
    for i in range(0,Number_courses,1):
        n = str(i + 1)
        print("course " + n)
        id = input("Enter courses ID: ")
        name = input("Enter courses name: ")
        s = course(id,name)
        studentMana.addCourse(s)

# List students
def listStudent(studentMana):
    studentMana.listStudents()

# List courses 
def listCourse(studentMana):
    studentMana.listCourses()

# Select a course, input marks for student in this course
def markStd(studentMana):
    print("------------------------")
    listCourse(studentMana)
    print("choose courses ID to mark...")
    x = int(input())
    
    for i in range(0,Number_Std,1):
        n = i + 1
        Mark = input("Enter mark of student " + str(n)+ " ")
        studentMana.setMark(i,x,Mark)

# Show student marks for a given course
def showMark(studentMana):
    print("------------------------")
    listCourse(studentMana)
    print("Choose courses ID to see mark...")
    x = int(input())
    studentMana.showMark(x)

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

class1 = studentMana()

i = ''
while True:
    try:
            i = int(input('Enter your choice: '))
    except:
            print('Wrong input. Please enter a number ...')
    if i == 1:
        Number_Std = setNumberOfStudent()
    elif i == 2:
        setStdInfo(class1)
    elif i == 3:
        Number_courses = setNumberOfCourses()
    elif i == 4:
        setCourseInfo(class1)
    elif i == 5:
        markStd(class1)
    elif i == 6:
        listCourse(class1)
    elif i == 7:
        listStudent(class1)
    elif i == 8:
        showMark(class1)
    elif i == 9:
        exit()
#     else: print('Invalid choice. Please enter a number between 1 and 9.')

# class1 = studentMana()
# Number_Std = setNumberOfStudent()
# setStdInfo(class1)
# listStudent(class1)
# Number_courses = setNumberOfCourses()
# print(Number_courses)
# setCourseInfo(class1)
# listCourse(class1)
# markStd(class1)
# showMark(class1)
