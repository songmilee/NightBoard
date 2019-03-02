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

    def setSex(self, sex):
        self.sex = sex

    def getSex(self):
        return self.sex

    def getAge(self):
        now = datetime.now()
        age = (now.year() - self.year) + 1
        return age

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address
