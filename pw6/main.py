import input
import output
from domains import studentMana
import pickle

with open("student.pickle",'rb') as f:
    class1 : studentMana= pickle.load(f)

output.listCourse(class1)
output.listStudent(class1)