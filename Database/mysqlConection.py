from sqlalchemy import create_engine, Column, Integer, String, Enum
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv
from User.Domain.Entities.UserType import UserType
from Results.Domain.Entities.Result import Result
from CorrectResults.Domain.Entities.Type_status import Type_status
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False, unique=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120), nullable=False)
    user_uuid = Column(String(36), unique=True)
    type = Column(Enum(UserType))
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'last_name': self.last_name,
            'phone': self.phone,
            'email': self.email,
            'password': self.password,
            'user_uuid': self.user_uuid,
            'type': self.type.value
        }


class SurveyModel(Base):
    __tablename__ = 'surveys'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    survey_uuid = Column(String(36), unique=True)

    asks = relationship("AskModel", back_populates="survey")  # Relación con las preguntas

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'survey_uuid': self.survey_uuid,
            'asks': [ask.to_dict() for ask in self.asks]
        }

class AwardModel(Base):
    __tablename__ = 'awards'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    award_uuid = Column(String(36), unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'award_uuid': self.award_uuid
        }

class ResultsModel(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_uuid = Column(String(36), unique=True)
    valorUno = Column(String(50), nullable=False)
    valorDos = Column(String(50), nullable=False)
    ask_uuid = Column(String(36), ForeignKey('asks.ask_uuid'))  # Agregar esta línea para definir la columna ask_uuid
    ask = relationship("AskModel", back_populates="result")  # Definir la relación

    def to_dict(self):
        return {
            'id': self.id,
            'valorUno': self.valorUno,
            'valorDos': self.valorDos,
            'result_uuid': self.result_uuid,
        }
    
class AskModel(Base):
    __tablename__ = 'asks'
    id = Column(Integer, primary_key=True)
    ask = Column(String(50), nullable=False)
    ask_uuid = Column(String(36), unique=True)
    survey_uuid = Column(String(36), ForeignKey('surveys.survey_uuid'), nullable=False)

    survey = relationship("SurveyModel", back_populates="asks")  # Relación inversa
    # Relación uno a uno con CorrectResultsModel usando UUID
    correct_result = relationship("CorrectResultsModel", uselist=False, back_populates="ask")
    # Agregar relación uno a uno con ResultsModel usando UUID
    result = relationship("ResultsModel", uselist=False, back_populates="ask")

    def to_dict(self):
        return {
            'id': self.id,
            'ask': self.ask,
            'ask_uuid': self.ask_uuid,
            'survey_uuid': self.survey_uuid,
            'correct_result': self.correct_result.to_dict() if self.correct_result else None,  # Convertir la respuesta correcta a un diccionario si existe
            'result': self.result.to_dict() if self.result else None  # Convertir el resultado asociado a un diccionario si existe
        }
    
class CorrectResultsModel(Base):
    __tablename__ = 'CorrectResults'
    id = Column(Integer, primary_key=True)
    valorUno = Column(String(50), nullable=False)
    valorDos = Column(String(50), nullable=False)
    valueDos = Column(Enum(Type_status))
    valueUno = Column(Enum(Type_status))
    correctResults_uuid = Column(String(36), unique=True)
    
    # Definir relación uno a uno con AskModel usando UUID
    ask_uuid = Column(String(36), ForeignKey('asks.ask_uuid'), unique=True)
    ask = relationship("AskModel", back_populates="correct_result")
    
    def to_dict(self):
        return {
            'id': self.id,
            'valorUno': self.valorUno,
            'valorDos': self.valorDos,
            'valueUno': self.valueUno.value,
            'valueDos': self.valueDos.value,
            'correctResults_uuid': self.correctResults_uuid
        }




class DBConnection:
    def __init__(self):
        load_dotenv()

        host = os.getenv('DB.HOST_MYSQL')
        port = os.getenv('DB.PORT_MYSQL')
        user = os.getenv('DB.USER_MYSQL')
        password = os.getenv('DB.PASSWORD_MYSQL')
        database = os.getenv('DB.DATABASE_MYSQL')

        try:
            self.engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
            Base.metadata.create_all(self.engine)
            self.Session = sessionmaker(bind=self.engine)
            print("Conexión exitosa a la base de datos con MySQL LISTA!")
        except Exception as e:
            print(f"Error al conectar a la base de datos: {str(e)}")