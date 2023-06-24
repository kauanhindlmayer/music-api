from domain.entities.genre import Genre
from datetime import datetime
from flask import request, jsonify

class GenreService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        genres = self.session.query(Genre).all()
        self.session.close()
        return jsonify([{
            'id': genre.id,
            'description': genre.description,
            'created_at': genre.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': genre.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        } for genre in genres])
    
    def add(self):
        data = request.get_json()
        description = data['description']
        created_at = datetime.now()
        updated_at = None
        genre = Genre(description=description, created_at=created_at, updated_at=updated_at)
        self.session.add(genre)
        self.session.commit()
        genre_id = genre.id
        self.session.close()
        return jsonify({
            'id': genre_id,
            'description': description,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': genre.updated_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 201
    
    def get_by_id(self, id):
        genre = self.session.query(Genre).get(id)
        self.session.close()
        if genre:
            return jsonify({
                'id': genre.id,
                'description': genre.description,
                'created_at': genre.created_at,
                'updated_at': genre.updated_at
            })
        else:
            return jsonify({'error': 'Subscription not found'}), 404
        
    def update(self, id):
        data = request.get_json()
        description = data.get('description')

        genre = self.session.query(Genre).get(id)

        if not genre:
            return jsonify({'error': 'Subscription not found'}), 404

        genre.description = description

        genre.updated_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Subscription updated successfully'})
    
    def delete(self, id):
        genre = self.session.query(Genre).get(id)

        if not genre:
            return jsonify({'error': 'Subscription not found'}), 404

        self.session.delete(genre)
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Subscription deleted successfully'})