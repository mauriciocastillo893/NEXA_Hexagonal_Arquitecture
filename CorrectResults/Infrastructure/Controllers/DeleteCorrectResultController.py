from flask import Blueprint, jsonify
from CorrectResults.Application.DeleteCorrectResultsUseCase import DeleteCorrectResultsUseCase

delete_correct_result_blueprint = Blueprint('delete_correct_result', __name__)

def initialize_endpoints(repository):
    deleteCorrectResultsUseCase = DeleteCorrectResultsUseCase(repository)

    @delete_correct_result_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_correct_result(id):
        try:
            deleteCorrectResultsUseCase.execute(id)
            return jsonify({'message': 'Correct Result deleted'}), 200
        except Exception as e:
            return jsonify({"message": "Error deleting Correct Result", "error": str(e)}), 400