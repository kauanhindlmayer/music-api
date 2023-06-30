from src.presentation.controllers.genre.delete_genre_controller import DeleteGenreRouter
from src.data.use_cases.genre.delete import DeleteGenre
from src.infra.db.repositories.genre_repository import GenreRepository


def delete_genre_composer() -> DeleteGenreRouter:
    ''' Composing Delete Genre Route
    :param - None
    :return - Object with Delete Genre Route
    '''

    repository = GenreRepository()
    use_case = DeleteGenre(repository)
    delete_genre_router = DeleteGenreRouter(use_case)

    return delete_genre_router