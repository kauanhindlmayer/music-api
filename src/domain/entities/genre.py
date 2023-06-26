from infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

class Genre(Base):
    __tablename__ = 'genres'

    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"Genres [id={self.id}, description={self.description}]"

