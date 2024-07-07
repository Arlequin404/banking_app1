from flask_app.app.models import User, Transaction
from flask_app.app.create_app import db
from .dto import UserDTO, TransactionDTO

class UserDAO:
    def __init__(self, database):
        self.database = database

    def get_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            return UserDTO(user.id, user.username, user.password, user.email, user.full_name, user.created_at, user.updated_at)
        return None

    def get_user_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            return UserDTO(user.id, user.username, user.password, user.email, user.full_name, user.created_at, user.updated_at)
        return None

    def create_user(self, user_dto):
        new_user = User(
            username=user_dto.username,
            password=user_dto.password,
            email=user_dto.email,
            full_name=user_dto.full_name
        )
        db.session.add(new_user)
        db.session.commit()

    def update_user(self, user_dto):
        user = User.query.get(user_dto.id)
        if user:
            user.username = user_dto.username
            user.password = user_dto.password
            user.email = user_dto.email
            user.full_name = user_dto.full_name
            db.session.commit()

    def delete_user(self, user_id):
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()

class TransactionDAO:
    def __init__(self, database):
        self.database = database

    def get_transaction(self, transaction_id):
        transaction = Transaction.query.with_bind_key('db2').get(transaction_id)
        if transaction:
            return TransactionDTO(transaction.id, transaction.user_id, transaction.amount, transaction.date, transaction.description, transaction.transaction_type, transaction.status)
        return None

    def create_transaction(self, transaction_dto):
        new_transaction = Transaction(
            user_id=transaction_dto.user_id,
            amount=transaction_dto.amount,
            description=transaction_dto.description,
            transaction_type=transaction_dto.transaction_type,
            status=transaction_dto.status
        )
        db.session.add(new_transaction)
        db.session.commit()

    def update_transaction(self, transaction_dto):
        transaction = Transaction.query.with_bind_key('db2').get(transaction_dto.id)
        if transaction:
            transaction.user_id = transaction_dto.user_id
            transaction.amount = transaction_dto.amount
            transaction.description = transaction_dto.description
            transaction.transaction_type = transaction_dto.transaction_type
            transaction.status = transaction_dto.status
            db.session.commit()

    def delete_transaction(self, transaction_id):
        transaction = Transaction.query.with_bind_key('db2').get(transaction_id)
        if transaction:
            db.session.delete(transaction)
            db.session.commit()
