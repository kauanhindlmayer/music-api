
from flask import Flask
from infra.configs.db_config import DBConnectionHandler
from infra.configs.db_base import Base
from services.plan_service import PlanService
from services.genre_service import GenreService

app = Flask(__name__)

database = DBConnectionHandler()
database.__enter__();
Base.metadata.create_all(database.get_engine())
plan_service = PlanService(database)
genre_service = GenreService(database)

@app.route('/subscriptions', methods=['GET'])
def get_all_plans(): 
    return plan_service.get_all()

@app.route('/subscriptions', methods=['POST'])
def add_plan():
    return plan_service.add()

@app.route('/subscriptions/<int:id>', methods=['GET'])
def get_plan_by_id(id):
    return plan_service.get_by_id(id)

@app.route('/subscriptions/<int:id>', methods=['PUT'])
def update_plan(id):
    return plan_service.update(id)

@app.route('/subscriptions/<int:id>', methods=['DELETE'])
def delete_plan(id):
    return plan_service.delete(id)

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

if __name__ == '__main__':
    app.run()