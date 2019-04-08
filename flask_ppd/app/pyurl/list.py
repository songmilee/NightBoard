from flask_restful import Resource
from flask import make_response, render_template

class List(Resource):
    def get(self):
        return make_response(render_template('list.html'), 200)