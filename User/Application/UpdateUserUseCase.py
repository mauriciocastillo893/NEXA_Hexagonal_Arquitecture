from User.Infrastructure.security.utils import get_hashed_password

class UpdateUserUseCase:
    def __init__(self, repository):
        self.repositorio = repository

    def execute(self, id, user_data):
        user = self.repositorio.get_by_id(id)
        if user is None:
            raise Exception('User not found')
        else:
            if 'password' in user_data:
                user_data['password'] = get_hashed_password(user_data['password'])
            
            valid_types = ['creator', 'respondent']
            if 'type' in user_data and user_data['type'] not in valid_types:
                raise ValueError("Invalid user type. Must be 'creator' or 'respondent'.")
            
            updated_user = self.repositorio.update(id, user_data)
            return updated_user