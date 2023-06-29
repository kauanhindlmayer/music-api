from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infra.db.entities.record_label import RecordLabel


class Artist(Base):
    __tablename__ = 'artists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(45), nullable=False)
    record_label_id = Column(Integer, ForeignKey('record_label.id'))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)
    record_label = relationship("RecordLabel")

    def __repr__(self):
        return f"Artists [id={self.id}, name={self.name}]"
