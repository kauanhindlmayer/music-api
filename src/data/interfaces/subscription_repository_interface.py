from abc import ABC, abstractmethod
from typing import List
from src.domain.models.subscription import Subscription

class SubscriptionRepositoryInterface(ABC):
    """ Interface to subscription Repository """

    @abstractmethod
    def insert_subscription(self, description: str, value: int, limit: int) -> None: 
        """ Insert data in subscription entity """

        raise Exception("Should implement method: insert_subscription")

    @abstractmethod
    def select_subscription(self, subscription_id: str = None) -> List[Subscription]:
        """ Select data in subscription entity """

        raise Exception("Should implement method: select_subscription")

    @abstractmethod
    def update_subscription(self, subscription_id: int, description: str = None, value: int = None, limit: int = None) -> None:
        """ Update data in subscription entity """

        raise Exception("Should implement method: update_subscription")

    @abstractmethod
    def delete_subscription(self, subscription_id: int) -> None:
        """ Delete data in subscription entity """

        raise Exception("Should implement method: delete_subscription")