from Surveys.Application.GetAskUseCase import GetAskUseCase
from flask import Blueprint, jsonify

get_ask_blueprint = Blueprint('get_ask', __name__)

def initialize_endpoints(repository):
    getAskUseCase = GetAskUseCase(repository)

    @get_ask_blueprint.route('/<int:id>', methods=['GET'])
    def get_ask(id):
        try:
            ask = getAskUseCase.execute(id)
            return jsonify(ask.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting ask", "error": str(e)}), 400