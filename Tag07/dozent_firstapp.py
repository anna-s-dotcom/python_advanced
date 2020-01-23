from flask import Flask, jsonify
from flask_restful import Api
app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({'about': 'Hello World!'})

@app.route('/hello')
def hello2():
    return '<p>Hello</p><p>Hello2</p>'

if __name__ == '__main__':
    app.run(debug = True)
