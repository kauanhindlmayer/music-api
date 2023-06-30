from abc import ABC, abstractmethod
from typing import List
from src.domain.models.record_label import RecordLabel

class RecordLabelRepositoryInterface(ABC):
    """ Interface to record_label Repository """

    @abstractmethod
    def insert_record_label(self, name: str, contract_value: int, expire_date: str) -> None: 
        """ Insert data in record_label entity """

        raise Exception("Should implement method: insert_record_label")

    @abstractmethod
    def select_record_label(self, record_label_id: str = None) -> List[RecordLabel]:
        """ Select data in record_label entity """

        raise Exception("Should implement method: select_record_label")

    @abstractmethod
    def update_record_label(self, record_label_id: int, name: str = None, contract_value: int = None, expire_date: str = None) -> None:
        """ Update data in record_label entity """

        raise Exception("Should implement method: update_record_label")

    @abstractmethod
    def delete_record_label(self, record_label_id: int) -> None:
        """ Delete data in record_label entity """

        raise Exception("Should implement method: delete_record_label")