from typing import Dict, List, Type
from src.data.use_cases.genre.find import FindGenre
from src.data.interfaces.genre_repository_interface import GenreRepositoryInterface as GenreRepository
from src.domain.use_cases.genre.register_genre import GenreRegister as RegistryGenreInterface
from src.domain.models.genre import Genre


class DeleteGenre(RegistryGenreInterface):
    """ Class to define usecase: Register Genre """

    def __init__(self, genre_repository: Type[GenreRepository], find_genre: Type[FindGenre]):
        self.genre_repository = genre_repository
        self.find_genre = find_genre

    def registry(self, description: str) -> Dict[bool, Genre]:
        """Registry pet
        :param  - description: genre description
        :return - Dictionary with informations of the process
        """

        response = None

        # Validating entry and trying to find a genre
        validate_entry = isinstance(description, str)
        genre = self.__find_genre_information(description)
        checker = validate_entry and genre["Success"]

        if checker:
            response = self.genre_repository.insert_genre(
                description=description
            )

        return {"Success": checker, "Data": response}

    def __find_genre_information(self, description: str) -> Dict[bool, List[Genre]]:
        """Check genreInfo Dicionaty and select genre
        :param - description: genre description
        :return - Dictionary with the response of find_genre use case
        """
        
        genre_founded = None

        if description:
            genre_founded = self.find_genre.by_description(description)
        else:
            return {"Success": False, "Data": None}

        return genre_founded