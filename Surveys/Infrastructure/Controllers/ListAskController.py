from flask import Blueprint, request, jsonify
from Surveys.Application.ListAskUseCase import ListAskUseCase


get_list_ask_blueprint = Blueprint('get_list_ask', __name__)

def initialize_endpoints(repository):
    listAsksUseCase = ListAskUseCase(repository)

    @get_list_ask_blueprint.route('/', methods=['GET'])
    def get_list_asks():
        try:
            asks = listAsksUseCase.execute()
            asks = [ask.to_dict() for ask in asks]
            return jsonify(asks), 200
        except Exception as e:
            return jsonify({"message": "Error getting asks", "error": str(e)}), 400