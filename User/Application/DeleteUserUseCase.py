class DeleteUserUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id):
        user = self.repository.get_by_id(id)
        if user is None:
            raise Exception('User not found')
        else:
            self.repository.delete(id)
            return True