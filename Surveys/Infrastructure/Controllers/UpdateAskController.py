from flask import Blueprint, request, jsonify
from Surveys.Application.UpdateAskUseCase import UpdateAskUseCase

update_ask_blueprint = Blueprint('update_ask', __name__)

def initialize_endpoints(repository):
    updateAskUseCase = UpdateAskUseCase(repository)

    @update_ask_blueprint.route('/<int:id>', methods=['PUT'])
    def update_ask(id):
        try:
            ask_data = request.get_json()
            ask = updateAskUseCase.execute(id, ask_data)
            return jsonify(ask.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error updating ask", "error": str(e)}), 400