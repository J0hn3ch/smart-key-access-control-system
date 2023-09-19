#!/usr/bin/env python
import os

from flask import Flask
from flask import Blueprint
from flask_restful import Api
from flasgger import Swagger
from pymongo import MongoClient
from api.routes.home import home_api
from api.routes.member import member_api

app = Flask(__name__)
#api = Api(app)

app.config['SWAGGER'] = {
    'title': 'Flask API Starter Kit',
}

swagger = Swagger(app)
#app.config.from_pyfile('config.py')
app.register_blueprint(home_api)
app.register_blueprint(member_api)


client = MongoClient("mongo:27017")
'''
@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB UniVersoMe client!\n"
'''

'''
===== [ ACCESS CONTROL ] =====

'''
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9091), debug=True)
