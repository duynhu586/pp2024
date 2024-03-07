import math

# List students
def listStudent(studentMana):
    studentMana.listStudents()

# List courses 
def listCourse(studentMana):
    studentMana.listCourses()

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