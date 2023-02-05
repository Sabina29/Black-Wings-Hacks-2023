from flask import Flask
from flask import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL']= 'sqlite:///melamarket.db'
db= SQLAlchemy(app)

from webpage import routes