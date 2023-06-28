
from sqlalchemy import delete, desc

from infra.db.entities.music import Music
from datetime import datetime
from flask import request, jsonify
from infra.db.entities.artist import Artist
from infra.db.entities.customer import Customer

from infra.db.entities.genre import Genre
from infra.db.entities.music_has_artist import MusicHasArtist
from infra.db.entities.music_has_customer import MusicHasCustomer


class MusicService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        musics = self.session.query(Music).all()
        
        for music in musics:
                music.genre = self.session.query(Genre).filter_by(id=music.genre_id).first()
                artists = self.session.query(Artist).join(MusicHasArtist).filter(MusicHasArtist.music_id == music.id)
                customers = self.session.query(Customer).join(MusicHasCustomer).filter(MusicHasCustomer.music_id == music.id)
                music.artists = str(artists.all())
                music.customers = str(customers.all())

        self.session.close()
        return jsonify([
            {
                'id': music.id,
                'name': music.name,
                'duration': music.duration.strftime('%Y-%m-%d %H:%M:%S'),
                'genre': str(music.genre),
                'artists':music.artists,
                'customer':music.customers,
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

        music_id_bd = self.session.query(Music).order_by(desc(Music.id)).first()
        music_id = music_id_bd.id if music_id_bd else None

        request_artists= data['artist_id']
        request_customers= data['customer_id']
        for artist in request_artists:
            music_has_artists = MusicHasArtist(
                music_id=music_id,
                artist_id=artist
            )
            self.session.add(music_has_artists)

        for customer in request_customers:
            music_has_customers = MusicHasCustomer(
            music_id=music_id,
            customer_id=customer
            )
            self.session.add(music_has_customers)

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
        music.genre = self.session.query(Genre).filter_by(id=music.genre_id).first()
        artists = self.session.query(Artist).join(MusicHasArtist).filter(MusicHasArtist.music_id == music.id)
        customers = self.session.query(Customer).join(MusicHasCustomer).filter(MusicHasCustomer.music_id == music.id)
        music.artists = str(artists.all())
        music.customers = str(customers.all())

        self.session.close()

        if music:
            return jsonify({
                'id': music.id,
                'name': music.name,
                'duration': music.duration.strftime('%Y-%m-%d %H:%M:%S'),
                'genre': str(music.genre),
                'artists':music.artists,
                'customer':music.customers,
                'release_date': music.release_date.strftime('%Y-%m-%d %H:%M:%S'),
                'created_at': music.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': music.modified_at.strftime('%Y-%m-%d %H:%M:%S')
            })
        else:
            return jsonify({'error': 'Music not found'}), 404

    def update(self, id):
        data = request.get_json()
        name = data.get('name')
        duration = data.get('duration')
        genre_id = data.get('genre_id')
        artists_data = data.get('artist_id')
        release_date = data.get('release_date')
        customers_data = data.get('customer_id')

        music = self.session.query(Music).get(id)
        if not music:
            return jsonify({'error': 'Music not found'}), 404
        if artists_data:
             # Clear existing artists
            delete_statement = delete(MusicHasArtist).where(MusicHasArtist.music_id == music.id)
            self.session.execute(delete_statement)
            # Create new artist objects and add them to the relationship
            for artist in artists_data:
                artist_id = artist
                association = MusicHasArtist(music_id=music.id, artist_id=artist_id)
                self.session.add(association)
        if customers_data:
             # Clear existing customers
            delete_statement = delete(MusicHasCustomer).where(MusicHasCustomer.music_id == music.id)
            self.session.execute(delete_statement)
            # Create new customer objects and add them to the relationship
            for customer in customers_data:
                customer_id = customer
                association = MusicHasCustomer(music_id=music.id, customer_id=customer_id)
                self.session.add(association)
        if name:
            music.name = name
        if duration:
            music.duration = duration
        if genre_id:
            music.genre_id = genre_id

        if release_date:
            music.release_date = release_date

        print(music)       
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
