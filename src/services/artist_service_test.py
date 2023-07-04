import pytest
from src.domain.entities.artist import Artist

@pytest.fixture
def in_memory_database():
    return []

def test_create_artist(in_memory_database):
    artist = Artist(name='Jeferson', record_label_id=1)
    artist.id = 1
    in_memory_database.append(artist)

    assert len(in_memory_database) == 1
    assert artist.id == 1
    assert artist.name == 'Jeferson'
    assert artist.record_label_id == 1

def test_update_artist(in_memory_database):
    artist = Artist(name='Jeferson', record_label_id=1)
    in_memory_database.append(artist)

    artist.name = 'Jeferson'

    assert artist.name == 'Jeferson'

def test_delete_artist(in_memory_database):
    artist = Artist(name='Jeferson', record_label_id=1)
    in_memory_database.append(artist)

    in_memory_database.remove(artist)

    assert len(in_memory_database) == 0

def test_get_artist_by_id(in_memory_database):
    first_artist = Artist(name='Jeferson', record_label_id=1)
    first_artist.id = 1
    second_artist = Artist(name='Jeferson', record_label_id=2)
    second_artist.id = 2
    in_memory_database.extend([first_artist, second_artist])

    retrieved_artist = next((artist for artist in in_memory_database if artist.id == 2), None)

    assert retrieved_artist.name == 'Jeferson'
    assert retrieved_artist.record_label_id == 2

def test_get_all_artists(in_memory_database):
    first_artist = Artist(name='Jeferson', record_label_id=1)
    second_artist = Artist(name='Jeferson', record_label_id=2)
    in_memory_database.extend([first_artist, second_artist])

    all_artists = in_memory_database

    assert len(all_artists) == 2
    assert first_artist in all_artists
    assert second_artist in all_artists