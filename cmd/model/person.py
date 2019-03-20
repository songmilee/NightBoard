from datetime import datetime

class Person:
    def __init__(self):
        self.name = ""
        self.year = 1900
        self.month = 1
        self.day = 1
        self.address = ""
        self.sex = "male"

    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = name

    def setYear(self, year):
        self.year = year

    def setMonth(self, month):
        self.month = month

    def setDay(self, day):
        self.day = day
    
    def setBirth(self, birth):
        temp = birth.split("-")

        self.setYear(int(temp[0]))
        self.setMonth(int(temp[1]))
        self.setDay(int(temp[2]))

    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex

    def getNumSex(self):
        if(self.sex.lower() == "male"):
            return 0
        else :
            return 1

    def getAge(self):
        now = datetime.now()
        age = (now.year() - self.year) + 1
        return age

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def getYear(self):
        return int(self.year)

    def getMonth(self):
        return int(self.month)

    def getDay(self):
        return int(self.day)
