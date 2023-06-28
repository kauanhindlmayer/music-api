from infra.db.settings.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from infra.db.entities.music import Music
from infra.db.entities.artist import Artist

class MusicHasArtist(Base):
    __tablename__ = 'music_has_artists'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    music_id = Column(Integer, ForeignKey('musics.id'))
    artist_id = Column(Integer, ForeignKey('artists.id'))
    music = relationship("Music")
    artist = relationship("Artist")

    def __repr__(self):
        return f"MusicHasArtist [id={self.id}, music_id={self.music_id}, artist_id={self.artist_id}]"