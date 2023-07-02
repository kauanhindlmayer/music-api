from flask import Flask
from src.main.routes.subscriptions import subscriptions_bp
from src.main.routes.genres import genres_bp
from src.main.routes.record_labels import record_labels_bp
from src.main.routes.musics import music_bp
from src.main.routes.artists import artists_bp
from src.main.routes.customers import customers_bp

from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.settings.base import Base

database = DBConnectionHandler()
try:
    Base.metadata.create_all(database.get_engine())
    app = Flask(__name__)

    app.register_blueprint(subscriptions_bp)
    app.register_blueprint(customers_bp)
    app.register_blueprint(genres_bp)
    app.register_blueprint(record_labels_bp)
    app.register_blueprint(music_bp)
    app.register_blueprint(artists_bp)

except:
    print("\nBanco de dados desconectado...")
