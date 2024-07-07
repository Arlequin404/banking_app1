class UserDTO:
    def __init__(self, id, username, password, email, full_name, created_at, updated_at):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.full_name = full_name
        self.created_at = created_at
        self.updated_at = updated_at

class TransactionDTO:
    def __init__(self, id, user_id, amount, date, description, transaction_type, status):
        self.id = id
        self.user_id = user_id
        self.amount = amount
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.status = status
