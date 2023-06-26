
from domain.entities.music import Music
from domain.entities.genre import Genre
from datetime import datetime
from flask import request, jsonify

from domain.entities.artist import Artist
from domain.entities.music_has_artist import MusicHasArtist

class MusicService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        musics = self.session.query(Music).all()
        
        for music in musics:
                music.genre = self.session.query(Genre).filter_by(id=music.genre_id).first()
                artists = self.session.query(Artist).join(MusicHasArtist).filter(MusicHasArtist.music_id == music.id)
                music.artists = artists.all()

        self.session.close()
        return jsonify([
            {
                'id': music.id,
                'name': music.name,
                'duration': music.duration.strftime('%Y-%m-%d %H:%M:%S'),
                'genre': str(music.genre),
                'artists':music.artists,
                'release_date': music.release_date.strftime('%Y-%m-%d %H:%M:%S'),
                'created_at': music.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': music.modified_at.strftime('%Y-%m-%d %H:%M:%S')
                } for music in musics
        ])

    def add(self,data):
        name = data['name']
        duration_str = data['duration']
        genre_id = data['genre_id']
        release_date_str = data['release_date']
        created_at = datetime.now()
        modified_at = datetime.now()

        duration = datetime.strptime(duration_str, "%Y-%m-%dT%H:%M:%SZ")

        # Convert release_date string to datetime object
        release_date = datetime.strptime(release_date_str, "%Y-%m-%dT%H:%M:%SZ")

        music = Music(
            name=name,
            duration=duration,
            genre_id=genre_id,
            release_date=release_date,
            created_at=created_at,
            modified_at=modified_at
        )

        self.session.add(music)
        self.session.commit()

        music_id = music.id

        self.session.close()

        return jsonify({
            'id': music_id,
            'name': name,
            'duration': duration,
            'genre_id': genre_id,
            'release_date': release_date,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'modified_at': modified_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 201

    def get_by_id(self, id):
        music = self.session.query(Music).get(id)
        self.session.close()

        if music:
            return jsonify({
                'id': music.id,
                'name': music.name,
                'duration': music.duration,
                'genre_id': music.genre_id,
                'release_date': music.release_date,
                'created_at': music.created_at,
                'modified_at': music.modified_at
            })
        else:
            return jsonify({'error': 'Music not found'}), 404

    def update(self, id):
        data = request.get_json()
        name = data.get('name')
        duration = data.get('duration')
        genre_id = data.get('genre_id')
        release_date = data.get('release_date')

        music = self.session.query(Music).get(id)

        if not music:
            return jsonify({'error': 'Music not found'}), 404

        if name:
            music.name = name
        if duration:
            music.duration = duration
        if genre_id:
            music.genre_id = genre_id
        if release_date:
            music.release_date = release_date

        music.modified_at = datetime.now()

        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Music updated successfully'})

    def delete(self, id):
        music = self.session.query(Music).get(id)

        if not music:
            return jsonify({'error': 'Music not found'}), 404

        self.session.delete(music)
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Music deleted successfully'})
