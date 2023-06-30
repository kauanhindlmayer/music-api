from abc import ABC, abstractmethod
from typing import Dict
from src.domain.models.genre import Genre

class GenreRegister(ABC):
    """ Interface to RegisterGenre use case """

    @abstractmethod
    def registry(self, description: str) -> Dict[bool, Genre]: 
        """ Case """

        raise Exception("Should implement method: registry")