from flask import Flask
from User.Infrastructure.Controllers.SignUpController import signup_blueprint, initialize_endpoints as initialize_endpoints_signup
from User.Infrastructure.Controllers.ListUserController import get_list_users_blueprint, initialize_endpoints as initialize_endpoints_list_users
from User.Infrastructure.Controllers.GetUserByIdController import get_user_blueprint, initialize_endpoints as initialize_endpoints_get_user
from User.Infrastructure.Controllers.UpdateUserController import update_user_blueprint, initialize_endpoints as initialize_endpoints_update_user
from User.Infrastructure.Controllers.DeleteUserController import delete_user_blueprint, initialize_endpoints as initialize_endpoints_delete_user
from User.Infrastructure.Controllers.SignInController import signin_blueprint, initialize_endpoints as initialize_endpoints_signin
from User.Infrastructure.security.utils import configure_jwt
from User.Infrastructure.Controllers.AwardOutcomeController import award_outcome_blueprint, initialize_endpoints as initialize_endpoints_award_outcome

def initialize_app(app, repositorio):
    configure_jwt(app)
    initialize_endpoints_signup(repositorio)
    initialize_endpoints_list_users(repositorio)
    initialize_endpoints_get_user(repositorio)
    initialize_endpoints_update_user(repositorio)
    initialize_endpoints_delete_user(repositorio)
    initialize_endpoints_signin(repositorio)
    initialize_endpoints_award_outcome()
    
    
    app.register_blueprint(signup_blueprint, url_prefix="/signup")
    app.register_blueprint(get_list_users_blueprint, url_prefix="/list-users")
    app.register_blueprint(get_user_blueprint, url_prefix="/get-user")
    app.register_blueprint(update_user_blueprint, url_prefix="/update-user")
    app.register_blueprint(delete_user_blueprint, url_prefix="/delete-user")
    app.register_blueprint(signin_blueprint, url_prefix="/signin")
    app.register_blueprint(award_outcome_blueprint, url_prefix="/award-outcome")