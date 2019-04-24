from flask_restful import Resource, reqparse
from flask import render_template, make_response
import json
import module.database as data

class User(Resource):
    def get(self):
        return make_response(render_template("user.html"))
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('mem_name', required=True)
            parser.add_argument('mem_address', required=True)
            parser.add_argument('mem_sex', required=True)
            parser.add_argument('mem_birth', required=True)
            
            args = parser.parse_args()
            
            mem_name = args['mem_name']
            mem_address = args['mem_address']
            mem_sex = args['mem_sex']
            mem_birth = args['mem_birth']

            birth = mem_birth.split('-')

            db = data.Database()
            sql = "insert into member(mem_name, mem_sex, mem_year, mem_month, mem_day, mem_address, mem_no) values(%s, %s, %s, %s, %s, %s, null)"
            
            db.execute(sql, (mem_name, mem_sex, birth[0], birth[1], birth[2], mem_address))
            db.commit()
            
            return { "result" : "1"}
        except Exception as e:
            return {'result' : "-1", "error" : str(e) }    