from domain.entities.plan import Plan
from datetime import datetime
from flask import request, jsonify

class PlanService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        plans = self.session.query(Plan).all()
        self.session.close()
        return jsonify([{
            'id': plan.id,
            'description': plan.description,
            'value': plan.value,
            'limit': plan.limit,
            'created_at': plan.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for plan in plans])
    
    def add(self):
        data = request.get_json()
        description = data['description']
        value = data['value']
        limit = data['limit']
        created_at = datetime.now()
        plan = Plan(description=description, value=value, limit=limit, created_at=created_at)
        self.session.add(plan)
        self.session.commit()
        plan_id = plan.id
        self.session.close()
        return jsonify({
            'id': plan_id,
            'description': description,
            'value': value,
            'limit': limit,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 201
    
    def get_by_id(self, id):
        plan = self.session.query(Plan).get(id)
        self.session.close()
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
        
    def update(self, id):
        data = request.get_json()
        description = data.get('description')
        value = data.get('value')
        limit = data.get('limit')

        plan = self.session.query(Plan).get(id)

        if not plan:
            return jsonify({'error': 'Plan not found'}), 404

        if description:
            plan.description = description
        if value:
            plan.value = value
        if limit:
            plan.limit = limit

        plan.modified_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Plan updated successfully'})
    
    def delete(self, id):
        plan = self.session.query(Plan).get(id)

        if not plan:
            return jsonify({'error': 'Plan not found'}), 404

        self.session.delete(plan)
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Plan deleted successfully'})