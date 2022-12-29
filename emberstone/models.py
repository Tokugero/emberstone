'''
Database models for the Emberstone project.
'''

# Imports
from flask import redirect, url_for
from flask_login import UserMixin
from sqlalchemy import ForeignKey, Column, Integer, String, Boolean, DateTime, Text, relationship
from emberstone import db, login_manager


# User model
class User(db.Model, UserMixin):
    '''SQL Table: Users'''
