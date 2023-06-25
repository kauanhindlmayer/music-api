from infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    payment_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"Payments [id={self.id}, payment_date={self.payment_date}]"
 