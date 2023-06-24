from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from datetime import datetime

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    value = Column(DECIMAL(5, 2), nullable=False)
    limit = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
