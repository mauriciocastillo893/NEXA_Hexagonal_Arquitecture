from flask import Blueprint, request, jsonify
from Results.Application.UpdateResultUseCase import UpdateResultUseCase

update_result_blueprint = Blueprint('update_result', __name__)

def initialize_endpoints(repository):
    updateResultUseCase = UpdateResultUseCase(repository)

    @update_result_blueprint.route('/<int:id>', methods=['PUT'])
    def update_result(id):
        try:
            result_data = request.get_json()
            result = updateResultUseCase.execute(id, result_data)
            return jsonify(result.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error updating result", "error": str(e)}), 400