from Results.Domain.Entities.AResult import AResult as ResultDomain

class CreateResultUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, result: ResultDomain):
        try:
            self.repository.save(result)
            return True, result
        except Exception as e:
            return False, {"error": str(e)}