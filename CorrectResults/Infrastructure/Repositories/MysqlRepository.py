from Database.mysqlConection import DBConnection, CorrectResultsModel
from CorrectResults.Domain.Entities.ACorrectResults import ACorrectResults as CorrectResultDomain
from CorrectResults.Domain.Entities.Type_status import Type_status

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
        
    def save(self, correct_domain: CorrectResultDomain):
        correct = CorrectResultsModel(
            valorUno=correct_domain.valorUno,
            valorDos=correct_domain.valorDos,
            valueUno=correct_domain.valueUno,
            valueDos=correct_domain.valueDos,
            correctResults_uuid=correct_domain.correctResults_uuid,
            ask_uuid=correct_domain.ask_uuid  # Asegúrate de incluir el ask_uuid aquí
        )
        self.session.add(correct)
        self.session.commit()
        return correct

    def list_all(self):
        correct = self.session.query(CorrectResultsModel).all()
        return correct
    
    def get_by_id(self, id):
        return self.session.query(CorrectResultsModel).filter(CorrectResultsModel.id == id).first()
    
    def update(self, id, correct_data):
        correct = self.get_by_id(id)
        correct.valorUno = correct_data['valorUno']
        correct.valorDos = correct_data['valorDos']
        correct.valueUno = Type_status[correct_data['valueUno']]
        correct.valueDos = Type_status[correct_data['valueDos']]
        self.session.commit()
        return correct
    
    def delete(self, id):
        correct = self.get_by_id(id)
        self.session.delete(correct)
        self.session.commit()
        return correct
