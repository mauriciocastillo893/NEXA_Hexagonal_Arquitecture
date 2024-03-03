from CorrectResults.Domain.Entities.ACorrectResults import ACorrectResults as CorrectDomain

class CreateCorrectResultsUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, correct: CorrectDomain):
        try:
            self.repository.save(correct)
            return True, correct
        except Exception as e:
            return False, {"error": str(e)}