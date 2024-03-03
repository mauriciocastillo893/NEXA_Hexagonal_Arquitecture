from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from User.Application.listUsersUseCase import ListUsersUseCase

get_list_users_blueprint = Blueprint('get_list_users', __name__)

def initialize_endpoints(repository):
    listUsersUseCase = ListUsersUseCase(repository)

    @get_list_users_blueprint.route('/', methods=['GET'])
    @jwt_required()
    def get_list_users():
        try:
            users = listUsersUseCase.execute()
            users = [user.to_dict() for user in users]
            return jsonify(users), 200
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500