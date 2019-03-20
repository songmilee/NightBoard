import pymysql

#create connection object
conn = None
def connectDB():
    global conn
    #create connection
    conn = pymysql.connect(host='den1.mysql5.gear.host', user='wilog', password='noti01!', db='wilog', charset='utf8')
    curs = conn.cursor()

    #return connection to other files
    return curs

def commit():
    conn.commit()

#connection out
def connectOut():
    global conn
    conn.close()
