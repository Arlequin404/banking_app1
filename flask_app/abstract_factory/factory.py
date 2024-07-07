from .dao import UserDAO, TransactionDAO

class SQLServerFactoryDB1:
    def create_user_dao(self):
        return UserDAO('db1')

class SQLServerFactoryDB2:
    def create_transaction_dao(self):
        return TransactionDAO('db2')
