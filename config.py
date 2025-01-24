# ---------------------------------------- Configurações Gerais --------------------------------------------------- #
SECRET_KEY_FLASK = 'mysecretkeyflask'

# ------------------------------------------- Banco de Dados ------------------------------------------------------ #

SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"
SQLALCHEMY_TRACK_MODIFICATIONS = False  # Quando alterar alguma informação na migration, altera no banco de dados