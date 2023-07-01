from src.domain.entities.subscription import Subscription
from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError

class SubcriptionService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        subscriptions = self.session.query(Subscription).all()
        self.session.close()
        return jsonify([{
            'id': subscription.id,
            'description': subscription.description,
            'value': subscription.value,
            'limit': subscription.limit,
            'created_at': subscription.created_at.strftime('%Y-%m-%d %H:%M:%S')
        } for subscription in subscriptions])
    
    def add(self):
        data = request.get_json()
        description = data['description']
        value = data['value']
        limit = data['limit']
        created_at = datetime.now()
        subscription = Subscription(description=description, value=value, limit=limit, created_at=created_at)
        self.session.add(subscription)
        self.session.commit()
        plan_id = subscription.id
        self.session.close()
        return jsonify({
            'id': plan_id,
            'description': description,
            'value': value,
            'limit': limit,
            'created_at': created_at.strftime('%Y-%m-%d %H:%M:%S')
        }), 201
    
    def get_by_id(self, id):
        subscription = self.session.query(Subscription).get(id)
        self.session.close()
        if subscription:
            return jsonify({
                'id': subscription.id,
                'description': subscription.description,
                'value': subscription.value,
                'limit': subscription.limit,
                'created_at': subscription.created_at,
                'modified_at': subscription.modified_at
            })
        else:
            return jsonify({'error': 'Subscription not found'}), 404
        
    def update(self, id):
        data = request.get_json()
        description = data.get('description')
        value = data.get('value')
        limit = data.get('limit')

        subscription = self.session.query(Subscription).get(id)

        if not subscription:
            return jsonify({'error': 'Subscription not found'}), 404

        if description:
            subscription.description = description
        if value:
            subscription.value = value
        if limit:
            subscription.limit = limit

        subscription.modified_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Subscription updated successfully'})
    
    def delete(self, id):
        subscription = self.session.query(Subscription).get(id)

        if not subscription:
            return jsonify({'error': 'Subscription not found'}), 404

        try:
            self.session.delete(subscription)
            self.session.commit()
            self.session.close()
        except  IntegrityError:
            self.session.rollback()
            return jsonify({'message': 'Não é possível excluir esse item, está associado a outras tabelas'}),401

        return jsonify({'message': 'Subscription deleted successfully'})
