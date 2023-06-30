from datetime import datetime

class Genre:
    def __init__(self, id: int, description: str) -> None:
        self.id = id
        self.description = description
        self.created_at = datetime.now()
        self.modified_at = datetime.now()