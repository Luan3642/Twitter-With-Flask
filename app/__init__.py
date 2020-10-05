from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# instância do flask, essa instância recebe uma variável
# essa variável vai controlar a aplicação inteira 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'


from app.controllers import default 
