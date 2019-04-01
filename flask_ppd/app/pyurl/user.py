from flask_restful import Resource
from flask import render_template

class User(Resource):
    def get(self):
        return "User"