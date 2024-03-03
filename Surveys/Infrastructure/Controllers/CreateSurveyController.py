from flask import Blueprint, request, jsonify
from Surveys.Application.CreateSurveyUseCase import CreateSurveyUseCase
from Surveys.Domain.Entities.ASurvey import ASurvey
from Surveys.Domain.Entities.Ask import Ask 
from Surveys.Application.CreateAskUseCase import CreateAskUseCase
from Surveys.Infrastructure.Repositories.MysqlRepositoryAsk import Repository as AskRepository
from CorrectResults.Domain.Entities.ACorrectResults import ACorrectResults
from CorrectResults.Application.CreateCorrectResultsUseCase import CreateCorrectResultsUseCase
from CorrectResults.Infrastructure.Repositories.MysqlRepository import Repository as CorrectResultRepository

create_survey_blueprint = Blueprint('create_survey', __name__)

def initialize_endpoints(repository):
    create_survey_use_case = CreateSurveyUseCase(repository)
    ask_repository_instance = AskRepository()  # Crear una instancia de AskRepository
    create_ask_use_case = CreateAskUseCase(ask_repository_instance)  # Usar la instancia creada
    correct_result_repository_instance = CorrectResultRepository()  # Crear una instancia de CorrectResultRepository
    create_correct_result_use_case = CreateCorrectResultsUseCase(correct_result_repository_instance)  # Usar la instancia creada

    @create_survey_blueprint.route('/', methods=['POST'])
    def create_survey():
        survey_data = request.get_json()
        asks_data = survey_data.pop('asks', [])

        survey = ASurvey(**survey_data)
        success, result = create_survey_use_case.execute(survey)
        
        if success:
            survey_uuid = result.survey_uuid # Suponiendo que result contiene la encuesta creada
            
            for ask_data in asks_data:
                ask_data['survey_uuid'] = survey_uuid
                ask = Ask(**ask_data)
                success, created_ask = create_ask_use_case.execute(ask)  # Llamar al método execute con el objeto Ask
                
                correct_result_data = ask_data.get('correct_result')

                if correct_result_data: 
                    correct_result_data['ask_uuid'] = created_ask.ask_uuid
                    correct_result = ACorrectResults(**correct_result_data)
                    success, _ = create_correct_result_use_case.execute(correct_result)
                    if not success:
                        return jsonify({"message": "Error creating correct result", "error": "Error creating correct result"}), 400
            
            return jsonify({"message": "Survey created", "survey": result.to_dict()}), 200
        else:
            return jsonify({"message": "Error creating survey", "error": result}), 400
