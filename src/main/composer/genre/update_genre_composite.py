from src.presentation.controllers.genre.update_genre_controller import UpdateGenreRouter
from src.data.use_cases.genre.update import UpdateGenre
from src.infra.db.repositories.genre_repository import GenreRepository


def update_genre_composer() -> UpdateGenreRouter:
    ''' Composing Update Genre Route
    :param - None
    :return - Object with Update Genre Route
    '''

    repository = GenreRepository()
    use_case = UpdateGenre(repository)
    update_genre_router = UpdateGenreRouter(use_case)

    return update_genre_router