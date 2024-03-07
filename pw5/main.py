import input
import output
from domains import studentMana
import tarfile
from tqdm import tqdm

def compress_to_dat(tar_file, members):
    tar = tarfile.open(tar_file, mode="w:gz")
    for member in members:
        tar.add(member)
    tar.close()


def decompress(tar_file, destination_folder):
    with tarfile.open(tar_file, 'r:gz') as tar:
        tar.extractall(destination_folder)

print("""
1. Input number of students in a class
2. Input student information: id,name,DoB
3. Input number of courses
4. Input course information: id,name
5. Select a course, input marks for student in this course
6.  List courses 
7.  List students
8. Show student marks for a given course
9. calculate GPA of a student
10. sort students by GPA descending
11. exit
""")

# class1 = studentMana.studentMana()
# i = ''
# while True:
#     try:
#             i = int(input('Enter your choice: '))
#     except:
#             print('Wrong input. Please enter a number ...')
#     if i == 1:
#         Number_Std = input.setNumberOfStudent(class1)
#     elif i == 2:
#         input.setStdInfo(class1)
#     elif i == 3:
#         Number_courses = input.setNumberOfCourses(class1)
#     elif i == 4:
#         input.setCourseInfo(class1)
#     elif i == 5:
#         input.markStd(class1)
#     elif i == 6:
#         output.listCourse(class1)
#     elif i == 7:
#         output.listStudent(class1)
#     elif i == 8:
#         output.showMark(class1)
#     elif i == 9:
#         output.calculateGPA(class1)
#     elif i == 10:
#         output.sortStudentGPA(class1)
#     elif i == 11:
#         exit()
#     else: print('Invalid choice. Please enter a number between 1 and 11.')

class1 = studentMana.studentMana()
Number_Std = input.setNumberOfStudent(class1)
input.setStdInfo(class1)
output.listStudent(class1)
input.setNumberOfCourses(class1)
input.setCourseInfo(class1)
output.listCourse(class1)
input.markStd(class1)
output.showMark(class1)
output.calculateGPA(class1)
output.sortStudentGPA(class1)

fileCompress = ["student.txt","course.txt","marks.txt"]
compress_to_dat("students.dat", fileCompress)

decompress('students.dat', './my_extracted_folder')