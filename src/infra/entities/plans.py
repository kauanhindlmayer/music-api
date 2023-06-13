from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from datetime import datetime
from src.infra.config import Base


class Plans(Base):
    """Plans Entity"""

    __tablename__ = "plans"
    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    value = Column(DECIMAL(5, 2), nullable=False)
    limit = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    modified_at = Column(TIMESTAMP, nullable=False, default=datetime.now)

    def __rep__(self):
        return f"Plan [plan=(self.description)]"
