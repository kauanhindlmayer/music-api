from infra.db.settings.connection import DBConnectionHandler
from infra.db.entities.genre import Genre as GenreEntity

class GenreRepository:
    
    @classmethod
    def insert_genre(cls, description: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = GenreEntity(
                    description=description,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_genre(cls, description: str) -> any:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session
                        .query(GenreEntity)
                        .filter(GenreEntity.description == description)
                        .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception