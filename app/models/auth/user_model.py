from app.models.base_model import BaseModel, db


class UserModel(BaseModel):
    '''
    Model responsável pelo registro de dados dos usuários
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(100))
    password = db.Column(db.String(100), nullable=False)
    
    # Relacionamento 1 - 1 com a tabela roles
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = db.relationship('RoleModel', backref=db.backref('users', lazy=True))

    active = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self, first_name, last_name, email, phone, password, role_id, active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.password = password
        self.role_id = role_id
        self.active = active