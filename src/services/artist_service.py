from domain.entities.artist import Artist
from datetime import datetime
from flask import request, jsonify

class ArtistService:
     def __init__(self, database):
        self.session = database.session

     def get_all(self):
        artists = self.session.query(Artist).all()
        self.session.close()
        return jsonify([
            {
                'id': artist.id,
                'name': artist.name,
                'record_label_id': artist.record_label_id,
                'created_at': artist.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': artist.modified_at.strftime('%Y-%m-%d %H:%M:%S') if artist.modified_at else None
            }
            for artist in artists
        ])

     def add(self):
        data = request.get_json()
        name = data['name']
        record_label_id = data['record_label_id']
        created_at = datetime.now()

        artist = Artist(name=name, record_label_id=record_label_id, created_at=created_at)
        self.session.add(artist)
        self.session.commit()

        artist_id = artist.id
        self.session.close()

        return jsonify({
            'id': artist_id,
            'name': name,
            'record_label_id': record_label_id,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 201

     def get_by_id(self, id):
        artist = self.session.query(Artist).get(id)
        self.session.close()

        if artist:
            return jsonify({
                'id': artist.id,
                'name': artist.name,
                'record_label_id': artist.record_label_id,
                'created_at': artist.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': artist.modified_at.strftime('%Y-%m-%d %H:%M:%S') if artist.modified_at else None
            })
        else:
            return jsonify({'error': 'Artist not found'}), 404

     def update(self, id):
        data = request.get_json()
        name = data.get('name')
        record_label_id = data.get('record_label_id')

        artist = self.session.query(Artist).get(id)

        if not artist:
            return jsonify({'error': 'Artist not found'}), 404

        if name:
            artist.name = name
        if record_label_id:
            artist.record_label_id = record_label_id

        artist.modified_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Artist updated successfully'})

     def delete(self, id):
        artist = self.session.query(Artist).get(id)

        if not artist:
            return jsonify({'error': 'Artist not found'}), 404

        self.session.delete(artist)
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Artist deleted successfully'})