from Database.mysqlConection import DBConnection, AskModel
from Surveys.Domain.Entities.Ask import Ask as AskDomain

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
 
    def save_ask(self, ask_domain: AskDomain):
        ask = AskModel(
            ask=ask_domain.ask,
            ask_uuid=ask_domain.ask_uuid,
            survey_uuid=ask_domain.survey_uuid  # Asignar el ID de la encuesta asociada
        )
        self.session.add(ask)
        self.session.commit()
        return ask

    
    def get_by_ask(self, ask):
        return self.session.query(AskModel).filter(AskModel.ask == ask).first()
    
    def list_all_ask(self):
        ask = self.session.query(AskModel).all()
        return ask
    
    def get_by_id_ask(self, id):
        return self.session.query(AskModel).filter(AskModel.id == id).first()
    
    def update_ask(self, id, ask_data):
        ask = self.get_by_id_ask(id)
        ask.ask = ask_data['ask']
        self.session.commit()
        return ask
    
    def delete_ask(self, id):
        ask = self.get_by_id_ask(id)
        self.session.delete(ask)
        self.session.commit()
        return ask