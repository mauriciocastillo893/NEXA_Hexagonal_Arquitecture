from User.Infrastructure.security.utils import verify_password, create_custom_access_token
class SignInUseCase:
    def __init__(self, repository):
        self.repositorio = repository
    
    def execute(self, email, password):
        user = self.repositorio.getByEmail(email)
        if user is None:
            return None
        if not verify_password(password, user.password):
            return None
        access_token = create_custom_access_token(subject=user.email, user_role=user.type.value)
        return access_token