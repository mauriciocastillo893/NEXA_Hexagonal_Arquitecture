from flask import Blueprint, request, jsonify
from User.Application.SignInUseCase import SignInUseCase

signin_blueprint = Blueprint('user_signIn', __name__)

def initialize_endpoints(repository):
    signInUsercase = SignInUseCase(repository)

    @signin_blueprint.route('/', methods=['POST'])
    def user_signIn():
        try:
            user_data = request.get_json()
            email = user_data['email']
            password = user_data['password']
            token = signInUsercase.execute(email, password)
            if token:
                return jsonify({"message": "User Entering", "token": token}), 200
            else:
                return jsonify({"message": "Incorrect Credentials"}), 400
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500