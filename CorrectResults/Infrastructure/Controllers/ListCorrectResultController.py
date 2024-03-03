from flask import Blueprint, request, jsonify
from CorrectResults.Application.ListCorrectResultUseCase import ListCorrectResultUseCase

get_list_correct_result_blueprint = Blueprint('get_correct_list_results', __name__)

def initialize_endpoints(repository):
    listCorrectResultsUseCase = ListCorrectResultUseCase(repository)

    @get_list_correct_result_blueprint.route('/', methods=['GET'])
    def get_list_correct_results():
        try:
            corrects = listCorrectResultsUseCase.execute()
            corrects = [correct.to_dict() for correct in corrects]
            return jsonify(corrects), 200
        except Exception as e:
            return jsonify({"message": "Error getting corrects results", "error": str(e)}), 400