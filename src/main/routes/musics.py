from flask import Blueprint, request
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.music_service import MusicService

database = DBConnectionHandler()
database.__enter__()
music_service = MusicService(database)

music_bp = Blueprint('music', __name__)


@music_bp.route('/music', methods=['GET'])
def get_all_music():
    return music_service.get_all()


@music_bp.route('/music', methods=['POST'])
def add_music():
    data = request.get_json()
    return music_service.add(data)


@music_bp.route('/music/<int:id>', methods=['GET'])
def get_music_by_id(id):
    return music_service.get_by_id(id)


@music_bp.route('/music/<int:id>', methods=['PUT'])
def update_music(id):
    return music_service.update(id)


@music_bp.route('/music/<int:id>', methods=['DELETE'])
def delete_music(id):
    return music_service.delete(id)
