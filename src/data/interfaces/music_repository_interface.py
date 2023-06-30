from abc import ABC, abstractmethod
from typing import List
from src.domain.models.music import Music

class MusicRepositoryInterface(ABC):
    """ Interface to music Repository """

    @abstractmethod
    def insert_music(self, name: str, duration: str, genre_id: int, release_date: str) -> None: 
        """ Insert data in music entity """

        raise Exception("Should implement method: insert_music")

    @abstractmethod
    def select_music(self, music_id: str = None) -> List[Music]:
        """ Select data in music entity """

        raise Exception("Should implement method: select_music")

    @abstractmethod
    def update_music(self, music_id: int, name: str = None, duration: str = None, genre_id: int = None, release_date: str = None) -> None:
        """ Update data in music entity """

        raise Exception("Should implement method: update_music")

    @abstractmethod
    def delete_music(self, music_id: int) -> None:
        """ Delete data in music entity """

        raise Exception("Should implement method: delete_music")