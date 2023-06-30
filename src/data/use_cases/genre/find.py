from typing import Dict, List, Type
from src.domain.use_cases.genre.finder_genre import GenreFinder as GenreFinderInterface
from src.data.interfaces.genre_repository_interface import GenreRepositoryInterface as GenreRepository
from src.domain.models.genre import Genre

class FindGenre(GenreFinderInterface):
    """ Class to define usecase: Select Gnere """

    def __init__(self, genre_repository: GenreRepository) -> None:
      self.genre_repository = genre_repository

    def find(self) -> Dict[bool, List[Genre]]:
      """Select Genre
        :param - None
        :return - Dictionary with informations of the process
        """
      
      response = self.genre_repository.select_genre()

      return {"Success": True, "Data": response}

    def by_description(self, description: str) -> Dict[bool, List[Genre]]:
      """Select Genre By description
        :param - description: description of the genre
        :return - Dictionary with informations of the process
        """
      
      response = None
      validate_entry = isinstance(description, str)

      if validate_entry:
          response = self.genre_repository.select_genre(description=description)

      return {"Success": validate_entry, "Data": response}
    
    def by_genre_id(self, genre_id: int) -> Dict[bool, List[Genre]]:
        """Select Genre By genre_id
        :param - genre_id: id of the genre
        :return - Dictionary with informations of the process
        """

        response = None
        validate_entry = isinstance(genre_id, int)

        if validate_entry:
            response = self.genre_repository.select_genre(genre_id=genre_id)

        return {"Success": validate_entry, "Data": response}