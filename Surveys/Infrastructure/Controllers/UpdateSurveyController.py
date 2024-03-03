from flask import Blueprint, request, jsonify
from Surveys.Application.UpdateSurveyUseCase import UpdateSurveyUseCase

update_survey_blueprint = Blueprint('update_survey', __name__)

def initialize_endpoints(repository):
    updateSurveyUseCase = UpdateSurveyUseCase(repository)

    @update_survey_blueprint.route('/<int:id>', methods=['PUT'])
    def update_survey(id):
        try:
            survey_data = request.get_json()
            survey = updateSurveyUseCase.execute(id, survey_data)
            return jsonify(survey.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error updating survey", "error": str(e)}), 400
        

        