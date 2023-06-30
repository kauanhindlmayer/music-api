from datetime import datetime

class Customer:
    def __init__(self, id: int, login: str, password: str, email: str, subscription_id: int) -> None:
        self.id = id
        self.login = login
        self.password = password
        self.email = email
        self.subscription_id = subscription_id
        self.created_at = datetime.now()
        self.modified_at = datetime.now()