class DeleteSurveyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, id):
        survey = self.repository.get_by_id(id)
        if survey is None:
            raise Exception('survey not found')
        else:
            self.repository.delete(id)
            return True