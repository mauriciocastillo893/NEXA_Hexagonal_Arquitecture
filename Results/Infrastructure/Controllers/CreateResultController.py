from flask import Blueprint, request, jsonify
from Results.Domain.Entities.AResult import AResult
from Results.Application.CreateResultUseCase import CreateResultUseCase

create_result_blueprint = Blueprint('create_result', __name__)

def initialize_endpoints(repository):
    create_result_use_case = CreateResultUseCase(repository)

    @create_result_blueprint.route('/', methods=['POST'])
    def create_result():
        try:
            result_data = request.get_json()
            ask_uuid = result_data.pop('ask_uuid', None)  # Extraer ask_uuid
            if ask_uuid is None:
                return jsonify({"message": "Error creating result", "error": "ask_uuid is required"}), 400
            
            # Aquí buscar el ask_uuid en la base de datos
            ask = repository.get_ask_by_uuid(ask_uuid)
            if ask is None:
                return jsonify({"message": "Error creating result", "error": "ask_uuid not found"}), 400
            
            # Si el ask_uuid existe, se procede a crear el resultado
            success, result = create_result_use_case.execute(AResult(**result_data, ask_uuid=ask_uuid))
            
            if success:
                return jsonify({"message": "Result created", "result": result}), 200
            else:
                return jsonify({"message": "Error creating result", "error": result}), 400
        except Exception as e:
            return jsonify({"message": "Error creating result", "error": str(e)}), 400
