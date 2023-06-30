from datetime import datetime

class Music:
    def __init__(self, id: int, name: str, duration: str, genre_id: int, release_date: str) -> None:
        self.id = id
        self.name = name
        self.duration = duration
        self.genre_id = genre_id
        self.release_date = release_date
        self.created_at = datetime.now()
        self.modified_at = datetime.now()