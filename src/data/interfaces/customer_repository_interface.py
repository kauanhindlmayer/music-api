from abc import ABC, abstractmethod
from typing import List
from src.domain.models.customer import Customer

class CustomerRepositoryInterface(ABC):
    """ Interface to Customer Repository """

    @abstractmethod
    def insert_customer(self, login: str, password: str, email: str, subscription_id: int) -> None: 
        """ Insert data in customer entity """

        raise Exception("Should implement method: insert_customer")


    @abstractmethod
    def select_customer(self, customer_id: int = None) -> List[Customer]: 
        """ Select data in customer entity """

        raise Exception("Should implement method: select_customer")


    @abstractmethod
    def update_customer(self, customer_id: int, login: str = None, password: str = None, email: str = None, subscription_id: int = None) -> None: 
        """ Update data in customer entity """

        raise Exception("Should implement method: update_customer")


    @abstractmethod
    def delete_customer(self, customer_id: int) -> None:
        """ Delete data in customer entity """

        raise Exception("Should implement method: delete_customer")
