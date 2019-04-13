from flask_restful import Resource
from flask import make_response, render_template

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import module.database as data

class List(Resource):
    def get(self):
        db = data.Database()
        
        sql = "select * from member"
        rows = db.executeAll(sql)
        return make_response(render_template('list.html', users=rows), 200)

    def delete(self, id):
        db = data.Database()

        sql = "delete from member where mem_no=%s" % (id)

        rows = db.execute(sql)

        if rows != 0:
            db.commit()
            return { "result" : "1"} #Success
        
        return { "result" : "0"} #Failed