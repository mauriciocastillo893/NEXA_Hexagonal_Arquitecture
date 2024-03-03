class DeleteAskUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id):
        ask = self.repository.get_by_id_ask(id)
        if ask is None:
            raise Exception('Ask not found')
        else:
            self.repository.delete_ask(id)
            return True