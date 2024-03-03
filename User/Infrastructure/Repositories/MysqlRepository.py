from Database.mysqlConection import DBConnection, UserModel
from User.Domain.Entities.AUser import AUser as UserDomain

class Repository:
    def __init__(self):
        self.connection = DBConnection()
        self.session = self.connection.Session()

    def save(self, user_domain: UserDomain):
        user = UserModel(
            name=user_domain.contact.name,
            last_name=user_domain.contact.last_name,
            phone=str(user_domain.contact.phone),
            email=user_domain.credentials.email,
            password=user_domain.credentials.password,
            user_uuid=user_domain.user_uuid,
            type=user_domain.type.name
        )
        self.session.add(user)
        self.session.commit()
        return user

    def getAll(self):
        user = self.session.query(UserModel).all()
        return user
    
    def get_by_id(self, id):
        return self.session.query(UserModel).filter(UserModel.id == id).first()
    
    def getByEmail(self, email):
        user = self.session.query(UserModel).filter_by(email=email).first()
        return user
    
    def getByUuid(self, user_uuid):
        user = self.session.query(UserModel).filter_by(user_uuid=user_uuid).first()
        return user
    
    def update(self, id, user_data):
        user = self.get_by_id(id)
        user.name = user_data['name']
        user.last_name = user_data['last_name']
        user.phone = user_data['phone']
        user.email = user_data['email']
        user.password = user_data['password']
        user.type = user_data['type']
        self.session.commit()
        return user
    
    def delete(self, id):
        user = self.get_by_id(id)
        self.session.delete(user)
        self.session.commit()
        return user