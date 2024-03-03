class DeleteResultUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, result_id):
        result = self.repository.get_by_id(result_id)
        if result is None:
            raise Exception('Result not found')
        else:
            self.repository.delete(result_id)
            return True