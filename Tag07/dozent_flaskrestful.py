# in console: pip install flask_restful
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

users = [
    {
    'name': 'Joe',
    'age': 45,
    'occupation': 'Engin'
    },
    {
    'name': 'Jane',
    'age': 34,
    'occupation': 'DEV'
    },
    {
    'name': 'Chris',
    'age': 23,
    'occupation': 'PR'
    }
    ]

class User(Resource):

    def get(self, name):
        if name == 'all':
            return users, 200
        for user in users:
            if name == user['name']:
                return user, 200
        return 'User not found', 404


    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        for user in users:
            if name == user['name']:
                return f"user {name} already exists", 400

        user = {
            'name': name,
            'age': int(args['age']),
            'occupation': args['occupation']
        }
        users.append(user)
        return user, 201


    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        for user in users:
            if name == user['name']:
                user['age'] = int(args['age'])
                user['occupation'] = args['occupation']
                return user, 201

        user = {'name': name, 'age': args['age'],
                'occupation': args['occupation']}
        users.append(user)
        return user, 201


    def delete(self, name):
        for index, user in enumerate(users):
            if user['name'] == name:
                return users.pop(index), 200
        # mögliche Variante:
        # global users
        #
        # users = [user for user in users if user['name'] != name]
        # return f'delted user {name}', 200



############# main Programm

api.add_resource(User, '/user/<string:name>')
app.run(debug = True)
