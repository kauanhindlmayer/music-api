from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from datetime import datetime

class RecordLabel(Base):
    __tablename__ = 'record_label'
    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    contract_value = Column(Integer, nullable=False)
    expire_date = Column(TIMESTAMP, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, default=datetime.now)
    modified_at = Column(TIMESTAMP, nullable=False)

def record_label_to_json(record_label):
    return {
        'id': record_label.id,
        'name': record_label.name,
        'contract_value': record_label.contract_value,
        'expire_date': record_label.expire_date.strftime('%Y-%m-%d %H:%M:%S'),
        'created_at': record_label.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        'modified_at': record_label.modified_at.strftime('%Y-%m-%d %H:%M:%S')
}
