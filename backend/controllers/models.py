from controllers.database import db
from flask_security import UserMixin, RoleMixin

class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    name = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('users', lazy='dynamic'))
    
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False) # for flask security to identify user uniquely
    fs_token_uniquifier = db.Column(db.String(255), unique=True, nullable=True)
    
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id'))
    
class Subject(db.Model):
    __tablename__="subject"
    id=db.Column(db.Integer(),primar_key=True,unique=True)  
    name=db.Column(db.String(25),unique=True)
    description=db.Column(db.String(100))