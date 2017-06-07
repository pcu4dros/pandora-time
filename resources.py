import datetime

from models import Task
from db import session

from flask.ext.restful import reqparse
from flask.ext.restful import abort
from flask.ext.restful import Resource
from flask.ext.restful import fields
from flask.ext.restful import marshal_with
from flask.ext.httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

task_fields = {
        'title': fields.String,
        'description': fields.String,
        'date': fields.DateTime(dt_format='rfc822'),
        'expires': fields.DateTime(dt_format='rfc822'),
        'done': fields.Boolean,
        'uri': fields.Url('task')
}

parser = reqparse.RequestParser()
parser.add_argument('id', type=int, location='json')
parser.add_argument('title', type=str, location='json')
parser.add_argument('description', type=str, location='json')
parser.add_argument('date', type=datetime, location='json')
parser.add_argument('expires', type=datetime, location='json')
parser.add_argument('done', type=bool, location='json')

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None
    
@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return make_response(jsonify({'message': 'Unauthorized access'}), 403)

class TaskAPI(Resource):
    decorators = [auth.login_required]

    @marshal_with(task_fields)
    def get(self, id):
        task = session.query(Task).filter(Task.id == id).first()
        if not task:
            abort(404, message="Todo {} doesn't exist".format(id))
        return task

    @marshal_with(task_fields)
    def put(self, id):
        parsed_args = parser.parse_args()
        task = session.query(Task).filter(Task.id == id).first()
        task.title = parsed_args['title']
        task.description = parsed_args['description']
        task.date = parsed_args['date']
        task.expires = parsed_args['expires']
        task.done = parsed_args['done']
        session.add(task)
        session.commit()
        return task, 201

    def delete(self, id):
        task = session.query(Task).filter(Task.id == id).first()
        if not todo:
            abort(404, message="Task {} doesn't exist".format(id))
        session.delete(task)
        session.commit()
        return {}, 204
        
class TaskListAPI(Resource):
    decorators = [auth.login_required]

    @marshal_with(task_fields)
    def get(self):
        tasks = session.query(Task).all()
        return tasks

    @marshal_with(task_fields)
    def post(self):
        parsed_args = parser.parse_args()
        task = Task(
        title = parsed_args['title'],
        description = parsed_args['description'],
        date = parsed_args['date'],
        expires = parsed_args['expires'],
        done = parsed_args['done'])
        session.add(task)
        session.commit()
        return todo, 201