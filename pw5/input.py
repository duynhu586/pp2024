from domains import student
from domains import course
import output
import math


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
    f = open("student.txt","w")
    for i in range(0,int(studentMana.getStdNumber()),1):
        n = str(i + 1)
        print("Student " + n)
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth (YYYY-MM-DD): ")
        s = student.student(id,name,dob)
        studentMana.addStudent(s)
        f.writelines("Student " + n + ": " + "id: " + str(id) + " name: " + str(name) + "dob: " + str(dob) + "\n")
    f.close()

# Input course information: id,name
def setCourseInfo(studentMana):
    f = open("course.txt","w")
    for i in range(0,int(studentMana.getCoursesNumber()),1):
        n = str(i + 1)
        print("course " + n)
        id = input("Enter courses ID: ")
        name = input("Enter courses name: ")
        weight = input("Enter the weight: ")
        s = course.course(id,name,weight)
        studentMana.addCourse(s)
        f.writelines("course: " + n + " id: " + str(id) + " name: " + str(name) + " weight: " +  str(weight)+"\n")
    f.close()

# Select a course, input marks for student in this course
def markStd(studentMana):
    print("------------------------")
    output.listCourse(studentMana)
    print("choose courses ID to mark...")
    x = int(input())
    f = open("marks.txt","w")
    for course in studentMana.getCourses():
        if int(course.getId()) == x:
            f.writelines("Course " + str(course.getName())+ "\n")
    for i in range(0,int(studentMana.getStdNumber()),1):
        n = i + 1
        Mark = math.floor(float(input("Enter mark of student " + str(n)+ " ")))
        studentMana.setMark(i,x,Mark)
        name = studentMana.getNameStd(i)
        f.writelines("name: " + str(name) + " Mark: " + str(Mark) + "\n")
    f.close()    