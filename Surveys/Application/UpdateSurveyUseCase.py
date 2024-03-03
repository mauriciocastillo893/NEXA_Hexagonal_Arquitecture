class UpdateSurveyUseCase:
    def __init__(self, repository):
        self.repository = repository
        
    def execute(self, id, survey_data):
        survey = self.repository.get_by_id(id)
        if survey is None:
            raise Exception('Survey not found')
        else:
            updated_survey = self.repository.update(id, survey_data)
            return updated_survey