from Database.mysqlConection import DBConnection, AwardModel
from Awards.Domain.Entities.AAward import AAward as AwardDomain

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
        
    def save(self, award_domain: AwardDomain):
        award = AwardModel(
            name=award_domain.name,
            description=award_domain.description,
            award_uuid=award_domain.award_uuid
        )
        self.session.add(award)
        self.session.commit()
        return award
    
    def get_by_name(self, name):
        return self.session.query(AwardModel).filter(AwardModel.name == name).first()
    
    def list_all(self):
        award = self.session.query(AwardModel).all()
        return award
    
    def get_by_id(self, id):
        return self.session.query(AwardModel).filter(AwardModel.id == id).first()
    
    def getByUuid(self, award_uuid):
        award = self.session.query(AwardModel).filter_by(award_uuid=award_uuid).first()
        return award
    
    def update(self, id, award_data):
        award = self.get_by_id(id)
        award.name = award_data['name']
        award.description = award_data['description']
        self.session.commit()
        return award
    
    def delete(self, id):
        award = self.get_by_id(id)
        self.session.delete(award)
        self.session.commit()
        return award