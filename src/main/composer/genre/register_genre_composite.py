from src.presentation.controllers.genre.register_genre_controller import RegisterGenreRouter
from src.data.use_cases.genre.register import RegisterGenre
from src.infra.db.repositories.genre_repository import GenreRepository
from src.data.use_cases.genre.find import FindGenre


def register_genre_composer() -> RegisterGenreRouter:
    ''' Composing Register Genre Route
    :param - None
    :return - Object with Register Genre Route
    '''

    repository = GenreRepository()
    find_gere_user_case = FindGenre(repository)
    register_genre_use_case = RegisterGenre(repository, find_gere_user_case)
    register_genre_router = RegisterGenreRouter(register_genre_use_case)

    return register_genre_router