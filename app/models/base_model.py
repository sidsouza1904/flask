from datetime import datetime
from pytz import timezone

from app import db


# Verificando o fuso horário
time_zone = timezone('America/Sao_Paulo')

class BaseModel(db.Model):
    '''
    Model base para registro de auditoria e exclusão lógica.
    '''
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(time_zone), nullable=False)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(time_zone), onupdate=lambda: datetime.now(time_zone), nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
