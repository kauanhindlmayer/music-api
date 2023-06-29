from flask import Blueprint
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.genre_service import GenreService

database = DBConnectionHandler()
database.__enter__()
genre_service = GenreService(database)

genres_bp = Blueprint('genres', __name__)

@genres_bp.route('/genres', methods=['GET'])
def get_all_genres():
    return genre_service.get_all()

@genres_bp.route('/genres', methods=['POST'])
def add_genre():
    return genre_service.add()

@genres_bp.route('/genres/<int:id>', methods=['GET'])
def get_genre_by_id(id):
    return genre_service.get_by_id(id)

@genres_bp.route('/genres/<int:id>', methods=['PUT'])
def update_genre(id):
    return genre_service.update(id)

@genres_bp.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre(id):
    return genre_service.delete(id)