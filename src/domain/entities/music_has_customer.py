from src.infra.db.settings.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class MusicHasCustomer(Base):
    __tablename__ = 'music_has_customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    music_id = Column(Integer, ForeignKey('musics.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    music = relationship("Music")
    customer = relationship("Customer")
