class UpdateCorrectResultUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, id, correct_data):
        correct = self.repository.get_by_id(id)
        if correct is None:
            raise Exception('Correct Result not found')
        else:
            updated_correct = self.repository.update(id, correct_data)
            return updated_correct