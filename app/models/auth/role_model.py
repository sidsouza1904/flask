from app.models.base_model import BaseModel, db


class RoleModel(BaseModel):
    '''
    Model responsável pelo registro de regra de usuário
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)

    def __init__(self, name, position):
        self.name = name
        self.position = position