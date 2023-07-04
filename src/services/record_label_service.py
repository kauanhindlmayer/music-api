from typing import List
from datetime import datetime
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from src.domain.entities.record_label import RecordLabel


class RecordLabelService:
    def __init__(self, database):
        self.session = database.session

    def convert_record_label_to_json(self, record_label):
        return {
            'id': record_label.id,
            'name': record_label.name,
            'contract_value': record_label.contract_value,
            'expire_date': record_label.expire_date.strftime('%Y-%m-%d %H:%M:%S'),
            'created_at': record_label.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'modified_at': record_label.modified_at.strftime('%Y-%m-%d %H:%M:%S')
        }

    def get_all(self):
        record_labels: List[RecordLabel] = self.session.query(
            RecordLabel).all()
        self.session.close()
        return [self.convert_record_label_to_json(label) for label in record_labels], 200

    def body_param_error(self, param):
        return {"error": param+" is not valid"}

    def validate_name(self, record_label_dict: dict):
        name = record_label_dict.get("name")
        if not isinstance(name, str):
            return name, self.body_param_error("name")
        return name, None

    def validate_expire_date(self, record_label_dict: dict):
        expire_date = record_label_dict.get("expire_date")
        if not isinstance(expire_date, str):
            if not expire_date:
                return None, self.body_param_error("expire_date")
            try:
                datetime.strptime(expire_date, '%Y-%m-%d %H:%M:%S')
            except Exception:
                return expire_date, self.body_param_error("expire_date")
        return expire_date, None

    def validate_contract_value(self, record_label_dict: dict):
        contract_value = record_label_dict.get("contract_value")
        if not isinstance(contract_value, (float, int)):
            return contract_value, self.body_param_error("contract_value")
        return contract_value, None

    def add(self, data: dict):

        name, name_error_message = self.validate_name(data)
        if not (name) or name_error_message:
            return name_error_message, 400

        contract_value, contract_value_error_message = self.validate_contract_value(
            data)
        if not (contract_value) or contract_value_error_message:
            return contract_value_error_message, 400

        expire_date, expire_date_error_message = self.validate_expire_date(
            data)
        if not (expire_date) or expire_date_error_message:
            return expire_date_error_message, 400

        now = datetime.now()
        modified_at = now
        created_at = now

        expire_date = datetime.strptime(expire_date, "%Y-%m-%dT%H:%M:%S")

        record_label = RecordLabel(
            name=name,
            contract_value=contract_value,
            expire_date=expire_date,
            modified_at=modified_at,
            created_at=created_at
        )

        self.session.add(record_label)

        self.session.commit()
        record_label_id = record_label.id
        self.session.close()
        record_label.id = record_label_id

        return self.convert_record_label_to_json(record_label), 201

    def get_by_id(self, id):
        record_label = None

        record_label = self.session.query(RecordLabel).get(id)

        self.session.close()

        if record_label:
            return self.convert_record_label_to_json(record_label), 200
        else:
            return jsonify({'error': 'Record label not found'}), 404

    def update(self, id, data: dict):
        expire_date, expire_date_error_message = self.validate_expire_date(
            data)
        contract_value, contract_value_error_message = self.validate_contract_value(
            data)
        name, name_error_message = self.validate_name(data)

        record_label = self.session.query(RecordLabel).get(id)

        if not record_label:
            return jsonify({'error': 'Record label not found'}), 404

        if name and name_error_message:
            return self.body_param_error("name")
        if name:
            record_label.name = name

        if contract_value and contract_value_error_message:
            return self.body_param_error("contract_value")
        if contract_value:
            record_label.contract_value = contract_value

        if expire_date and expire_date_error_message:
            return self.body_param_error("expire_date")
        if expire_date:
            record_label.expire_date = expire_date

        record_label.modified_at = datetime.now()
        self.session.commit()
        self.session.close()

        return jsonify({'message': 'Record label updated successfully'}), 200

    def delete(self, id):
        record_label = self.session.query(RecordLabel).get(id)

        if not record_label:
            return {'error': 'Record label not found'}, 404
        try:
            self.session.delete(record_label)
            self.session.commit()
            self.session.close()
        except IntegrityError:
            self.session.rollback()
            return {'message': 'Cannot delete this item, it is associated with other tables'}, 400

        return {'message': 'Record label deleted successfully'}, 200
