
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, TIMESTAMP
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

app = Flask(__name__)
Base = declarative_base()

#modelo do plano, poderia ser uma classe, poderia mas n to a fim

class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True)
    description = Column(String(45), nullable=False)
    value = Column(DECIMAL(5, 2), nullable=False)
    limit = Column(Integer, nullable=False)
    created = Column(TIMESTAMP, nullable=False)
    modified = Column(TIMESTAMP, nullable=False, default=datetime.now)

#cria sessão com o banco, informações meramente ilustrativas, explicado com o rodar o banco na docker file
engine = create_engine('mysql://root:1234@localhost:3306/musicas')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

@app.route('/plans', methods=['GET'])
def get_all_plans():
    session = Session()
    plans = session.query(Plan).all()
    session.close()
    return jsonify([{
        'id': plan.id,
        'description': plan.description,
        'value': plan.value,
        'limit': plan.limit,
        'created': plan.created.strftime('%Y-%m-%d %H:%M:%S')
    } for plan in plans])


@app.route('/plans', methods=['POST'])
def add_plan():
    data = request.get_json()
    description = data['description']
    value = data['value']
    limit = data['limit']
    created = datetime.now()
    session = Session()
    plan = Plan(description=description, value=value, limit=limit, created=created)
    session.add(plan)
    session.commit()
    plan_id = plan.id
    session.close()
    return jsonify({
        'id': plan_id,
        'description': description,
        'value': value,
        'limit': limit,
        'created': created.strftime('%Y-%m-%d %H:%M:%S')
    }), 201

@app.route('/plans/<int:id>', methods=['GET'])
def get_plan(id):
    session = Session()
    plan = session.query(Plan).get(id)
    session.close()
    if plan:
        return jsonify({
            'id': plan.id,
            'description': plan.description,
            'value': plan.value,
            'limit': plan.limit,
            'created': plan.created,
            'modified': plan.modified
        })
    else:
        return jsonify({'error': 'Plan not found'}), 404

@app.route('/plans/<int:id>', methods=['PUT'])
def update_plan(id):
    data = request.get_json()
    description = data.get('description')
    value = data.get('value')
    limit = data.get('limit')

    session = Session()
    plan = session.query(Plan).get(id)

    if not plan:
        return jsonify({'error': 'Plan not found'}), 404

    if description:
        plan.description = description
    if value:
        plan.value = value
    if limit:
        plan.limit = limit

    plan.modified = datetime.now()
    session.commit()
    session.close()

    return jsonify({'message': 'Plan updated successfully'})

@app.route('/plans/<int:id>', methods=['DELETE'])
def delete_plan(id):
    session = Session()
    plan = session.query(Plan).get(id)

    if not plan:
        return jsonify({'error': 'Plan not found'}), 404

    session.delete(plan)
    session.commit()
    session.close()

    return jsonify({'message': 'Plan deleted successfully'})

if __name__ == '__main__':
    app.run()