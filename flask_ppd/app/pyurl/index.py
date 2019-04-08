from flask_restful import Resource
from flask import render_template, make_response

class Index(Resource):
    #Return Main Index Page
    def get(self):
        return make_response(render_template('index.html'), 200)