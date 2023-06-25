from flask import Flask
from infra.configs.db_config import DBConnectionHandler
from infra.configs.db_base import Base
from services.subscription_service import SubcriptionService
from services.genre_service import GenreService
<<<<<<< HEAD
from services.record_label_service import RecordLabelService
=======
from services.music_service import MusicService
>>>>>>> 58f61fa041690d0b5bb0d1963e952ee3b71fc2b4

app = Flask(__name__)

database = DBConnectionHandler()
database.__enter__()
Base.metadata.create_all(database.get_engine())
subscription_service = SubcriptionService(database)
genre_service = GenreService(database)
<<<<<<< HEAD
record_label_service = RecordLabelService(database)
=======
music_service = MusicService(database)
>>>>>>> 58f61fa041690d0b5bb0d1963e952ee3b71fc2b4

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

<<<<<<< HEAD
@app.route('/record-labels', methods=['GET'])
def get_record_labels():
    return record_label_service.get_all()

@app.route('/record-labels', methods=['POST'])
def add_record_label():
    return record_label_service.add()

@app.route('/record-labels/<int:id>', methods=['GET'])
def get_record_labels_by_id(id):
    return record_label_service.get_by_id(id)

@app.route('/record-labels/<int:id>', methods=['PUT'])
def update_record_labels(id):
    return record_label_service.update(id)

@app.route('/record-labels/<int:id>', methods=['DELETE'])
def delete_record_labels(id):
    return record_label_service.delete(id)
=======
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
>>>>>>> 58f61fa041690d0b5bb0d1963e952ee3b71fc2b4

if __name__ == '__main__':
    app.run()
