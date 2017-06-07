#!flask/bin/python

"""task manager for time"""

from flask import Flask
from flask.ext.restful import Api
from flask.ext.httpauth import HTTPBasicAuth
from resources import TaskListAPI
from resources import TaskAPI

app = Flask(__name__, static_url_path="")
api = Api(app)
   
api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)