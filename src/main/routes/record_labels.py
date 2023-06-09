from flask import Blueprint, jsonify, request
from src.infra.db.settings.connection import DBConnectionHandler
from src.services.record_label_service import RecordLabelService

database = DBConnectionHandler()
database.__enter__()
record_label_service = RecordLabelService(database)

record_labels_bp = Blueprint('record_labels', __name__)


@record_labels_bp.route('/record-labels', methods=['GET'])
def get_record_labels():
    body, status = record_label_service.get_all()
    return jsonify(body), status; 


@record_labels_bp.route('/record-labels', methods=['POST'])
def add_record_label():
    return record_label_service.add(request.get_json())


@record_labels_bp.route('/record-labels/<int:id>', methods=['GET'])
def get_record_labels_by_id(id):
    return record_label_service.get_by_id(id)


@record_labels_bp.route('/record-labels/<int:id>', methods=['PUT'])
def update_record_labels(id):
    return record_label_service.update(id, request.get_json())


@record_labels_bp.route('/record-labels/<int:id>', methods=['DELETE'])
def delete_record_labels(id):
    body, status = record_label_service.delete(id)
    return jsonify(body), status
