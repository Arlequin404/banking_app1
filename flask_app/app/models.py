from sqlalchemy.ext.declarative import declarative_base
from .create_app import db

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    full_name = db.Column(db.String(150), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class Transaction(Base):
    __tablename__ = 'transaction'
    __bind_key__ = 'db2'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())
    description = db.Column(db.String(255), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
