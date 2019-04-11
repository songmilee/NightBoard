import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='den1.mysql5.gear.host', 
                                    user='wilog', 
                                    password='noti01!', 
                                    db='wilog', 
                                    charset='utf8')
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
    
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row

    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row

    def commit():
        self.db.commit()