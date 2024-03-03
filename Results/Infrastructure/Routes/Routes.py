from Results.Infrastructure.Controllers.CreateResultController import create_result_blueprint, initialize_endpoints as initialize_endpoints_create_result
from Results.Infrastructure.Controllers.ListResultController import get_list_result_blueprint, initialize_endpoints as initialize_endpoints_list_result
from Results.Infrastructure.Controllers.GetResultByIdController import get_Result_blueprint, initialize_endpoints as initialize_endpoints_get_result
from Results.Infrastructure.Controllers.UpdateResultController import update_result_blueprint, initialize_endpoints as initialize_endpoints_update_result
from Results.Infrastructure.Controllers.DeleteResultController import delete_result_blueprint, initialize_endpoints as initialize_endpoints_delete_result

def initialize_app(app,repository):
    initialize_endpoints_create_result(repository)
    initialize_endpoints_list_result(repository)
    initialize_endpoints_get_result(repository)
    initialize_endpoints_update_result(repository)
    initialize_endpoints_delete_result(repository)
    
    app.register_blueprint(create_result_blueprint, url_prefix="/create-result")
    app.register_blueprint(get_list_result_blueprint, url_prefix="/list-result")
    app.register_blueprint(get_Result_blueprint, url_prefix="/get-result")
    app.register_blueprint(update_result_blueprint, url_prefix="/update-result")
    app.register_blueprint(delete_result_blueprint, url_prefix="/delete-result")

