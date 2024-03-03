from Surveys.Application.GetSurveyUseCase import GetSurveyUseCase
from flask import Blueprint, request, jsonify

get_survey_blueprint = Blueprint('get_survey', __name__)

def initialize_endpoints(repository):
    getSurveyUseCase = GetSurveyUseCase(repository)

    @get_survey_blueprint.route('/<int:id>', methods=['GET'])
    def get_survey(id):
        try:
            survey = getSurveyUseCase.execute(id)
            return jsonify(survey.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting survey", "error": str(e)}), 400