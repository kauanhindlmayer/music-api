from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.domain.models.genre import Genre
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.genre import Genre as GenreEntity
from src.data.interfaces.genre_repository_interface import GenreRepositoryInterface
from datetime import datetime


class GenreRepository(GenreRepositoryInterface):
    """ Class to manage Genre Repository"""
    
    @classmethod
    def insert_genre(cls, description: str) -> None:
        """
        Insert data in genre entity
        :param  - description: genre description
        :return - tuple with new genre inserted informations
        """
          
        with DBConnectionHandler() as database:
            try:
                new_registry = GenreEntity(
                    description=description,
                )
                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                print(exception)
                raise exception

    @classmethod
    def select_genre(cls, genre_id: int = None, description: str = None) -> List[Genre]:
        """
        Select data in genre entity by id or none
        :param  - genre_id: Id of the registry
                - descriptoin: description of the registry
        :return - List with genres selected
        """

        try:
            query_data = None

            if genre_id:
                # Select by genre_id
                with DBConnectionHandler() as database:
                    genres = (
                        database.session
                            .query(GenreEntity)
                            .filter(GenreEntity.id == genre_id)
                            .one()
                    )
                    query_data = [genres]

            elif description:
                # Select by description
                with DBConnectionHandler() as database:
                    genres = (
                        database.session
                            .query(GenreEntity)
                            .filter(GenreEntity.description == description)
                            .one()
                    )
                    query_data = [genres]
            else:
                # Select all
                with DBConnectionHandler() as database:
                    genres = (
                            database.session
                                .query(GenreEntity)
                                .all()
                        )
                    query_data = genres
        
            return query_data

        except NoResultFound:
            return []
        except Exception as exception:
            database.session.rollback()
            print(exception)
            raise exception
        

    @classmethod
    def update_genre(cls, genre_id: int, description: str) -> None:
        """
        Insert data in genre entity
        :param  - genre_id: Id of the registry
                - description: genre description
        :return - tuple with new genre inserted informations
        """
          
        with DBConnectionHandler() as database:
            try:
                genre = database.session.query(Genre).get(id=genre_id)
                genre.description = description
                genre.modified_at = datetime.now()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                print(exception)
                raise exception
            

    @classmethod
    def delete_genre(cls, genre_id: int) -> None:
        """
        Delete data in genre entity
        :param  - genre_id: Id of the registry
        :return - None
        """
          
        with DBConnectionHandler() as database:
            try:
                genre = database.session.query(Genre).get(id=genre_id)
                database.session.delete(genre)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                print(exception)
                raise exception