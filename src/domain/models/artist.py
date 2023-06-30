from datetime import datetime

class Artist:
    def __init__(self, id: int, name: str, record_label_id: int) -> None:
        self.id = id
        self.name = name
        self.record_label_id = record_label_id
        self.created_at = datetime.now()
        self.modified_at = datetime.now()