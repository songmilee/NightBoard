import db
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import model.person as ps

class PPD:
    def __init__(self):
        self.cur = db.connectDB()

    def __del__(self):
        #db connection out
        db.connectOut()
        

    def showList(self):
        #clear the display
        os.system('clear')

        #connect to db
        sql = "select * from member"
        self.cur.execute(sql)

        rows = self.cur.fetchall()

        #show the data list
        for i in rows:
            print(i[6], i[0])

    def addData(self):
        os.system('clear')

        data = ps.Person()

        data.setName(input("Name > "))
        sex = input("Sex(1. Male 2. Female) > ")

        if sex == 1:
            data.setSex("Male")
        else:
            data.setSex("Female")

        data.setAddress(input("Address > "))
        data.setBirth(input("Birth(ex > 1991-01-01) > "))

        sql = "insert into member(mem_name, mem_sex, mem_year, mem_month, mem_day, mem_address, mem_no) values(%s, %s, %s, %s, %s, %s, null)"
        self.cur.execute(sql, (data.getName(), data.getNumSex(), data.getYear(), data.getMonth(), data.getDay(), data.getAddress()))
        db.commit()

        print("Data Inserted")
