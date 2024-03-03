from CorrectResults.Infrastructure.Controllers.CreateCorrectResultController import create_correct_result_blueprint, initialize_endpoints as initialize_endpoints_create_result_correct
from CorrectResults.Infrastructure.Controllers.ListCorrectResultController import get_list_correct_result_blueprint, initialize_endpoints as initialize_endpoints_list_result_correct
from CorrectResults.Infrastructure.Controllers.GetCorrectResultByIdController import get_Correct_Result_blueprint, initialize_endpoints as initialize_endpoints_get_result_correct
from CorrectResults.Infrastructure.Controllers.UpdateCorrectResultController import update_correct_result_blueprint, initialize_endpoints as initialize_endpoints_update_result_correct
from CorrectResults.Infrastructure.Controllers.DeleteCorrectResultController import delete_correct_result_blueprint, initialize_endpoints as initialize_endpoints_delete_result_correct

def initialize_app(app,repository):
    initialize_endpoints_create_result_correct(repository)
    initialize_endpoints_list_result_correct(repository)
    initialize_endpoints_get_result_correct(repository)
    initialize_endpoints_update_result_correct(repository)
    initialize_endpoints_delete_result_correct(repository)
    
    app.register_blueprint(create_correct_result_blueprint, url_prefix="/create-correct")
    app.register_blueprint(get_list_correct_result_blueprint, url_prefix="/list-correct")
    app.register_blueprint(get_Correct_Result_blueprint, url_prefix="/get-correct")
    app.register_blueprint(update_correct_result_blueprint, url_prefix="/update-correct")
    app.register_blueprint(delete_correct_result_blueprint, url_prefix="/delete-correct")

#pene pene pene pene pito chupas