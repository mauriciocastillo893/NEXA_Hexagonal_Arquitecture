class GetSurveyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, survey_id: str):
        return self.repository.get_by_id(survey_id)