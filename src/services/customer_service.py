from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
import bcrypt
from src.domain.entities.customer import Customer
from src.domain.entities.subscription import Subscription


class CustomerService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        customers = self.session.query(Customer).all()
        for customer in customers:
            customer.subscription = self.session.query(
                Subscription).filter_by(id=customer.subscription_id).first()
        self.session.close()
        return jsonify([
            {
                'id': customer.id,
                'login': customer.login,
                'password': customer.password,
                'email': customer.email,
                'subscription': str(customer.subscription),
                'created_at': customer.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': customer.modified_at.strftime('%Y-%m-%d %H:%M:%S')
            } for customer in customers
        ])

    def add(self):
        data = request.get_json()
        login = data['login']
        password = str(data['password']).encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        email = data['email']
        subscription_id = data['subscription_id']
        now = datetime.now()

        customer = Customer(
            login=login,
            password=hashed,
            email=email,
            subscription_id=subscription_id,
            created_at=now,
            modified_at=now
        )

        self.session.add(customer)
        self.session.commit()

        customer_id = customer.id

        self.session.close()

        return jsonify({
            'id': customer_id,
            'login': login,
            'password': str(hashed),
            'email': email,
            'subscription_id': subscription_id,
            'created_at': now.strftime('%Y-%m-%d %H:%M:%S'),
            'modified_at': now.strftime('%Y-%m-%d %H:%M:%S')
        }), 201

    def get_by_id(self, id):
        customer = self.session.query(Customer).get(id)

        customer.subscription = self.session.query(
            Subscription).filter_by(id=customer.subscription_id).first()
        self.session.close()

        if not customer:
            return jsonify({'error': 'Customer not found'}), 404

        modified_at = customer.modified_at.strftime(
            '%Y-%m-%d %H:%M:%S') if customer.modified_at else None

        return jsonify({
            'id': customer.id,
            'login': customer.login,
            'password': customer.password,
            'email': customer.email,
            'subscription': str(customer.subscription),
            'created_at': customer.created_at,
            'modified_at': modified_at
        })

    def update(self, id):
        data = request.get_json
        login = data.get('login')
        password = str(data.get('password')).encode()
        hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        email = data.get('email')
        subscription_id = data.get('subscription_id')

        customer = self.session.query(Customer).get(id)

        if not customer:
            return jsonify({'error': 'Customer not found'}), 404

        if login:
            customer.login = login
        if password:
            customer.password = hashed
        if email:
            customer.email = email
        if subscription_id:
            customer.subscription_id = subscription_id

        customer.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({'message': 'Customer updated successfully'})

    def delete(self, id):
        customer = self.session.query(Customer).get(id)

        if not customer:
            return jsonify({'error': 'Customer not found'}), 404
        try:
            self.session.delete(customer)
            self.session.commit()
            self.session.close()
        except IntegrityError:
            self.session.rollback()
            return jsonify(
                {'message': 'Cannot delete this item, it is associated with other tables'}
            ), 401

        return jsonify({'message': 'Customer deleted successfully'})
