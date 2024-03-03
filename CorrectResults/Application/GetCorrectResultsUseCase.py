class GetCorrectResultsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, correct_id: str):
        return self.repository.get_by_id(correct_id)