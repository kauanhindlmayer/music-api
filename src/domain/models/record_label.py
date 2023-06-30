from datetime import datetime

class RecordLabel:
    def __init__(self, id: int, name: str, contract_value: int, expired_date: int) -> None:
        self.id = id
        self.name = name
        self.contract_value = contract_value
        self.expired_date = expired_date
        self.created_at = datetime.now()
        self.modified_at = datetime.now()