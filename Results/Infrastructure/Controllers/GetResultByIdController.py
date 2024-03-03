from flask import Blueprint, request, jsonify
from Results.Application.GetResultUseCase import GetResultUseCase

get_Result_blueprint = Blueprint('get_result', __name__)

def initialize_endpoints(repository):
    getResultUseCase = GetResultUseCase(repository)

    @get_Result_blueprint.route('/<int:id>', methods=['GET'])
    def get_result(id):
        try:
            result = getResultUseCase.execute(id)
            return jsonify(result.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting result", "error": str(e)}), 400