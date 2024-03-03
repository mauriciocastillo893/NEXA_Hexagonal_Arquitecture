from Surveys.Domain.Entities.Ask import Ask as AskDomain 

class CreateAskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, ask: AskDomain):
       try:
        self.repository.save_ask(ask)
        return True, ask
       
       except Exception as e:
        return False, {"error": str(e)}