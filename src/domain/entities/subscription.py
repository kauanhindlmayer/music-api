from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime

class Subscription(Base):
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    value = Column(DECIMAL(5, 2), nullable=False)
    limit = Column(Integer, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
    customers = relationship("Customer", back_populates="Subscription")