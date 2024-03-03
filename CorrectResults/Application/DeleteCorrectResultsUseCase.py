class DeleteCorrectResultsUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, correct_id):
        correct = self.repository.get_by_id(correct_id)
        if correct is None:
            raise Exception('Correct Results not found')
        else:
            self.repository.delete(correct_id)
            return True