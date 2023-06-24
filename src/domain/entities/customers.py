from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    login = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    plan_id = Column(Integer, ForeignKey('subscriptions.id'))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
    musics = relationship("Music", back_populates="Customer")
    subscription = relationship("Subscription", back_pupulates="Customer")