from Awards.Infrastructure.Controllers.CreateAwardController import create_award_blueprint, initialize_endpoints as initialize_endpoints_create_award
from Awards.Infrastructure.Controllers.ListAwardController import get_list_awards_blueprint, initialize_endpoints as initialize_endpoints_list_awards
from Awards.Infrastructure.Controllers.GetAwardByIdController import get_Award_blueprint, initialize_endpoints as initialize_endpoints_get_award
from Awards.Infrastructure.Controllers.UpdateAwardController import update_award_blueprint, initialize_endpoints as initialize_endpoints_update_award
from Awards.Infrastructure.Controllers.DeleteAwardController import delete_award_blueprint, initialize_endpoints as initialize_endpoints_delete_award


def initialize_app(app,repository):
    initialize_endpoints_create_award(repository)
    initialize_endpoints_list_awards(repository)
    initialize_endpoints_get_award(repository)
    initialize_endpoints_update_award(repository)
    initialize_endpoints_delete_award(repository)
    
    app.register_blueprint(create_award_blueprint, url_prefix="/create-award")
    app.register_blueprint(get_list_awards_blueprint, url_prefix="/list-awards")
    app.register_blueprint(get_Award_blueprint, url_prefix="/get-award")
    app.register_blueprint(update_award_blueprint, url_prefix="/update-award")
    app.register_blueprint(delete_award_blueprint, url_prefix="/delete-award")