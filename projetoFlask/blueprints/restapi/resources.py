from flask import jsonify, abort
from flask_restful import Resource
from projetoFlask.ext.database import ListUsers

class UserResource(Resource):
    def get(self):
        users = ListUsers.query.all() or abort(204)
        return jsonify(
            {'users':[ 
                {
                    'id':user.id,
                    'name':user.name,
                }
                for user in users
            ]}
        )

class UserItemResource(Resource):
    def get(self, user_id):
        user = ListUsers.query.filter_by(id=user_id).first() or abort(
            404
        )
        
        return jsonify(user.to_dict())