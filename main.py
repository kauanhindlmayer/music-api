
from flask import Flask, request, jsonify
from src.domain.entities.plans import Plan
from src.infra.configs.db_config import DBConnectionHandler
from datetime import datetime
from src.infra.configs.db_base import Base
from src.services.plan_service import PlanService

app = Flask(__name__)

database = DBConnectionHandler()
database.__enter__();
Base.metadata.create_all(database.get_engine())
plan_service = PlanService(database)

@app.route('/plans', methods=['GET'])
def get_all_plans(): 
    return plan_service.get_all()

@app.route('/plans', methods=['POST'])
def add_plan():
    return plan_service.add()

@app.route('/plans/<int:id>', methods=['GET'])
def get_plan(id):
    return plan_service.get_by_id(id)

@app.route('/plans/<int:id>', methods=['PUT'])
def update_plan(id):
    return plan_service.update(id)

@app.route('/plans/<int:id>', methods=['DELETE'])
def delete_plan(id):
    return plan_service.delete(id)

if __name__ == '__main__':
    app.run()