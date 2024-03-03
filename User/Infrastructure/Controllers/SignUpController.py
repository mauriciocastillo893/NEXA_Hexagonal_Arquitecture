from flask import Blueprint, request, jsonify
from User.Application.SignUpUseCase import SignUpUseCase
from User.Domain.Entities.AUser import AUser
from User.Domain.Entities.Contact import Contact
from User.Domain.Entities.Credentials import Credentials
from User.Domain.Entities.UserType import UserType

signup_blueprint = Blueprint('user_signUp', __name__)

def initialize_endpoints(repository):
    createUserUsercase = SignUpUseCase(repository)

    @signup_blueprint.route('/', methods=['POST'])
    def user_signUp():
        try:
            user_data = request.get_json()
            contact = Contact(name=user_data['name'], last_name=user_data['last_name'], phone=user_data['phone'])
            credentials = Credentials(email=user_data['email'], password=user_data['password'])
            user_type= UserType(user_data['type'].upper())
            user = AUser(contact=contact, credentials=credentials, type=user_type)
            user_created, message = createUserUsercase.execute(user)
            if user_created:
                return jsonify({"message": "User created", "user": user_created}), 200
            else:
                return jsonify({"message": message["error"]}), 400
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500