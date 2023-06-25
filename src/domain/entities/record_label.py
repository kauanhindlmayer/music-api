from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

class RecordLabel(Base):
    __tablename__ = 'record_label'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    contract_value = Column(Integer, nullable=False)
    expire_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
    artists = relationship("Artist", back_populates="RecordLabel")
