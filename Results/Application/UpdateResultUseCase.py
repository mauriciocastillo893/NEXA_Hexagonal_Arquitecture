class UpdateResultUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, id, result_data):
        result = self.repository.get_by_id(id)
        if result is None:
            raise Exception('Result not found')
        else:
            updated_result = self.repository.update(id, result_data)
            return updated_result