from flask import Response
import pytest
from src.domain.entities.record_label import RecordLabel
from src.services.record_label_service import RecordLabelService

class DataBaseSessionMock():
    def __init__(self):
        self.count = 1;
        self.arr = [];

    def commit(self):
        pass;
    def close(self):
        pass;

    def query(self, one=1, two=2, three=3):
        return self;

    def add(self, record_label):
        record_label.id = self.count;
        self.count += 1;
        self.arr.append(record_label)
        return record_label;

    def get(self, search_id):
        for record_label in self.arr:
            if record_label.id == search_id:
                return record_label
        return None

    def delete(self, search_id):
        for record_label in self.arr:
            if record_label.id == search_id:
                self.arr.remove(record_label);
                return record_label;
        return None

    def all(self):
        return self.arr;

class DataBaseMock():
    def __init__(self):
        self.session = DataBaseSessionMock()

def test_create_record_label():
    database_mock = DataBaseMock()

    record_label_service = RecordLabelService(database_mock);

    record_label_to_create = {
        "name": 'Label 1',
        "contract_value": 1000000,
        "expire_date": '2023-07-03T00:00:00'
    }

    create_result, status = record_label_service.add(record_label_to_create);
    
    assert type(create_result) == dict 
    assert create_result["name"] == record_label_to_create["name"]; 
    assert create_result["contract_value"] == record_label_to_create["contract_value"]; 
    assert status == 201; 

def test_get_record_label_by_id():
    database_mock = DataBaseMock()

    record_label_service = RecordLabelService(database_mock);

    record_label_to_create = {
        "name": 'Label 1',
        "contract_value": 1000000,
        "expire_date": '2023-07-03T00:00:00'
    }

    create_result, status = record_label_service.add(record_label_to_create);
    
    assert type(create_result) == dict 

    found_record_label, status = record_label_service.get_by_id(create_result["id"]);

    assert type(found_record_label) == dict 
    assert found_record_label["id"] == create_result["id"] 

def test_delete_record_label_by_id():
    database_mock = DataBaseMock()

    record_label_service = RecordLabelService(database_mock);

    record_label_to_create = {
        "name": 'Label 1',
        "contract_value": 1000000,
        "expire_date": '2023-07-03T00:00:00'
    }

    create_result, status = record_label_service.add(record_label_to_create);
    
    assert isinstance(create_result, dict)

    deleted_record_label, status = record_label_service.delete(create_result["id"]);

    assert isinstance(deleted_record_label, dict)

    assert status == 200
    assert deleted_record_label["message"] == "Record label deleted successfully"

def test_get_all_record_label_by_id():
    database_mock = DataBaseMock()

    record_label_service = RecordLabelService(database_mock);

    record_label_to_create = {
        "name": 'Label 1',
        "contract_value": 1000000,
        "expire_date": '2023-07-03T00:00:00'
    }

    create_result, status = record_label_service.add(record_label_to_create);
    
    assert isinstance(create_result, dict)

    deleted_record_label, status = record_label_service.get_all();

    assert isinstance(deleted_record_label, list)
    assert len(deleted_record_label);
    assert status == 200
