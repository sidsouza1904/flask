from flask import Flask, request, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
from functools import wraps

import config
from mapping_roles import mapping_roles


app = Flask(__name__)
app.secret_key = config.SECRET_KEY_FLASK
app.config.from_object('config')

# Instância do banco de dados
db = SQLAlchemy()
db.init_app(app)


# Instância do migrate
migrate = Migrate(app, db)


# Instância do login
login_manager = LoginManager()

@login_manager.unauthorized_handler
def unauthorized():
    if request.endpoint != 'login':
        flash(('Você estar logado para acessar esta página', 'warning'))
    return redirect(url_for('login'))


# Controle de acesso por permissões
def requires_roles(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        endpoint = request.endpoint
        requires_roles = mapping_roles.get(endpoint, [])

        # Cargo do ususário
        user_role = current_user.role.name

        if user_role not in requires_roles:
            return render_template()
        
        return f(*args, **kwargs)
    
    return wrapped



# Registrar todas as models
from app.models import base_model  # noqa: E402, F401
from app.models.auth import user_model, role_model  # noqa: E402, F401

# Registrar todas as views
from app.views.home import home_view  # noqa: E402, F401
