class GetResultUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, result_id: str):
        return self.repository.get_by_id(result_id)