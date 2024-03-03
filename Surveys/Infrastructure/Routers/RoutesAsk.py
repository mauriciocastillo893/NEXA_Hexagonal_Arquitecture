
from Surveys.Infrastructure.Controllers.CreateAskController import create_ask_blueprint, initialize_endpoints as initialize_endpoints_create_ask
from Surveys.Infrastructure.Controllers.DeleteAskController import delete_ask_blueprint,initialize_endpoints as initialize_endpoints_delete_ask
from Surveys.Infrastructure.Controllers.GetAskByIdController import get_ask_blueprint, initialize_endpoints as initialize_endpoints_getId_ask
from Surveys.Infrastructure.Controllers.ListAskController import get_list_ask_blueprint, initialize_endpoints as initialize_endpoints_get_list_ask
from Surveys.Infrastructure.Controllers.UpdateAskController import update_ask_blueprint, initialize_endpoints as initialize_endpoints_update_ask

def initialize_app(app,repository):
    initialize_endpoints_create_ask(repository)
    initialize_endpoints_delete_ask(repository)
    initialize_endpoints_getId_ask(repository)
    initialize_endpoints_get_list_ask(repository)
    initialize_endpoints_update_ask(repository)

    app.register_blueprint(create_ask_blueprint,url_prefix="/create-ask")
    app.register_blueprint(delete_ask_blueprint,url_prefix="/delete-ask")
    app.register_blueprint(get_ask_blueprint,url_prefix="/get-ask")
    app.register_blueprint(get_list_ask_blueprint,url_prefix="/get-list-ask")
    app.register_blueprint(update_ask_blueprint,url_prefix="/update-ask")

