from flask import Blueprint, request, jsonify
from Surveys.Application.CreateAskUseCase import CreateAskUseCase
from Surveys.Domain.Entities.Ask import Ask

from CorrectResults.Infrastructure.Repositories.MysqlRepository import Repository as CRRepository
from CorrectResults.Application.CreateCorrectResultsUseCase import CreateCorrectResultsUseCase

create_ask_blueprint = Blueprint('create_ask', __name__)

def initialize_endpoints(repository):
    create_ask_use_case = CreateAskUseCase(repository)
    correctRes_repository_instance =CRRepository()
    create_corR_use_case = CreateCorrectResultsUseCase (correctRes_repository_instance)


    @create_ask_blueprint.route('/', methods=['POST'])
    def create_ask():
        ask_data = request.get_json()
        
        success, result = create_ask_use_case.execute(Ask(**ask_data))
        
        if success:
            return jsonify({"message": "Ask created", "ask": result}), 200
        else:
            return jsonify({"message": "Error creating ask", "error": result}), 400
        


