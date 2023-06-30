from abc import ABC, abstractmethod
from typing import Dict

class GenreDelete(ABC):
    """ Interface to DeleteGenre use case """

    @abstractmethod
    def delete(self, genre_id: int) -> Dict:
        """ Case """

        raise Exception("Should implement method: delete")