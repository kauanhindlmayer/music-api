from flask import Blueprint
from infra.db.settings.connection import DBConnectionHandler
from services.subscription_service import SubcriptionService

database = DBConnectionHandler()
database.__enter__()
subscription_service = SubcriptionService(database)

subscriptions_bp = Blueprint('subscriptions', __name__)

@subscriptions_bp.route('/subscriptions', methods=['GET'])
def get_all_subscriptions():
    return subscription_service.get_all()

@subscriptions_bp.route('/subscriptions', methods=['POST'])
def add_subscription():
    return subscription_service.add()

@subscriptions_bp.route('/subscriptions/<int:id>', methods=['GET'])
def get_subscription_by_id(id):
    return subscription_service.get_by_id(id)

@subscriptions_bp.route('/subscriptions/<int:id>', methods=['PUT'])
def update_subscription(id):
    return subscription_service.update(id)

@subscriptions_bp.route('/subscriptions/<int:id>', methods=['DELETE'])
def delete_subscription(id):
    return subscription_service.delete(id)