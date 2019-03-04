import db
import os
def showList():
    #clear the display
    os.system('clear')

    #connect to db
    cur = db.connectDB()
    sql = "select * from member"
    cur.execute(sql)

    rows = cur.fetchall()
    for i in rows:
        print(i[6], i[0])

    #db connection out
    db.connectOut()