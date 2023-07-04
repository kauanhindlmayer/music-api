import pytest
from src.domain.entities.record_label import RecordLabel

@pytest.fixture
def in_memory_database():
    return []


def test_create_record_label(in_memory_database):
    record_label = RecordLabel(
        name='Label 1',
        contract_value=1000000,
        expire_date='2023-07-03 00:00:00'
    )
    record_label.id = 1
    in_memory_database.append(record_label)

    assert len(in_memory_database) == 1
    assert record_label.id == 1
    assert record_label.name == 'Label 1'
    assert record_label.contract_value == 1000000
    assert record_label.expire_date == '2023-07-03 00:00:00'


def test_update_record_label(in_memory_database):
    record_label = RecordLabel(
        name='Label 1',
        contract_value=1000000,
        expire_date='2023-07-03 00:00:00'
    )
    in_memory_database.append(record_label)

    record_label.name = 'Label 2'
    record_label.contract_value = 2000000
    record_label.expire_date = '2024-07-03 00:00:00'

    assert record_label.name == 'Label 2'
    assert record_label.contract_value == 2000000
    assert record_label.expire_date == '2024-07-03 00:00:00'


def test_delete_record_label(in_memory_database):
    record_label = RecordLabel(
        name='Label 1',
        contract_value=1000000,
        expire_date='2023-07-03 00:00:00'
    )
    in_memory_database.append(record_label)

    in_memory_database.remove(record_label)

    assert len(in_memory_database) == 0


def test_get_record_label_by_id(in_memory_database):
    first_record_label = RecordLabel(
        name='Label 1',
        contract_value=1000000,
        expire_date='2023-07-03 00:00:00'
    )
    first_record_label.id = 1
    second_record_label = RecordLabel(
        name='Label 2',
        contract_value=2000000,
        expire_date='2024-07-03 00:00:00'
    )
    second_record_label.id = 2
    in_memory_database.extend([first_record_label, second_record_label])

    retrieved_record_label = next(
        (record_label for record_label in in_memory_database if record_label.id == 2), None
    )

    assert retrieved_record_label.name == 'Label 2'
    assert retrieved_record_label.contract_value == 2000000
    assert retrieved_record_label.expire_date == '2024-07-03 00:00:00'


def test_get_all_record_labels(in_memory_database):
    first_record_label = RecordLabel(
        name='Label 1',
        contract_value=1000000,
        expire_date='2023-07-03 00:00:00'
    )
    second_record_label = RecordLabel(
        name='Label 2',
        contract_value=2000000,
        expire_date='2024-07-03 00:00:00'
    )
    in_memory_database.extend([first_record_label, second_record_label])

    all_record_labels = in_memory_database

    assert len(all_record_labels) == 2
    assert first_record_label in all_record_labels
    assert second_record_label in all_record_labels
