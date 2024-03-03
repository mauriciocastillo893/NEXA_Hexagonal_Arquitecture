from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from User.Application.GetUserUseCase import GetUserUseCase

get_user_blueprint = Blueprint('get_user', __name__)

def initialize_endpoints(repository):
    getUserUseCase = GetUserUseCase(repository)

    @get_user_blueprint.route('/<int:id>', methods=['GET'])
    @jwt_required()
    def get_user(id):
        try:
            user = getUserUseCase.execute(id)
            return jsonify(user.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500