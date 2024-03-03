from Database.mysqlConection import DBConnection, SurveyModel, AskModel
from Surveys.Domain.Entities.ASurvey import ASurvey as SurveyDomain
from Surveys.Infrastructure.Repositories.MysqlRepositoryAsk import  Repository as AskRepository


class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
    def repositoryA():
        AskRepository
    
    def save(self, survey_domain: SurveyDomain):
        survey = SurveyModel(
            title=survey_domain.title,
            survey_uuid=survey_domain.survey_uuid,
        )
        self.session.add(survey)
        self.session.commit()
        return survey
    
    def get_by_title(self, title):
        return self.session.query(SurveyModel).filter(SurveyModel.title == title).first()
    
    def list_all(self):
        survey = self.session.query(SurveyModel).all()
        return survey
    
    def get_by_id(self, id):
        return self.session.query(SurveyModel).filter(SurveyModel.id == id).first()
    
    def getByUuid(self, survey_uuid):
        survey = self.session.query(SurveyModel).filter_by(survey_uuid=survey_uuid).first()
        return survey
    
    def update(self, id, survey_data):
        survey = self.get_by_id(id)
        survey.title = survey_data['title']
        self.session.commit()
        return survey
    
    def delete(self, id):
        survey = self.get_by_id(id)
        self.session.delete(survey)
        self.session.commit()
        return survey
    
