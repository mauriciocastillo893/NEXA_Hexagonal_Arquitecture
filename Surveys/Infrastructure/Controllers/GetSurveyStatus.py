from flask import Blueprint, request, jsonify
from Surveys.Application.GetSurveyUseCase import GetSurveyUseCase

get_survey_status_blueprint = Blueprint('get_survey_status', __name__)

def initialize_endpoints(repository):
    getSurveyUseCase = GetSurveyUseCase(repository)

    @get_survey_status_blueprint.route('/<int:id>', methods=['GET'])
    def get_pot_survey_status(id):
        try:
            # Usar el caso de uso para obtener la encuesta con todo su contenido
            survey = getSurveyUseCase.execute(id)

            # Inicializar la lista para almacenar los resultados de la comparación
            comparison_results = []

            # Iterar sobre cada pregunta en la encuesta
            for ask in survey.asks:
                # Verificar si existe CorrectResult
                correct_result_data = None
                if ask.correct_result:
                    correct_result_data = {
                        'valueUno': ask.correct_result.valueUno,
                        'valueDos': ask.correct_result.valueDos
                    }
                
                # Verificar si existe Result
                result_data = None
                if ask.result:
                    result_data = {
                        'valorUno': ask.result.valorUno,
                        'valorDos': ask.result.valorDos
                    }
                
                # Verificar si tanto CorrectResult como Result existen antes de comparar
                if correct_result_data and result_data:
                    # Comparar los datos de CorrectResult y Result para la pregunta actual
                    comparison_result = correct_result_data['valueUno'] == result_data['valorUno'] and correct_result_data['valueDos'] == result_data['valorDos']
                else:
                    # Si uno de los objetos es None, considerarlo como comparación no exitosa
                    comparison_result = False
                
                # Agregar el resultado de la comparación a la lista
                comparison_results.append(comparison_result)

            # Retorna los resultados de comparación en formato JSON
            return jsonify({"comparison_results": comparison_results}), 200

        
        except Exception as e:
            # En caso de error, retorna un mensaje de error
            return jsonify({"message": "Error processing request", "error": str(e)}), 400



