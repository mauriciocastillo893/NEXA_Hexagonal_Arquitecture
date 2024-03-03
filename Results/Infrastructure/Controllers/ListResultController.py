from flask import Blueprint, jsonify
from Results.Application.ListResultUseCase import ListResultUseCase

get_list_result_blueprint = Blueprint('get_list_results', __name__)

def initialize_endpoints(repository):
    listResultsUseCase = ListResultUseCase(repository)

    @get_list_result_blueprint.route('/', methods=['GET'])
    def get_list_results():
        try:
            results = listResultsUseCase.execute()
            results = [result.to_dict() for result in results]
            return jsonify(results), 200
        except Exception as e:
            return jsonify({"message": "Error getting results", "error": str(e)}), 400
