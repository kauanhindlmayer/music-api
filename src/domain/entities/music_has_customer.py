from infra.configs.db_base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from domain.entities.music import Music
from domain.entities.customer import Customer

class MusicHasCustomer(Base):
    __tablename__ = 'music_has_customers'
    id = Column(Integer, primary_key=True)
    music_id = Column(Integer, ForeignKey('musics.id'))
    customer_id = Column(Integer, ForeignKey('customers.id'))
    music = relationship("Music")
    customer = relationship("Customer")