from flask import Blueprint
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.customer_service import CustomerService

database = DBConnectionHandler()
database.__enter__()
customer_service = CustomerService(database)

customers_bp = Blueprint('customers', __name__)

@customers_bp.route('/customers', methods=['GET'])
def get_all_customers():
    return customer_service.get_all()

@customers_bp.route('/customers', methods=['POST'])
def add_customer():
    return customer_service.add()

@customers_bp.route('/customers/<int:id>', methods=['GET'])
def get_customer_by_id(id):
    return customer_service.get_by_id(id)

@customers_bp.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    return customer_service.update(id)

@customers_bp.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    return customer_service.delete(id)