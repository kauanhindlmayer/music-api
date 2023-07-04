import pytest
from src.domain.entities.music import Music
from datetime import datetime

@pytest.fixture
def in_memory_database():
    return []

def test_create_music(in_memory_database):
    now = datetime.now()
    music = Music(
        name='Song 1',
        duration=now,
        genre_id=1,
        release_date=now,
        created_at=now,
        modified_at=now
    )
    music.id = 1
    in_memory_database.append(music)

    assert len(in_memory_database) == 1
    assert music.id == 1
    assert music.name == 'Song 1'
    assert music.duration == now
    assert music.genre_id == 1
    assert music.release_date == now
    assert music.created_at == now
    assert music.modified_at == now

def test_update_music(in_memory_database):
    now = datetime.now()
    music = Music(
        name='Song 1',
        duration=now,
        genre_id=1,
        release_date=now,
        created_at=now,
        modified_at=now
    )
    in_memory_database.append(music)
    
    now = datetime.now()

    music.name = 'Song 2'
    music.duration = now
    music.genre_id = 2
    music.release_date = now
    music.modified_at = now

    assert music.name == 'Song 2'
    assert music.duration == now
    assert music.genre_id == 2
    assert music.release_date == now
    assert music.modified_at == now

def test_delete_music(in_memory_database):
    music = Music(
        name='Song 1',
        duration=datetime.now(),
        genre_id=1,
        release_date=datetime.now(),
        created_at=datetime.now(),
        modified_at=datetime.now()
    )
    in_memory_database.append(music)

    in_memory_database.remove(music)

    assert len(in_memory_database) == 0

def test_get_music_by_id(in_memory_database):
    now = datetime.now()
    first_music = Music(
        name='Song 1',
        duration=now,
        genre_id=1,
        release_date=now,
        created_at=now,
        modified_at=now
    )
    first_music.id = 1
    second_music = Music(
        name='Song 2',
        duration=now,
        genre_id=2,
        release_date=now,
        created_at=now,
        modified_at=now
    )
    second_music.id = 2
    in_memory_database.extend([first_music, second_music])

    retrieved_music = next((m for m in in_memory_database if m.id == 2), None)

    assert retrieved_music.name == 'Song 2'
    assert retrieved_music.duration == now
    assert retrieved_music.genre_id == 2
    assert retrieved_music.release_date == now
    assert retrieved_music.created_at == now
    assert retrieved_music.modified_at == now

def test_get_all_musics(in_memory_database):
    first_music = Music(
        name='Song 1',
        duration=datetime.now(),
        genre_id=1,
        release_date=datetime.now(),
        created_at=datetime.now(),
        modified_at=datetime.now()
    )
    second_music = Music(
        name='Song 2',
        duration=datetime.now(),
        genre_id=2,
        release_date=datetime.now(),
        created_at=datetime.now(),
        modified_at=datetime.now()
    )
    in_memory_database.extend([first_music, second_music])

    all_musics = in_memory_database

    assert len(all_musics) == 2
    assert first_music in all_musics
    assert second_music in all_musics