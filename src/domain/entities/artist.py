from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    record_label_id = Column(Integer, ForeignKey('record_label.id'))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
    record_label = relationship("RecordLabel", back_populates="Artist")
    musics = relationship("Music", back_populates="Artist")
