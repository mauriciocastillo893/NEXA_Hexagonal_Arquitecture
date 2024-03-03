from flask import Blueprint, request, jsonify
from CorrectResults.Application.GetCorrectResultsUseCase import GetCorrectResultsUseCase

get_Correct_Result_blueprint = Blueprint('get_correct_result', __name__)

def initialize_endpoints(repository):
    getCorrectResultUseCase = GetCorrectResultsUseCase(repository)

    @get_Correct_Result_blueprint.route('/<int:id>', methods=['GET'])
    def get_correct_result(id):
        try:
            correct = getCorrectResultUseCase.execute(id)
            return jsonify(correct.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting correct result", "error": str(e)}), 400