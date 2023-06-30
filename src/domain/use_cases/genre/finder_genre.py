from abc import ABC, abstractmethod
from typing import Dict

class GenreFinder(ABC):
    """ Interface to UpdateGenre use case """

    @abstractmethod
    def find(self) -> Dict: 
        """ Case """

        raise Exception("Should implement method: find")

    @abstractmethod
    def by_description(self, description: str) -> Dict: 
        """ Case """

        raise Exception("Should implement method: by_description")

    @abstractmethod
    def by_genre_id(self, genre_id: int) -> Dict:
        """ Case """

        raise Exception("Should implement method: by_genre_id")