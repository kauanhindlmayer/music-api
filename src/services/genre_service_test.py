import pytest
from src.domain.entities.genre import Genre

@pytest.fixture
def in_memory_database():
    return []

def test_create_genre(in_memory_database):
    genre = Genre(description='Rock')
    genre.id = 1
    in_memory_database.append(genre)

    assert len(in_memory_database) == 1
    assert genre.id == 1
    assert genre.description == 'Rock'

def test_update_genre(in_memory_database):
    genre = Genre(description='Rock')
    in_memory_database.append(genre)

    genre.description = 'Pop'

    assert genre.description == 'Pop'

def test_delete_genre(in_memory_database):
    genre = Genre(description='Rock')
    in_memory_database.append(genre)

    in_memory_database.remove(genre)

    assert len(in_memory_database) == 0

def test_get_genre_by_id(in_memory_database):
    first_genre = Genre(description='Rock')
    first_genre.id = 1
    second_genre = Genre(description='Pop')
    second_genre.id = 2
    in_memory_database.extend([first_genre, second_genre])

    retrieved_genre = next((genre for genre in in_memory_database if genre.id == 2), None)

    assert retrieved_genre.description == 'Pop'

def test_get_all_genres(in_memory_database):
    first_genre = Genre(description='Rock')
    second_genre = Genre(description='Pop')
    in_memory_database.extend([first_genre, second_genre])

    all_genres = in_memory_database

    assert len(all_genres) == 2
    assert first_genre in all_genres
    assert second_genre in all_genres
