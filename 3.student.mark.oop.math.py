import math
import numpy as np

class student:
    def __init__(self,__id,__name,__Dob):
        self.__id = __id
        self.__name = __name
        self.__Dob = __Dob
        self.__NumberOfCourses = 0
        self.__courses = []
    
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

    def setNumCourses(self,num):
        self.__NumberOfCourses = num

    def getNumCourses(self):
        return int(self.__NumberOfCourses)

    def setMark(self,courseId,mark):
        for course in self.__courses:
            if int(course.getId()) == courseId:
                # Found the matching course
                course.setMark(mark)
                print(f"Mark set for course {courseId}")
                break
            else:
                print(f"Course {courseId} not found.")

    def getMark(self,courseId):
        for course in self.__courses:
            if int(course.getId()) == courseId:
                return course.getMark()

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DOB: {self.dob}"
    
    def addCourse(self,course):
        self.__courses.append(course)
    
    def showGPA(self):
        markList =[]
        weightList = []
        for course in self.__courses:
            markList.append(float(course.getMark()))
            weightList.append(float(course.getWeight()))
        
        weightSum = np.dot(markList,weightList)
        totalCredits = np.sum(weightList)

        return weightSum/totalCredits

class course:
    def __init__(self,id,name,weights):
        self.__id = id
        self.__name = name
        self.__mark = 0
        self.__weights = weights

    def getId(self):
        return self.__id
    
    def getName(self):
        return self.__name
    
    def getMark(self):
        return self.__mark
    
    def getWeight(self):
        return self.__weights
    
    def setId(self,id):
        self.__id = id

    def setname(self,name):
        self.__name = name

    def setMark(self,mark):
        self.__mark = mark
    
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"
    
class studentMana:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__NumberStd = 0
        self.__NumberCourses = 0  

    def setNumberStd(self, numberStd):
        self.__NumberStd = numberStd

    def setNumberCourses(self,numberCourses):
        self.__NumberCourses = numberCourses
        for i in range(len(self.__students)):
            self.__students[i].setNumCourses(numberCourses)

    def getStdNumber(self):
        return self.__NumberStd
    
    def getCoursesNumber(self):
        return self.__NumberCourses

    def addStudent(self, student):
        self.__students.append(student)

    def addCourse(self, course):
        self.__courses.append(course)
        for i in range(len(self.__students)):
            self.__students[i].addCourse(course)

    def listCourses(self):
        print("List of courses:")
        for i in range(0,int(self.getCoursesNumber()),1):
            name = self.__courses[i].getName()
            Id = self.__courses[i].getId()
            weight = self.__courses[i].getWeight()
            print("name: " + name + " id: " + Id + " weight: " + weight)
    
    def listStudents(self):
        print("List of students:")
        for i in range(0,int(self.getStdNumber()),1):
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
            print(f"{name}: {mark}")

    def showGPA(self, stdId):
        for student in self.__students:
            if int(student.getId()) == stdId:
                student.showGPA()

    def sortGPA(self):
        for i in range(len(self.__students)-1):
            for j in range(len(self.__students)-i-1):
                if self.__students[j].showGPA() < self.__students[j+1].showGPA():
                    temp = self.__students[j]
                    self.__students[j] = self.__students[j+1]
                    self.__students[j+1] = temp


#Input number of students in a class
def  setNumberOfStudent(studentMana):   
    x = input("enter number of students: ")
    print("number of students in class " + x)
    studentMana.setNumberStd(x)

# Input number of courses
def  setNumberOfCourses(studentMana):   
    x = input("enter number of Courses: ")
    print("number of courses in class " + x)
    studentMana.setNumberCourses(x)

#Input student information: id,name,DoB
def setStdInfo(studentMana):
    for i in range(0,int(studentMana.getStdNumber()),1):
        n = str(i + 1)
        print("Student " + n)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        s = student(id,name,dob)
        studentMana.addStudent(s)

# Input course information: id,name
def setCourseInfo(studentMana):
    for i in range(0,int(studentMana.getCoursesNumber()),1):
        n = str(i + 1)
        print("course " + n)
        id = input("Enter courses ID: ")
        name = input("Enter courses name: ")
        weight = input("Enter the weight: ")
        s = course(id,name,weight)
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
    
    for i in range(0,int(studentMana.getStdNumber()),1):
        n = i + 1
        Mark = math.floor(float(input("Enter mark of student " + str(n)+ " ")))
        studentMana.setMark(i,x,Mark)

# Show student marks for a given course
def showMark(studentMana):
    print("------------------------")
    listCourse(studentMana)
    print("Choose courses ID to see mark...")
    x = int(input())
    studentMana.showMark(x)

# calculate GPA
def calculateGPA(studentMana):
    x = int(input("choose student id to see GPA:"))
    studentMana.showGPA(x)

# sort students by GPA
def sortStudentGPA(studentMana):
    studentMana.sortGPA()

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

# i = ''
# while True:
#     try:
#             i = int(input('Enter your choice: '))
#     except:
#             print('Wrong input. Please enter a number ...')
#     if i == 1:
#         Number_Std = setNumberOfStudent(class1)
#     elif i == 2:
#         setStdInfo(class1)
#     elif i == 3:
#         Number_courses = setNumberOfCourses(class1)
#     elif i == 4:
#         setCourseInfo(class1)
#     elif i == 5:
#         markStd(class1)
#     elif i == 6:
#         listCourse(class1)
#     elif i == 7:
#         listStudent(class1)
#     elif i == 8:
#         showMark(class1)
#     elif i == 9:
#         exit()
#     else: print('Invalid choice. Please enter a number between 1 and 9.')

class1 = studentMana()
Number_Std = setNumberOfStudent(class1)
setStdInfo(class1)
listStudent(class1)
setNumberOfCourses(class1)
setCourseInfo(class1)
listCourse(class1)
markStd(class1)
showMark(class1)
calculateGPA(class1)
sortStudentGPA(class1)