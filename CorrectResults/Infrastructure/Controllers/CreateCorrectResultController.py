from flask import Blueprint, request, jsonify
from CorrectResults.Domain.Entities.ACorrectResults import ACorrectResults
from CorrectResults.Application.CreateCorrectResultsUseCase import CreateCorrectResultsUseCase

create_correct_result_blueprint = Blueprint('create_correct_result', __name__)

def initialize_endpoints(repository):
    create_correct_result_use_case = CreateCorrectResultsUseCase(repository)

    @create_correct_result_blueprint.route('/', methods=['POST'])
    def create_correct_result():
        try:
            correct_data = request.get_json()
            success, result = create_correct_result_use_case.execute(ACorrectResults(**correct_data))
            
            if success:
                return jsonify({"message": "Correct Result created", "result": result}), 200
            else:
                return jsonify({"message": "Error creating correct result", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error creating correct result", "error": str(e)}), 400