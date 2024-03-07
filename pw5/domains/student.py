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