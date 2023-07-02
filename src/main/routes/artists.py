from flask import Blueprint
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.artist_service import ArtistService

database = DBConnectionHandler()
database.__enter__()
artist_service = ArtistService(database)

artists_bp = Blueprint('artists', __name__)


@artists_bp.route('/artists', methods=['GET'])
def get_all_artists():
    return artist_service.get_all()


@artists_bp.route('/artists', methods=['POST'])
def add_artist():
    return artist_service.add()


@artists_bp.route('/artists/<int:id>', methods=['GET'])
def get_artist_by_id(id):
    return artist_service.get_by_id(id)


@artists_bp.route('/artists/<int:id>', methods=['PUT'])
def update_artist(id):
    return artist_service.update(id)


@artists_bp.route('/artists/<int:id>', methods=['DELETE'])
def delete_artist(id):
    return artist_service.delete(id)
