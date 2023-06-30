from abc import ABC, abstractmethod
from typing import List
from src.domain.models.genre import Genre

class GenreRepositoryInterface(ABC):
    """ Interface to genre Repository """

    @abstractmethod
    def insert_genre(self, description: str) -> None: 
        """ Insert data in genre entity """

        raise Exception("Should implement method: insert_genre")

    @abstractmethod
    def select_genre(self, genre_id: int = None, description: str = None) -> List[Genre]:
        """ Select data in genre entity """

        raise Exception("Should implement method: select_genre")

    @abstractmethod
    def update_genre(self, genre_id: int, description: str) -> None:
        """ Update data in genre entity """

        raise Exception("Should implement method: update_genre")

    @abstractmethod
    def delete_genre(self, genre_id: int) -> None:
        """ Delete data in genre entity """

        raise Exception("Should implement method: delete_genre")