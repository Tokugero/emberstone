'''
Database models for the Emberstone project.
'''

# Imports
from flask import redirect, url_for
from flask_login import UserMixin
from sqlalchemy.sql import func
from emberstone import db, login_manager


# User loader
@login_manager.user_loader
def load_user(user_id):
    '''Load user from database'''
    return User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized():
    '''Redirect unauthorized users to login page'''
    return redirect(url_for('auth.login'))


# Fire department model
class FireDepartment(db.Model):
    '''SQL Table: Fire Departments'''
    __tablename__ = 'fire_departments'
    id = db.Column(db.Integer, primary_key=True)
    nfirs_id = db.Column(db.String(5), unique=True)
    name = db.Column(db.String(100), nullable=False)
    street_number = db.Column(db.String(10))
    street_prefix = db.Column(db.String(10))
    street_name = db.Column(db.String(50))
    street_type = db.Column(db.String(10))
    street_suffix = db.Column(db.String(10))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer(9))
    phone = db.Column(db.Integer(10))
    fax = db.Column(db.Integer(10))
    email = db.Column(db.String(100))
    county_code = db.Column(db.String(3))
    status = db.Column(db.String(10), nullable=False, default='Active')
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, default=func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime(timezone=True))
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Relationships
    users = db.relationship('User', backref='fire_department', lazy=True)
    fire_station = db.relationship(
        'FireStation', backref='fire_department', lazy=True)

    def __repr__(self):
        return f"FireDepartment('{self.name}')"


# Station model
class FireStation(db.Model):
    '''SQL Table: Fire Stations'''
    __tablename__ = 'fire_stations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(10))
    street_number = db.Column(db.String(10))
    street_prefix = db.Column(db.String(10))
    street_name = db.Column(db.String(50))
    street_type = db.Column(db.String(10))
    street_suffix = db.Column(db.String(10))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer(9))
    phone = db.Column(db.Integer(10))
    fax = db.Column(db.Integer(10))
    email = db.Column(db.String(100))
    county_code = db.Column(db.String(3))
    status = db.Column(db.String(10), nullable=False, default='Active')
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, default=func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime(timezone=True))
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Relationships
    fire_department = db.relationship(
        'FireDepartment', backref='fire_stations', lazy=True)
    users = db.relationship('User', backref='fire_station', lazy=True)

    def __repr__(self):
        return f"FireStation('{self.name}')"


# User model
class User(db.Model, UserMixin):
    '''SQL Table: Users'''
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50))
    suffix = db.Column(db.String(10))
    prefix = db.Column(db.String(10))
    email = db.Column(db.String(100), unique=True, nullable=False)
    street_number = db.Column(db.String(10))
    street_prefix = db.Column(db.String(10))
    street_name = db.Column(db.String(50))
    street_type = db.Column(db.String(10))
    street_suffix = db.Column(db.String(10))
    city = db.Column(db.String(50))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer(9))
    phone = db.Column(db.Integer(10))
    fax = db.Column(db.Integer(10))
    county_code = db.Column(db.String(3))
    post_office_box = db.Column(db.String(10))
    apartment_number = db.Column(db.String(10))
    personnel_number = db.Column(db.String(10))
    rank = db.Column(db.String(10))
    password = db.Column(db.String(60), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='Active')
    created_at = db.Column(db.DateTime(timezone=True),
                           nullable=False, default=func.now())
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    updated_at = db.Column(db.DateTime(timezone=True))
    updated_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Relationships
    fire_department = db.relationship(
        'FireDepartment', backref='users', lazy=True)

    def __repr__(self):
        return f"User('{self.firstname} {self.lastname}')"
