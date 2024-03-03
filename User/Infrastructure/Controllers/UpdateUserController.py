from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from User.Application.UpdateUserUseCase import UpdateUserUseCase

update_user_blueprint = Blueprint('update_user', __name__)

def initialize_endpoints(repository):
    updateUserUseCase = UpdateUserUseCase(repository)

    @update_user_blueprint.route('/<int:id>', methods=['PUT'])
    @jwt_required()
    def update_user(id):
        try:
            user_data = request.get_json()
            user = updateUserUseCase.execute(id, user_data)
            return jsonify(user.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500