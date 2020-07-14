from flask_restful import Api
from flask import Flask

import datetime

import resource


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hi_sempai!'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)
api = Api(app)
api.add_resource(resource.MyResource, '/post')


@app.route('/')
def index():
    return {'test_passed': True}


if __name__ == '__main__':
    app.run(host='localhost')
