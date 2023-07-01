from src.domain.entities.genre import Genre
from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

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
            'modified_at': genre.modified_at.strftime('%Y-%m-%d %H:%M:%S')
        } for genre in genres])
    
    def add(self):
        data = request.get_json()
        description = data['description']

        genre_found = self.session.query(Genre).filter_by(description=description).all()
        if genre_found:
            return jsonify({'error': 'Genre already exists!'}), 404

        now = datetime.now()
        genre = Genre(description=description, created_at=now, modified_at=now)
        self.session.add(genre)
        self.session.commit()
        genre_id = genre.id
        self.session.close()
        return jsonify({
            'id': genre_id,
            'description': description,
            'created_at': now.strftime('%Y-%m-%d %H:%M:%S'),
        }), 201
    
    def get_by_id(self, id):
        genre_found = self.session.query(Genre).get(id)
        self.session.close()
        if genre_found:
            return jsonify({
                'id': genre_found.id,
                'description': genre_found.description,
                'created_at': genre_found.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': genre_found.modified_at.strftime('%Y-%m-%d %H:%M:%S') 
            })
        else:
            return jsonify({'error': 'Genre not found'}), 404
        
    def update(self, id):
        data = request.get_json()
        description = data.get('description')

        genre_found = self.session.query(Genre).get(id)

        if not genre_found:
            return jsonify({'error': 'Genre not found'}), 404

        genre_found.description = description
        genre_found.modified_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Genre updated successfully'})
    
    def delete(self, id):
        genre_found = self.session.query(Genre).get(id)

        if not genre_found:
            return jsonify({'error': 'Genre not found'}), 404
        
        try:
            self.session.delete(genre_found)
            self.session.commit()
            self.session.close()
        except IntegrityError:
            self.session.rollback()
            return jsonify({'message': 'Cannot delete this item, it is associated with other tables'}),401
        
        return jsonify({'message': 'Genre deleted successfully'})