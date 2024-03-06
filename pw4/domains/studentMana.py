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