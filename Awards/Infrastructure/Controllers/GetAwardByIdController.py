from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from Awards.Application.GetAwardUseCase import GetAwardUseCase

get_Award_blueprint = Blueprint('get_award', __name__)

def initialize_endpoints(repository):
    getAwardUseCase = GetAwardUseCase(repository)

    @get_Award_blueprint.route('/<int:id>', methods=['GET'])
    @jwt_required()
    def get_award(id):
        claims = get_jwt_identity()
        if claims['type'] != 'CREATOR':
            return jsonify({"message": "Unauthorized"}), 401
        try:
            award = getAwardUseCase.execute(id)
            return jsonify(award.to_dict()), 200
        except Exception as e:
            return jsonify({"message": "Error getting award", "error": str(e)}), 400