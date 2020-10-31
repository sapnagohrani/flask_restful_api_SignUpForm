from flask import Flask
from flask_restful import Resource, Api
from reqparser import parser
from service import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.app_context().push()

api = Api(app)


class Registration(Resource):
    def get(self):
        return SignupService.get_all_users()

    def post(self):
        args = parser.parse_args()
        return args


api.add_resource(Registration, '/signup')
if __name__ == '__main__':
    app.run(debug=True)
