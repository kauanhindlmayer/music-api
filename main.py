
from flask import Flask, request, jsonify
from src.domain.entities.plans import Plan
from src.infra.configs.db_config import DBConnectionHandler
from datetime import datetime
from src.infra.configs.db_base import Base

app = Flask(__name__)

db = DBConnectionHandler()
db.__enter__();
Base.metadata.create_all(db.get_engine())


@app.route('/plans', methods=['GET'])
def get_all_plans():
    session = db.session
    plans = session.query(Plan).all()
    session.close()
    return jsonify([{
        'id': plan.id,
        'description': plan.description,
        'value': plan.value,
        'limit': plan.limit,
        'created_at': plan.created_at.strftime('%Y-%m-%d %H:%M:%S')
    } for plan in plans])


@app.route('/plans', methods=['POST'])
def add_plan():
    data = request.get_json()
    description = data['description']
    value = data['value']
    limit = data['limit']
    created_at = datetime.now()
    session = db.session
    plan = Plan(description=description, value=value, limit=limit, created_at=created_at)
    session.add(plan)
    session.commit()
    plan_id = plan.id
    session.close()
    return jsonify({
        'id': plan_id,
        'description': description,
        'value': value,
        'limit': limit,
        'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@app.route('/plans/<int:id>', methods=['GET'])
def get_plan(id):
    session = db.session
    plan = session.query(Plan).get(id)
    session.close()
    if plan:
        return jsonify({
            'id': plan.id,
            'description': plan.description,
            'value': plan.value,
            'limit': plan.limit,
            'created_at': plan.created_at,
            'modified_at': plan.modified_at
        })
    else:
        return jsonify({'error': 'Plan not found'}), 404

@app.route('/plans/<int:id>', methods=['PUT'])
def update_plan(id):
    data = request.get_json()
    description = data.get('description')
    value = data.get('value')
    limit = data.get('limit')

    session = db.session
    plan = session.query(Plan).get(id)

    if not plan:
        return jsonify({'error': 'Plan not found'}), 404

    if description:
        plan.description = description
    if value:
        plan.value = value
    if limit:
        plan.limit = limit

    plan.modified_at = datetime.now()
    session.commit()
    session.close()

    return jsonify({'message': 'Plan updated successfully'})

@app.route('/plans/<int:id>', methods=['DELETE'])
def delete_plan(id):
    session = db.session
    plan = session.query(Plan).get(id)

    if not plan:
        return jsonify({'error': 'Plan not found'}), 404

    session.delete(plan)
    session.commit()
    session.close()

    return jsonify({'message': 'Plan deleted successfully'})

if __name__ == '__main__':
    app.run()