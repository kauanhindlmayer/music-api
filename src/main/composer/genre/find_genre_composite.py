from src.presentation.controllers.genre.find_genre_controller import FindGenreRouter
from src.data.use_cases.genre.find import FindGenre
from src.infra.db.repositories.genre_repository import GenreRepository


def find_genre_composer() -> FindGenreRouter:
    ''' Composing Find Genre Route
    :param - None
    :return - Object with Find Genre Route
    '''

    repository = GenreRepository()
    use_case = FindGenre(repository)
    find_genre_router = FindGenreRouter(use_case)

    return find_genre_router