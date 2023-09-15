from flask_restful import reqparse, abort, Resource

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '?????'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Member(Resource):
    def get(self, member_id):
        abort_if_todo_doesnt_exist(member_id)
        return TODOS[member_id]

    def delete(self, member_id):
        abort_if_todo_doesnt_exist(member_id)
        del TODOS[member_id]
        return '', 204

    def put(self, member_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[member_id] = task
        return task, 201


# TodoList
# shows a list of all todos, and lets you POST to add new tasks
class MemberList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        member_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        member_id = 'todo%i' % member_id
        TODOS[member_id] = {'task': args['task']}
        return TODOS[member_id], 201

##
## Actually setup the Api resource routing here
##
api.add_resource(MemberList, '/members')
api.add_resource(Member, '/members/<member_id>')