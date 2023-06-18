from src.infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime


class Genre(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    modified_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
