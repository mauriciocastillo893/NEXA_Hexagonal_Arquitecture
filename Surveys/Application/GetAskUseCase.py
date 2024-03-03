class GetAskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, ask_id: str):
        return self.repository.get_by_id_ask(ask_id)