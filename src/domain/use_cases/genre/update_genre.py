from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.genre import Genre

class GenreUpdate(ABC):
    """ Interface to UpdateGenre use case """

    @abstractmethod
    def update(self, description: str) -> Dict[bool, Genre]: 
        """ Case """

        raise Exception("Should implement method: update")