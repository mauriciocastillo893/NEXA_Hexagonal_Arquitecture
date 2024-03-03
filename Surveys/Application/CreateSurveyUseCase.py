from Surveys.Domain.Entities.ASurvey import ASurvey as SurveyDomain 

class CreateSurveyUseCase:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, survey: SurveyDomain):
       title_exist = self.repository.get_by_title(survey.title)
       if title_exist is not None:
        return False, {"error": "it already exists."}
       
       try:
        self.repository.save(survey)
        return True, survey
       
       except Exception as e:
        return False, {"error": str(e)}