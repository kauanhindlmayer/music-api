from datetime import datetime

class Payment:
    def __init__(self, id: int, payment_date: str) -> None:
        self.id = id
        self.payment_date = payment_date
        self.created_at = datetime.now()
        self.modified_at = datetime.now()