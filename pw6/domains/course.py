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