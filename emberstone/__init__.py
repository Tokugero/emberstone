'''
This file initializes the Flask app, the routes, and the database.
'''

# Imports
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail


# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')


# Flask initialization
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'data.sqlite')
app.config['SECRET_KEY'] = SECRET_KEY


# Initialize SQL database
db = SQLAlchemy(app)


# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)


# Initialize mail
mail = Mail()
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'rodneygauna@gmail.com'
app.config['MAIL_PASSWORD'] = EMAIL_PASSWORD
mail.init_app(app)
