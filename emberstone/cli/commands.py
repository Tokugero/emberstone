'''
CLI Commands for the website app
'''

# Imports
from datetime import datetime
from flask import Blueprint
from werkzeug.security import generate_password_hash
from emberstone.models import FireDepartment, FireStation, User
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


@commands_bp.cli.command('db_seed')
def db_seed():
    '''Use "flask db_seed" to seed the database in the terminal'''
    # Test Fire Department
    test_fire_department = FireDepartment(
        name='Test Fire Department',
        status='Active',
        created_at=datetime.now())

    # Test User
    test_user = User(
        fire_department_id=1,
        firstname='Test',
        lastname='User',
        email='testuser@emberstone.io',
        password=generate_password_hash('testuser', method='sha256'),
        status='Active',
        created_at=datetime.now())

    # Add to database
    db.session.add(test_fire_department)
    db.session.add(test_user)
    db.session.commit()
    print('Database seeded')
