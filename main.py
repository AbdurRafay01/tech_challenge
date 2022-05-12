from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity
from functools import wraps
# DB
from models import Database
# 
app = Flask(__name__)
api = Api(app)
# 
app.config['SECRET_KEY'] = 'super-secret'
jwt = JWT(app, authenticate, identity)

def checkuser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_identity.username == 'user1':
            return func(*args, **kwargs)
        return abort(401)
    return wrapper



data_patch_args = reqparse.RequestParser()
data_patch_args.add_argument("data", type=dict, help="missing patch data", required=True, action="append")

class CRUD(Resource):

    def __init__(self):
        self.db = Database()

    decorators = [checkuser, jwt_required()]
    def get(self, id):
        result = self.db.get_data_by_id(id)
        return {'result': result}
    
    def patch(self, id):
        data = request.get_json()
        self.db.update_data_by_id(id, data)
        return '', 204
    
    def delete(self, id):
        status = self.db.delete_data_by_id(id)
        return '', 204

add_data_puts_args = reqparse.RequestParser()
add_data_puts_args.add_argument("data_list", type=list,  help="missing data", required=True, action='append')

class InsertQuery(Resource):

    def __init__(self):
        self.db = Database()
        
    def put(self):
        datalist = request.get_json()
        self.db.insert_data(datalist)
        return '', 204

api.add_resource(CRUD, "/covid_data/<int:id>")
api.add_resource(InsertQuery, "/covid_data_update")


if __name__ == "__main__":
    app.run(debug=True)
