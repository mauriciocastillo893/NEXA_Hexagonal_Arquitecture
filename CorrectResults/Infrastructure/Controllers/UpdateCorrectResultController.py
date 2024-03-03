from flask import Blueprint, request, jsonify
from CorrectResults.Application.UpdateCorrectResultUseCase import UpdateCorrectResultUseCase

update_correct_result_blueprint = Blueprint('update_correct_result', __name__)

def initialize_endpoints(repository):
    updateCorrectResultUseCase = UpdateCorrectResultUseCase(repository)

    @update_correct_result_blueprint.route('/<int:id>', methods=['PUT'])
    def update_correct_result(id):
        try:
            correct_result_data = request.get_json()
            correct_result = updateCorrectResultUseCase.execute(id, correct_result_data)
            return jsonify(correct_result.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error updating correct result", "error": str(e)}), 400