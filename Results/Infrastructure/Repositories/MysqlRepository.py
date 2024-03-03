
from Results.Domain.Entities.AResult import AResult as ResultDomain
from Results.Domain.Entities.Result import Result
from Database.mysqlConection import DBConnection, ResultsModel, AskModel

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()
        
    def save(self, result_domain: ResultDomain):
        result = ResultsModel(
            valorUno=result_domain.valorUno,
            valorDos=result_domain.valorDos,
            result_uuid=result_domain.result_uuid,
            ask_uuid=result_domain.ask_uuid  # Agregar el ask_uuid al guardar el resultado
        )
        self.session.add(result)
        self.session.commit()
        return result

    def list_all(self):
        return self.session.query(ResultsModel).all()
    
    def get_by_id(self, id):
        return self.session.query(ResultsModel).filter(ResultsModel.id == id).first()
    
    def update(self, id, result_data):
        result = self.get_by_id(id)
        result.result = Result[result_data['result']]
        self.session.commit()
        return result
    
    def delete(self, id):
        result = self.get_by_id(id)
        self.session.delete(result)
        self.session.commit()
        return result
    
    # Método para buscar una pregunta por su ask_uuid
    def get_ask_by_uuid(self, ask_uuid):
        return self.session.query(AskModel).filter(AskModel.ask_uuid == ask_uuid).first()
