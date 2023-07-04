from flask import Blueprint
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.payment_sevice import PaymentService

database = DBConnectionHandler()
database.__enter__()
customer_service = PaymentService(database)

payments_bp = Blueprint('payments', __name__)


@payments_bp.route('/payments', methods=['GET'])
def get_all_payments():
    return customer_service.get_all()


@payments_bp.route('/payments', methods=['POST'])
def add_customer():
    return customer_service.add()


@payments_bp.route('/payments/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    return customer_service.get_by_id(id)


@payments_bp.route('/payments/<int:id>', methods=['PUT'])
def update_customer(id):
    return customer_service.update(id)


@payments_bp.route('/payments/<int:id>', methods=['DELETE'])
def delete_customer(id):
    return customer_service.delete(id)
