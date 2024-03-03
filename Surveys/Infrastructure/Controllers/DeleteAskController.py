from flask import Blueprint, jsonify
from Surveys.Application.DeleteAskUseCase import DeleteAskUseCase 

delete_ask_blueprint = Blueprint('delete_ask', __name__)

def initialize_endpoints(repositorio):
    deleteAskUseCase = DeleteAskUseCase(repositorio)

    @delete_ask_blueprint.route('/<int:id>', methods=['DELETE'])
    def delete_ask(id):
        try:
            deleteAskUseCase.execute(id)
            return jsonify({'message': 'ask deleted'}), 200
        except Exception as e:
               return jsonify({'message': 'Error deleted',"error": str(e)}), 400
        
