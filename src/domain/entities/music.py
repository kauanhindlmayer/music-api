from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime


class Music(Base):
    __tablename__ = 'musics'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    duration = Column(TIMESTAMP, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    release_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)
    genre = relationship("Genre")

    def __repr__(self):
        return f"Musics [id={self.id}, name={self.name}]"
