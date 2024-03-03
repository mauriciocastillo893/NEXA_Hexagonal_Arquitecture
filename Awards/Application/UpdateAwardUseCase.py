class UpdateAwardUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, id, award_data):
        award = self.repository.get_by_id(id)
        if award is None:
            raise Exception('Award not found')
        else:
            updated_award = self.repository.update(id, award_data)
            return updated_award