from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from src.infra.db.entities.subscription import Subscription

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    login = Column(String(45), nullable=False)
    password = Column(String(60), nullable=False)
    email = Column(String(45), nullable=False)
    subscription_id = Column(Integer, ForeignKey('subscriptions.id'))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)
    subscription = relationship("Subscription")

    def __repr__(self):
        return f"Customers [id={self.id}, email={self.email}]"