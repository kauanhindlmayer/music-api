from infra.db.settings.base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP
from datetime import datetime

class RecordLabel(Base):
    __tablename__ = 'record_label'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    contract_value = Column(Integer, nullable=False)
    expire_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=True)

    def __repr__(self):
        return f"Record Labels [id={self.id}, name={self.name}]"
