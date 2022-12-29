'''
CLI Commands for the website app
'''

# Imports
from flask import Blueprint
from .. import db

# Blueprint Configuration
commands_bp = Blueprint('commands', __name__)


# Flask CLI commands
@commands_bp.cli.command('db_create')
def db_create():
    '''Use "flask db_create" to create the database in the terminal'''
    db.create_all()
    print('Database created')


@commands_bp.cli.command('db_drop')
def db_drop():
    '''Use "flask db_drop" to drop the database in the terminal'''
    db.drop_all()
    print('Database dropped')
