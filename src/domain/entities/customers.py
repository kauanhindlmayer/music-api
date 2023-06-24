from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    login = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)
    plan_id = Column(Integer, ForeignKey('plans.id'))
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
 