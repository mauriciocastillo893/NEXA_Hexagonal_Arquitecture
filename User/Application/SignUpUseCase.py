from User.Domain.Entities.AUser import AUser as UserDomain
from User.Infrastructure.security.utils import get_hashed_password

class SignUpUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user: UserDomain):
        user_exist = self.repository.getByEmail(user.credentials.email)
        if user_exist is not None:
            return False, {"error": "Eamil already exist in the system. Please use another email."}
        try:
            user.credentials.password = get_hashed_password(user.credentials.password)
            self.repository.save(user)
            return True, user
        except Exception as e:
            return False, {"error": str(e)}