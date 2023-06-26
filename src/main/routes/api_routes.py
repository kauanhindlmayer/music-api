from flask import Flask
from main.routes.subscriptions import subscriptions_bp
from main.routes.genres import genres_bp
from main.routes.record_labels import record_labels_bp
from main.routes.musics import music_bp
from main.routes.artists import artists_bp

from infra.db.settings.connection import DBConnectionHandler
from infra.db.settings.base import Base

database = DBConnectionHandler()
Base.metadata.create_all(database.get_engine())

app = Flask(__name__)

app.register_blueprint(subscriptions_bp)
app.register_blueprint(genres_bp)
app.register_blueprint(record_labels_bp)
app.register_blueprint(music_bp)
app.register_blueprint(artists_bp)