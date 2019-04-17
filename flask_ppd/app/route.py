from flask import Flask
from flask_restful import Api
from flask_cors import CORS

import os

from pyurl.user import User
from pyurl.index import Index
from pyurl.list import List


#app config
class ConfigFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(ROOT_PATH, 'static')

app = ConfigFlask(__name__, static_folder=STATIC_PATH, static_url_path='')
cors = CORS(app, resources={
    r"/user/*" : {"origin" : "*"},
    r"/list/*" : {"origin" : "*"},
})
api = Api(app=app)

#set app url
api.add_resource(Index, "/")
api.add_resource(List, "/list", "/list/<id>")
api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run(debug=True)