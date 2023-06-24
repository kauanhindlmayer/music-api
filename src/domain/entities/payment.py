from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

class Payment(Base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    payment_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)
 