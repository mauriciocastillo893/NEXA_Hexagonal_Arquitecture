from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from User.Application.DeleteUserUseCase import DeleteUserUseCase

delete_user_blueprint = Blueprint('delete_user', __name__)

def initialize_endpoints(repository):
    deleteUserUseCase = DeleteUserUseCase(repository)

    @delete_user_blueprint.route('/<int:id>', methods=['DELETE'])
    @jwt_required()
    def delete_user(id):
        try:
            deleteUserUseCase.execute(id)
            return jsonify({'message': 'User deleted'}), 200
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500