from flask_restful import reqparse

parser = reqparse.RequestParser()

parser.add_argument('name', type=str, required=True, help='Important Parameter')
parser.add_argument('email', type=str, required=True, help='Important Parameter')
parser.add_argument('password', type=str, required=True, help='Important Parameter')
