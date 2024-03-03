from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from User.Application.AwardOutcomeUseCase import AwardOutcomeUseCase

award_outcome_blueprint = Blueprint('award_outcome', __name__)

def initialize_endpoints():
    @award_outcome_blueprint.route('/', methods=['POST'])
    @jwt_required()
    def award_outcome():
        user_uuid = request.json.get('user_uuid')
        survey_uuid = request.json.get('survey_uuid')
        outcome = AwardOutcomeUseCase().execute(user_uuid, survey_uuid)
        return jsonify(outcome=outcome)