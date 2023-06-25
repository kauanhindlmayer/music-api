from sqlalchemy import except_
from sqlalchemy.engine import create
from domain.entities.plan import Plan
from datetime import datetime
from flask import request, jsonify
from typing import List
from domain.entities.record_label import RecordLabel, record_label_to_json

ok_validate_message = "ok"

class RecordLabelService:
    def __init__(self, database):
        self.session = database.session

    def get_all(self):
        record_labels: List[RecordLabel] = self.session.query(RecordLabel).all()
        self.session.close()
        return jsonify(list(map(lambda label: record_label_to_json(label), record_labels)))

    def body_param_error(self, param):
        return { "error": param+" is not valid" }

    def validate_record_label(self, data: dict):
        if (not data.__contains__("name")):
            return False, self.body_param_error("name");
        else: 
            temp_name = data["name"];
            if not type(temp_name) is str:
                return False, self.body_param_error("name");

        if (not data.__contains__("contract_value")):
            return False, self.body_param_error("contract_value");
        else:
            temp_contract_value = data["contract_value"];
            if not(type(temp_contract_value) is float or type(temp_contract_value) is int):
                return False, self.body_param_error("contract_value");

        if (not data.__contains__("expire_date")):
            return False, self.body_param_error("expire_date");
        else: 
            try:
                datetime.strptime(data["expire_date"], '%Y-%m-%d %H:%M:%S');
            except:
                return False, self.body_param_error("expire_date");

        return  True, ok_validate_message;
    
    def add(self):
        data: dict = request.get_json()

        valid, message = self.validate_record_label(data);

        if not valid:
            return jsonify(message), 400

        name = data["name"];
        contract_value = data["contract_value"];
        expire_date = data["expire_date"];

        now = datetime.now();

        modified_at = now;
        created_at = now;

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
        
        return record_label_to_json(record_label);
    
    def get_by_id(self, id):
        record_label = None;

        if id.isdecimal():
            record_label = self.session.query(RecordLabel).get(id)
        else:
            return jsonify({'error': 'id is not valid'}), 404

        self.session.close()

        if record_label:
            return record_label_to_json(record_label);
        else:
            return jsonify({'error': 'Record label not found'}), 404
        
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
