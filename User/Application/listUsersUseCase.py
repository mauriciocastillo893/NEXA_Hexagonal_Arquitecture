class ListUsersUseCase:
    def __init__(self, user_repo):
        self.user_repo = user_repo

    def execute(self):
        return self.user_repo.getAll()