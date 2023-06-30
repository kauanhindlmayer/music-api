from abc import ABC, abstractmethod
from typing import List
from src.domain.models.artist import Artist

class ArtistRepositoryInterface(ABC):
    """ Interface to artist Repository """

    @abstractmethod
    def insert_artist(self, name: str, record_label_id: int) -> None: 
        """ Insert data in artist entity """

        raise Exception("Should implement method: insert_artist")

    @abstractmethod
    def select_artist(self, artist_id: str = None) -> List[Artist]:
        """ Select data in artist entity """

        raise Exception("Should implement method: select_artist")

    @abstractmethod
    def update_artist(self, artist_id: int, name: str = None, record_label_id: int = None) -> None:
        """ Update data in artist entity """

        raise Exception("Should implement method: update_artist")

    @abstractmethod
    def delete_artist(self, artist_id: int) -> None:
        """ Delete data in artist entity """

        raise Exception("Should implement method: delete_artist")