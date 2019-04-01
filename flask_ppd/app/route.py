from flask import Flask, render_template
from flask_restful import Api

from pyurl.user import User

app = Flask(__name__)
api = Api(app=app)

@app.route("/")
def index():
    return render_template("index.html")

api.add_resource(User, "/user")

if __name__ == "__main__":
    app.run(debug=True)