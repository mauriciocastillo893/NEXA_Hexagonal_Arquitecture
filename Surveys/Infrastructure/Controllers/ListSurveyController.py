from flask import Blueprint, request, jsonify
from Surveys.Application.ListSurveyUseCase import ListSurveyUseCase


get_list_survey_blueprint = Blueprint('get_list_survey', __name__)

def initialize_endpoints(repository):
    listSurveysUseCase = ListSurveyUseCase(repository)

    @get_list_survey_blueprint.route('/', methods=['GET'])
    def get_list_surveys():
        try:
            surveys = listSurveysUseCase.execute()
            surveys = [survey.to_dict() for survey in surveys]
            return jsonify(surveys), 200
        except Exception as e:
            return jsonify({"message": "Error getting surveys", "error": str(e)}), 400