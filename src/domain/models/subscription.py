from datetime import datetime

class Subscription:
    def __init__(self, id: int, description: str, value: int, limit: int) -> None:
        self.id = id
        self.description = description
        self.value = value
        self.limit = limit
        self.created_at = datetime.now()
        self.modified_at = datetime.now()