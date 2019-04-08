from flask import Flask, render_template
from flask_restful import Api

from pyurl.user import User
from pyurl.index import Index
from pyurl.list import List

app = Flask(__name__)
api = Api(app=app)

#set app url
api.add_resource(Index, "/")
api.add_resource(List, "/list")
api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run(debug=True)