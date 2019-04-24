from flask_restful import Resource, reqparse
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

    def delete(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('mem_id', required=True)

            args = parser.parse_args()
            
            print(args)
            id = args['mem_id']

            db = data.Database()

            sql = "delete from member where mem_no=%s" % (id)

            rows = db.execute(sql)

            if rows != 0:
                db.commit()
                return { "result" : "1"} #Success
        except Exception as e:
            return { "result" : "0", "error" : str(e)} #Failed