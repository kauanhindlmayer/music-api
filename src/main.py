
from flask import Flask
from infra.configs.db_config import DBConnectionHandler
from infra.configs.db_base import Base
from services.subscription_service import SubcriptionService
from services.genre_service import GenreService
from services.music_service import MusicService

app = Flask(__name__)

database = DBConnectionHandler()
database.__enter__()
Base.metadata.create_all(database.get_engine())
subscription_service = SubcriptionService(database)
genre_service = GenreService(database)
music_service = MusicService(database)

@app.route('/subscriptions', methods=['GET'])
def get_all_subscriptions(): 
    return subscription_service.get_all()

@app.route('/subscriptions', methods=['POST'])
def add_subscription():
    return subscription_service.add()

@app.route('/subscriptions/<int:id>', methods=['GET'])
def get_subscription_by_id(id):
    return subscription_service.get_by_id(id)

@app.route('/subscriptions/<int:id>', methods=['PUT'])
def update_subscription(id):
    return subscription_service.update(id)

@app.route('/subscriptions/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    return subscription_service.delete(id)

@app.route('/genres', methods=['GET'])
def get_all_genres(): 
    return genre_service.get_all()

@app.route('/genres', methods=['POST'])
def add_genre():
    return genre_service.add()

@app.route('/genres/<int:id>', methods=['GET'])
def get_genre_by_id(id):
    return genre_service.get_by_id(id)

@app.route('/genres/<int:id>', methods=['PUT'])
def update_genre(id):
    return genre_service.update(id)

@app.route('/genres/<int:id>', methods=['DELETE'])
def delete_genre(id):
    return genre_service.delete(id)

@app.route('/music', methods=['GET'])
def get_all_music(): 
    return music_service.get_all()

@app.route('/music', methods=['POST'])
def add_music():
    return music_service.add()

@app.route('/music/<int:id>', methods=['GET'])
def get_music_by_id(id):
    return music_service.get_by_id(id)

@app.route('/music/<int:id>', methods=['PUT'])
def update_music(id):
    return music_service.update(id)

@app.route('/music/<int:id>', methods=['DELETE'])
def delete_music(id):
    return music_service.delete(id)

if __name__ == '__main__':
    app.run()