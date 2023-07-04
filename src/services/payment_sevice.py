from datetime import datetime
from flask import request, jsonify
from sqlalchemy.exc import IntegrityError
from src.domain.entities.payment import Payment


class PaymentService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        payments = self.session.query(Payment).all()
        self.session.close()
        return jsonify([
            {
                'id': payment.id,
                'payment_date': payment.payment_date.strftime('%Y-%m-%d %H:%M:%S'),
                'created_at': payment.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'modified_at': payment.modified_at.strftime('%Y-%m-%d %H:%M:%S')
            } for payment in payments
        ])

    def add(self):
        now = datetime.now()

        payment = Payment(
            payment_date=now,
            created_at=now,
            modified_at=now
        )

        self.session.add(payment)
        self.session.commit()

        payment_id = payment.id

        self.session.close()

        return jsonify({
            'id': payment_id,
            'payment_date': now.strftime('%Y-%m-%d %H:%M:%S'),
            'created_at': now.strftime('%Y-%m-%d %H:%M:%S'),
            'modified_at': now.strftime('%Y-%m-%d %H:%M:%S')
        }), 201

    def get_by_id(self, id):
        payment = self.session.query(Payment).get(id)
        
        self.session.close()

        if not payment:
            return jsonify({'error': 'Payment not found'}), 404

        modified_at = payment.modified_at.strftime(
            '%Y-%m-%d %H:%M:%S') if payment.modified_at else None

        return jsonify({
            'payment_date' : payment.payment_date,
            'created_at': payment.created_at,
            'modified_at': modified_at
        })

    def update(self, id):
        payment = self.session.query(Payment).get(id)

        if not payment:
            return jsonify({'error': 'Payment not found'}), 404

        payment.payment_date = datetime.now()
        payment.modified_at = datetime.now()

        self.session.commit()
        self.session.close()
        return jsonify({'message': 'Payment updated successfully'})

    def delete(self, id):
        payment = self.session.query(Payment).get(id)

        if not payment:
            return jsonify({'error': 'Payment not found'}), 404
        try:
            self.session.delete(payment)
            self.session.commit()
            self.session.close()
        except IntegrityError:
            self.session.rollback()
            return jsonify(
                {'message': 'Cannot delete this item, it is associated with other tables'}
            ), 401

        return jsonify({'message': 'Payment deleted successfully'})
