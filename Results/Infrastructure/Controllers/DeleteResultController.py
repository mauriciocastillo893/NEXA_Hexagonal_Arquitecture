from flask import Blueprint, jsonify
from Results.Application.DeleteResultUseCase import DeleteResultUseCase

delete_result_blueprint = Blueprint('delete_result', __name__)

def initialize_endpoints(repository):
    deleteResultUseCase = DeleteResultUseCase(repository)

    @delete_result_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_result(id):
        try:
            deleteResultUseCase.execute(id)
            return jsonify({'message': 'Result deleted'}), 200
        except Exception as e:
            return jsonify({"message": "Error deleting Result", "error": str(e)}), 400