class UpdateAskUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, id, ask_data):
        ask = self.repository.get_by_id_ask(id)
        if ask is None:
            raise Exception('ask not found')
        else:
            updated_ask = self.repository.update_ask(id, ask_data)
            return updated_ask